"""`init --existing --controls` accepts only agents with hooks, like `init` (ADR-108 phases C and D)."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InitExistingControlsTests(unittest.TestCase):
    def test_controls_need_an_agent_with_hooks(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder).resolve()
            env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
            for agent in ("none", "skills"):
                with self.subTest(agent=agent):
                    project = base / agent
                    project.mkdir()
                    (project / "app.py").write_text("x = 1\n")
                    result = subprocess.run([sys.executable, "-m", "dixi_spec_kit", "init", str(project), "--agent",
                                             agent, "--existing", "--controls"], cwd=base, env=env, text=True,
                                            capture_output=True, timeout=20)
                    self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                    self.assertEqual(sorted(p.name for p in project.iterdir()), ["app.py"])


if __name__ == "__main__":
    unittest.main()
