"""Check packaging failures without requiring external services or YAML packages."""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "validate_skills", Path(__file__).resolve().parents[1] / "scripts/validate_skills.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PackagingValidationTests(unittest.TestCase):
    def test_multiline_plain_description(self):
        fields, errors = validator.parse_frontmatter(
            "---\nname: sample\ndescription:\n  A library guide\n  across two lines.\nmetadata:\n  author: example\n---\nBody\n"
        )
        self.assertFalse(errors)
        self.assertEqual(fields["description"], "A library guide across two lines.")

    def test_folded_description(self):
        fields, errors = validator.parse_frontmatter(
            "---\nname: sample\ndescription: >-\n  A folded\n  description.\n---\nBody\n"
        )
        self.assertFalse(errors)
        self.assertEqual(fields["description"], "A folded description.")

    def test_empty_description_is_still_rejected(self):
        _, errors = validator.parse_frontmatter(
            "---\nname: sample\ndescription:\nmetadata:\n  author: someone\n---\nBody\n"
        )
        self.assertIn("missing frontmatter field: description", errors)

    def test_examples_do_not_become_file_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "guide.md"
            prose = "```markdown\n[Example](not-a-real-file.md)\n```\n`[Example](also-not-real.md)`\n"
            self.assertEqual(validator.validate_links(doc, prose), [])

    def test_longer_fence_keeps_nested_example_out_of_prose(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "guide.md"
            text = "````markdown\n```\n[Example](not-real.md)\n```\n````\n[Actual](missing.md)"
            self.assertEqual(validator.validate_links(doc, text), ["broken local link: missing.md"])

    def test_supporting_reference_link_is_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp)
            (skill / "SKILL.md").write_text("---\nname: sample\ndescription: A guide\n---\n[Guide](guide.md)\n")
            (skill / "guide.md").write_text("[Missing](missing.md)\n")
            self.assertIn("guide.md: broken local link: missing.md", validator.validate_skill(skill))
            (skill / "missing.md").write_text("Now available\n")
            self.assertEqual(validator.validate_skill(skill), [])

    def test_encoded_local_paths_and_remote_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "guide.md"
            (Path(tmp) / "two words.md").write_text("Content\n")
            text = "[Local](two%20words.md#section) [Web](https://example.com/a) [Heading](#title)"
            self.assertEqual(validator.validate_links(doc, text), [])

    def test_duplicate_discoverable_names_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ("one", "two"):
                skill = Path(tmp) / name
                skill.mkdir()
                (skill / "SKILL.md").write_text("---\nname: same-name\ndescription: A guide\n---\n")
            capture = io.StringIO()
            with patch.object(validator, "SKILLS_DIR", Path(tmp)), contextlib.redirect_stdout(capture):
                result = validator.main()
            self.assertEqual(result, 1)
            self.assertIn("duplicate declared name", capture.getvalue())

    def test_metadata_prompt_must_name_its_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp)
            (skill / "SKILL.md").write_text("---\nname: sample\ndescription: A guide\n---\n")
            (skill / "agents").mkdir()
            (skill / "agents/openai.yaml").write_text('interface:\n  default_prompt: "Use $another-skill"\n')
            self.assertIn("default_prompt does not mention the declared skill name", validator.validate_skill(skill))


if __name__ == "__main__":
    unittest.main()
