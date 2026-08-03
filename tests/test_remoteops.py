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

    def test_linux_example_manifest_validates(self) -> None:
        result = self.run_cli("validate", str(ROOT / "examples" / "desired-state.example.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["platform"], "linux")

    def test_windows_example_manifest_validates(self) -> None:
        result = self.run_cli("validate", str(ROOT / "examples" / "desired-state.windows.example.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["platform"], "windows")

    def test_init_creates_private_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "state"
            result = self.run_cli("init", "--path", str(target))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / ".git").is_dir())
            self.assertTrue((target / "desired-state.json").is_file())

    def test_invalid_platform_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "invalid.json"
            manifest.write_text(
                json.dumps(
                    {
                        "schemaVersion": "1.0",
                        "device": {"id": "example-device", "platform": "unsupported"},
                        "policies": {"approval": "risk-based", "rollback": "required"},
                    }
                ),
                encoding="utf-8",
            )
            result = self.run_cli("validate", str(manifest))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("windows, linux or macos", result.stderr)


if __name__ == "__main__":
    unittest.main()
