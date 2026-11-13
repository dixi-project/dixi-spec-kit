"""TASK-023: `make release` shows the merged pull requests that the CHANGELOG section does not mention."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("release_script_guard", ROOT / "scripts/release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)

LOG = """Merge pull request #57 from dixi-project/docs/cli-reference
Merge branch 'main' into docs/cli-reference
Merge pull request #56 from dixi-project/docs/command-examples
Merge pull request #5 from someone/fix/typo-in-readme
Merge pull request #49 from dixi-project/docs/changelog-init-existing
[docs] fix: a commit that is not a merge
"""
SECTION = """### Added

- CLI reference (#57): one page per terminal command.
- Examples in the command reference, from the docs/command-examples branch.

<!-- no changelog entry: #49 -->
"""
CHANGELOG = f"""# Changelog

## [Unreleased]

## [1.10.0] — 2026-11-13

{SECTION}
## [1.9.0] — 2026-11-12

- Older (#5).
"""


class ChangelogGuardTests(unittest.TestCase):
    def test_merged_pull_requests_are_parsed_from_merge_subjects(self):
        self.assertEqual(release.merged_pull_requests(LOG), [
            (57, "docs/cli-reference"), (56, "docs/command-examples"), (5, "fix/typo-in-readme"),
            (49, "docs/changelog-init-existing")])
        self.assertEqual(release.merged_pull_requests(""), [])

    def test_previous_tag_is_the_highest_version_below_this_one(self):
        tags = ["v1.9.0", "v1.8.0", "v1.10.0", "v1.2.0", "v2.0.0", "not-a-version", "v1.9"]
        self.assertEqual(release.previous_tag(tags, "1.10.0"), "v1.9.0")
        self.assertEqual(release.previous_tag(tags, "1.9.0"), "v1.8.0")
        self.assertEqual(release.previous_tag(tags, "2.0.0"), "v1.10.0")
        self.assertIsNone(release.previous_tag(["v1.0.0"], "1.0.0"))
        self.assertIsNone(release.previous_tag([], "1.0.0"))

    def test_unannounced_are_the_pull_requests_the_section_does_not_mention(self):
        pulls = release.merged_pull_requests(LOG)
        self.assertEqual(release.unannounced(pulls, SECTION), [(5, "fix/typo-in-readme")])
        self.assertEqual(release.unannounced(pulls, "### Added\n\n- Nothing relevant.\n"), pulls)
        self.assertEqual(release.unannounced([], SECTION), [])

    def test_a_number_matches_whole_and_a_branch_by_name(self):
        self.assertEqual(release.unannounced([(5, "fix/x")], "- See #57 and #50."), [(5, "fix/x")])
        self.assertEqual(release.unannounced([(5, "fix/x")], "- See (#5)."), [])
        self.assertEqual(release.unannounced([(5, "fix/x")], "- From fix/x."), [])
        self.assertEqual(release.unannounced([(5, "fix/x")], "- From fix/xylophone."), [(5, "fix/x")])

    def test_documentation_only_pull_requests_can_be_marked(self):
        marked = "### Added\n\n- One thing.\n\n<!-- no changelog entry: #49, #50 and #51 -->\n"
        self.assertEqual(release.no_entry_needed(marked), {49, 50, 51})
        self.assertEqual(release.no_entry_needed("- One thing.\n"), set())
        pulls = [(49, "docs/a"), (50, "docs/b"), (52, "feat/c")]
        self.assertEqual(release.unannounced(pulls, marked), [(52, "feat/c")])

    def test_the_marker_is_not_published_in_the_release_notes(self):
        notes = release.changelog_notes(CHANGELOG, "1.10.0")
        self.assertNotIn("no changelog entry", notes)
        self.assertNotIn("<!--", notes)
        self.assertIn("- CLI reference (#57)", notes)
        self.assertEqual(release.unannounced([(49, "docs/x")], release.changelog_section(CHANGELOG, "1.10.0")), [])

    def test_a_marker_quoted_inside_an_entry_is_text_not_a_marker(self):
        # TASK-025: the notes of v1.11.0 lost the example an entry quoted.
        entry = "- Pull requests that need no entry are marked with `<!-- no changelog entry: #7 -->`, which is left out."
        section = f"### Added\n\n{entry}\n- Another thing (#8).\n\n<!-- no changelog entry: #9 -->\n"
        changelog = f"# Changelog\n\n## [Unreleased]\n\n## [2.0.0] — 2026-11-13\n\n{section}\n## [1.0.0] — 2026-01-01\n\n- Old.\n"
        notes = release.changelog_notes(changelog, "2.0.0")
        self.assertIn(entry, notes)
        self.assertNotIn("#9", notes)
        self.assertEqual(notes.count("<!--"), 1)
        self.assertEqual(release.no_entry_needed(section), {9})
        pulls = [(7, "docs/a"), (8, "feat/b"), (9, "docs/c"), (10, "feat/d")]
        self.assertEqual(release.unannounced(pulls, section), [(10, "feat/d")])
        indented = "- One thing.\n\n  <!-- no changelog entry: #3 -->  \n"
        self.assertEqual(release.no_entry_needed(indented), {3})
        self.assertNotIn("<!--", release.NO_ENTRY.sub("", indented))

    def test_warning_names_each_pull_request_and_how_to_resolve_it(self):
        lines = release.changelog_warning([(5, "fix/typo-in-readme"), (60, "feat/x")], "v1.9.0", 4)
        text = "\n".join(lines)
        self.assertIn("v1.9.0", text)
        self.assertIn("#5 (fix/typo-in-readme)", text)
        self.assertIn("#60 (feat/x)", text)
        self.assertIn("<!-- no changelog entry: #5, #60 -->", text)
        self.assertEqual(release.changelog_warning([], "v1.9.0", 4),
                         ["All 4 pull requests merged since v1.9.0 are in the CHANGELOG section."])

    def test_the_person_confirms_before_continuing(self):
        asked = []

        def ask(prompt, answer):
            asked.append(prompt)
            return answer

        missing = [(5, "fix/typo-in-readme")]
        self.assertTrue(release.confirm_unannounced([], lambda prompt: ask(prompt, "no")))
        self.assertEqual(asked, [])
        self.assertTrue(release.confirm_unannounced(missing, lambda prompt: ask(prompt, " yes \n")))
        for answer in ("", "y", "no", "1.10.0"):
            self.assertFalse(release.confirm_unannounced(missing, lambda prompt: ask(prompt, answer)), answer)
        self.assertIn("yes", asked[0])

    def test_main_checks_the_changelog_before_asking_for_the_version(self):
        source = (ROOT / "scripts/release.py").read_text(encoding="utf-8")
        main = source.split("\ndef main(argv):", 1)[1]
        self.assertLess(main.index("confirm_unannounced("), main.index("to create the release"))
        self.assertLess(main.index("confirm_unannounced("), main.index('"gh", "release", "create"'))
        self.assertIn('"--merges"', source)
        self.assertIn('"--first-parent"', source)

    def test_guide_explains_the_check_and_the_marker(self):
        guide = (ROOT / "docs/pypi-publishing.md").read_text(encoding="utf-8")
        self.assertIn("<!-- no changelog entry: #", guide)
        self.assertIn("(#", guide)


if __name__ == "__main__":
    unittest.main()
