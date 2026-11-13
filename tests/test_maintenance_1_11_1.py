"""TASK-026, TASK-027 and TASK-028: follow-ups found while releasing v1.10.0 and v1.11.0."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def jobs(workflow):
    body = workflow.split("\njobs:\n", 1)[1]
    parts = re.split(r"(?m)^  ([\w-]+):\n", body)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts), 2)}


class VersionBadgeTests(unittest.TestCase):
    """TASK-026: the badge at the top of the READMEs must not look stale for hours after a release."""

    BADGE = ('<a href="https://github.com/dixi-project/dixi-spec-kit/releases/latest">'
             '<img src="https://img.shields.io/github/v/release/dixi-project/dixi-spec-kit?color=1f5fc4"')

    def test_readmes_show_the_latest_github_release(self):
        for name in ("README.md", "README.es.md"):
            with self.subTest(readme=name):
                text = read(name)
                self.assertEqual(text.count(self.BADGE), 1)
                self.assertNotIn("img.shields.io/pypi/v/", text)
                self.assertIn("https://pypi.org/project/dixi-spec-kit/", text)

    def test_publishing_guide_explains_the_delay_and_the_real_version(self):
        guide = read("docs/pypi-publishing.md")
        section = guide.split("\n## After a release\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("https://pypi.org/project/dixi-spec-kit/", section)
        self.assertIn("six hours", section)
        self.assertIn("five minutes", section)
        self.assertIn("`dixi --version`", section)


class VerifyWorkflowTests(unittest.TestCase):
    """TASK-027: a slow macOS runner queue must not fail a required check, and every job keeps a limit."""

    def setUp(self):
        self.text = read(".github/workflows/verify.yml")
        self.jobs = jobs(self.text)

    def limit(self, job):
        found = re.findall(r"(?m)^    timeout-minutes: (\d+)$", self.jobs[job])
        self.assertEqual(len(found), 1, job)
        return int(found[0])

    def test_every_job_has_a_limit_and_the_matrix_job_has_room_for_the_queue(self):
        self.assertEqual(set(self.jobs), {"verify", "windows-refusal", "dco"})
        self.assertEqual(self.limit("verify"), 30)
        self.assertEqual(self.limit("windows-refusal"), 10)
        self.assertEqual(self.limit("dco"), 5)

    def test_workflow_rules_are_kept(self):
        for action in re.findall(r"uses: (\S+)", self.text):
            self.assertRegex(action, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$", action)
        self.assertRegex(self.text, r"\npermissions:\n  contents: read\n")
        self.assertNotIn("secrets.", self.text)
        self.assertIn("macos-latest", self.jobs["verify"])

    def test_settings_say_what_to_do_when_a_job_is_cancelled_while_waiting(self):
        settings = read("docs/repository-settings.md")
        section = settings.split("\n## Checks cancelled while waiting for a runner\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("Re-run failed jobs", section)
        self.assertIn("30 minutes", section)
        self.assertIn("macOS", section)

    def test_settings_name_the_real_cause_of_the_cancellation(self):
        # Correction of TASK-027: GitHub cancels a job that no hosted runner acquires; `timeout-minutes` does not
        # count while the job waits, so raising it did not prevent the cancellation (seen again on 2026-11-13).
        settings = read("docs/repository-settings.md")
        section = settings.split("\n## Checks cancelled while waiting for a runner\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("The job was not acquired by Runner of type hosted", section)
        self.assertIn("`timeout-minutes` does not count while a job waits", section)
        self.assertNotIn("the rest for the macOS queue", section)
        workflow = read(".github/workflows/verify.yml")
        self.assertNotIn("leaves room for the macOS runner queue", workflow)
        task = read("tasks/backlog/TASK-027-macos-job-timeout.md")
        self.assertIn("\n## Correction\n", task)
        self.assertIn("2026-11-13", task.split("\n## Correction\n", 1)[1])


class IsolatedHandoffTests(unittest.TestCase):
    """TASK-028: an isolated agent session hands off without writing private content to the repository."""

    def test_local_development_describes_the_procedure(self):
        guide = read("docs/local-development.md")
        section = guide.split("\n## Handoff from an isolated agent session\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn("`.context/`", section)
        self.assertIn("cp ", section)
        self.assertIn("outside the repository", section)
        self.assertLess(guide.index("## Handoff from an isolated agent session"), guide.index("\n## Related\n"))

    def test_the_handoff_itself_is_not_in_the_repository(self):
        self.assertIn(".context/", read(".gitignore").splitlines())
        tracked = [path for path in ROOT.rglob("HANDOFF*.md") if ".context" not in path.parts
                   and not {".venv", ".git", "node_modules", ".claude"} & set(path.parts)]
        self.assertEqual(tracked, [])


if __name__ == "__main__":
    unittest.main()
