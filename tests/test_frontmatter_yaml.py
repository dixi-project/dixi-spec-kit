import json
from pathlib import Path
import re
import unittest


RESOURCES = Path(__file__).resolve().parents[1] / "src/dixi_spec_kit/resources"
PLAIN_SAFE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


class FrontmatterYamlTests(unittest.TestCase):
    def frontmatters(self):
        for path in sorted(RESOURCES.glob("*/*/dixi*.md")):
            match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.DOTALL)
            self.assertIsNotNone(match, path)
            yield path, match.group(1).splitlines()

    def test_resources_exist_for_both_adapters(self):
        adapters = {path.parts[-3] for path, _ in self.frontmatters()}
        self.assertEqual(adapters, {"claude", "codex"})

    def test_values_are_valid_yaml_scalars(self):
        for path, lines in self.frontmatters():
            for line in lines:
                key, value = line.split(": ", 1)
                with self.subTest(file=f"{path.parts[-3]}/{path.parts[-2]}/{path.name}", key=key):
                    if PLAIN_SAFE.fullmatch(value):
                        continue
                    self.assertTrue(value.startswith('"') and value.endswith('"'), value)
                    decoded = json.loads(value)
                    self.assertIsInstance(decoded, str)
                    self.assertTrue(decoded.strip())


if __name__ == "__main__":
    unittest.main()
