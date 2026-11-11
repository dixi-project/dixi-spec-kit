from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/i18n-site"


class I18nSiteNext16ProxyTests(unittest.TestCase):
    """Next.js 16 renames the `middleware` file convention to `proxy`."""

    def test_proxy_file_replaces_middleware(self):
        self.assertTrue((EXAMPLE / "proxy.ts").is_file(), "examples/i18n-site/proxy.ts is missing")
        self.assertFalse((EXAMPLE / "middleware.ts").exists(), "middleware.ts is deprecated in Next.js 16")

    def test_proxy_exports_proxy_function_and_keeps_matcher(self):
        source = (EXAMPLE / "proxy.ts").read_text(encoding="utf-8")
        self.assertRegex(source, r"(?m)^export function proxy\(")
        self.assertNotRegex(source, r"\bfunction middleware\b")
        self.assertRegex(source, r"(?m)^export const config = \{")
        self.assertIn("matcher:", source)
        self.assertIsNone(re.search(r"\bruntime\s*:", source), "proxy does not accept a runtime option")


if __name__ == "__main__":
    unittest.main()
