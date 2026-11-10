from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/publish.yml"


class PublishWorkflowTests(unittest.TestCase):
    """PyPI publication through Trusted Publishing (ADR-106): no stored secrets, least privilege."""

    def setUp(self):
        self.assertTrue(WORKFLOW.is_file(), "missing .github/workflows/publish.yml")
        self.text = WORKFLOW.read_text(encoding="utf-8")

    def jobs(self):
        body = self.text.split("\njobs:\n", 1)[1]
        parts = re.split(r"\n  (?=[a-z][a-z0-9_-]*:\n)", "\n" + body)
        return {part.split(":", 1)[0].strip(): part for part in parts if part.strip()}

    def test_runs_only_on_published_releases(self):
        triggers = self.text.split("\non:\n", 1)[1].split("\n\n", 1)[0]
        self.assertIn("release:", triggers)
        self.assertIn("types: [published]", triggers)
        for other in ("push:", "pull_request", "workflow_dispatch", "schedule"):
            self.assertNotIn(other, triggers)

    def test_least_privilege(self):
        top = self.text.split("\njobs:\n", 1)[0]
        self.assertRegex(top, r"\npermissions:\n  contents: read\n")
        jobs = self.jobs()
        self.assertEqual(set(jobs), {"build", "publish"})
        self.assertNotIn("id-token", jobs["build"])
        self.assertIn("id-token: write", jobs["publish"])
        self.assertIn("needs: build", jobs["publish"])
        self.assertRegex(jobs["publish"], r"environment:\n\s+name: pypi\n\s+url: https://pypi\.org/p/dixi-spec-kit")

    def test_no_stored_secrets_and_pinned_actions(self):
        self.assertNotIn("secrets.", self.text)
        self.assertNotIn("password:", self.text)
        uses = re.findall(r"uses: (\S+)", self.text)
        self.assertTrue(uses)
        for action in uses:
            self.assertRegex(action, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$", f"{action} must be pinned to a full commit SHA")
        self.assertTrue(any(a.startswith("pypa/gh-action-pypi-publish@") for a in uses))

    def test_builds_verified_artifacts_matching_the_tag(self):
        build = self.jobs()["build"]
        self.assertIn("persist-credentials: false", build)
        self.assertIn("--require-hashes -r requirements-build.txt", build)
        self.assertIn("make verify", build)
        self.assertIn("GITHUB_REF_NAME", build, "the job must compare the tag with the package version")
        self.assertIn("dist/", build)


if __name__ == "__main__":
    unittest.main()
