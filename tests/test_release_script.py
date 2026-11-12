"""`make release` refuses to create a GitHub release before the release PR is merged and dist/ is clean."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("release_script", ROOT / "scripts/release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)

GOOD = dict(version="1.8.0", main_version="1.8.0", local_head="abc", remote_head="abc", dirty=False,
            tag_exists=False, dist_names=["dixi_spec_kit-1.8.0-py3-none-any.whl", "dixi_spec_kit-1.8.0.tar.gz"])
CHANGELOG = """# Changelog

## [Unreleased]

## [1.8.0] — 2026-11-11

### Added

- Something new.

## [1.7.0] — 2026-11-11

- Older.
"""


class ReleaseGuardTests(unittest.TestCase):
    def problems(self, **changes):
        return release.release_problems(**{**GOOD, **changes})

    def test_ready_release_has_no_problems(self):
        self.assertEqual(self.problems(), [])

    def test_release_pr_not_merged(self):
        problems = self.problems(main_version="1.7.0")
        self.assertTrue(any("merge" in p for p in problems), problems)

    def test_local_checkout_not_at_public_main(self):
        self.assertTrue(self.problems(local_head="old"))
        self.assertTrue(self.problems(dirty=True))

    def test_existing_tag_is_refused(self):
        problems = self.problems(tag_exists=True)
        self.assertTrue(any("v1.8.0" in p for p in problems), problems)

    def test_dist_must_hold_exactly_this_version(self):
        self.assertTrue(self.problems(dist_names=GOOD["dist_names"] + ["dixi_spec_kit-1.7.0.tar.gz"]))
        self.assertTrue(self.problems(dist_names=["dixi_spec_kit-1.8.0.tar.gz"]))
        self.assertTrue(self.problems(dist_names=[]))

    def test_invalid_version_is_refused(self):
        for version in ("1.8", "v1.8.0", "1.8.0; rm -rf /", ""):
            with self.subTest(version=version):
                self.assertTrue(self.problems(version=version))

    def test_notes_come_from_the_changelog_section(self):
        self.assertEqual(release.changelog_notes(CHANGELOG, "1.8.0").strip(), "### Added\n\n- Something new.")
        with self.assertRaises(ValueError):
            release.changelog_notes(CHANGELOG, "1.9.0")

    def test_version_is_read_from_pyproject(self):
        self.assertEqual(release.pyproject_version('[project]\nname = "x"\nversion = "1.8.0"\n'), "1.8.0")

    def test_makefile_and_guide_use_the_guard(self):
        makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
        self.assertIn("release:", makefile)
        self.assertIn("scripts/release.py $(VERSION)", makefile)
        self.assertIn("make release VERSION=", (ROOT / "docs/pypi-publishing.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
