from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "src" / "remoteops.py"


class RemoteOpsCliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(CLI), *args], text=True, capture_output=True, check=False)

    def test_example_manifest_validates(self) -> None:
        result = self.run_cli("validate", str(ROOT / "examples" / "desired-state.example.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["ok"])

    def test_init_creates_private_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "state"
            result = self.run_cli("init", "--path", str(target))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / ".git").is_dir())
            self.assertTrue((target / "desired-state.json").is_file())


if __name__ == "__main__":
    unittest.main()
