import json
from pathlib import Path
import sys
import unittest

import test_workflows as helpers


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dixi_spec_kit.filesystem import Issue
from dixi_spec_kit.workflows import load_recipes, prepare_packet


class WorkflowEdgeTests(unittest.TestCase):
    def setUp(self):
        self.case = helpers.WorkflowTests()
        self.case.setUp()
        self.addCleanup(self.case.doCleanups)
        self.case.init()

    def test_target_excludes_unknown_fields(self):
        graph = self.case.graph()
        target = next(item for item in graph["items"] if item["id"] == "FEATURE-001")
        target["body"] = "PRIVATE-CONTENT-MARKER"
        target["unexpected"] = "\ud800"
        self.case.set_graph(graph)
        packet = self.case.packet(self.case.prepare())
        self.assertEqual(set(packet["target"]), {"id", "kind", "path", "parents"})
        self.assertNotIn("PRIVATE-CONTENT-MARKER", json.dumps(packet))

    def test_surrogate_request_rejected_before_filesystem(self):
        recipe = load_recipes("es")["plan"]
        with self.assertRaises(Issue) as context:
            prepare_packet(self.case.base / "absent", recipe, "FEATURE-001", "bad\ud800")
        self.assertEqual(context.exception.code, 2)

    def test_shared_ancestor_is_emitted_once(self):
        graph = self.case.graph()
        module = next(item for item in graph["items"] if item["kind"] == "module")
        graph["items"].append({"id": "DOMAIN-002", "kind": "domain", "path": "03-domains/second.md",
                               "parents": ["GOAL-001"]})
        module["parents"].append("DOMAIN-002")
        (self.case.project / "03-domains/second.md").write_text("# Second domain\n")
        self.case.set_graph(graph)
        packet = self.case.packet(self.case.prepare())
        paths = [source["path"] for source in packet["sources"]]
        self.assertEqual(paths.count("01-business/vision.md"), 1)
        self.assertIn("03-domains/second.md", paths)
