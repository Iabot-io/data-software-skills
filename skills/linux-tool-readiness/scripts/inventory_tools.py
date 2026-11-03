"""Read-only inventory of tools available to the current Linux process."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import platform
from pathlib import Path
import shutil
import subprocess


TOOLS = {
    "python3": ["--version"],
    "libreoffice": ["--version"],
    "blender": ["--version"],
    "FreeCADCmd": ["--version"],
    "ffmpeg": ["-version"],
    "ffprobe": ["-version"],
    "tesseract": ["--version"],
    "ocrmypdf": ["--version"],
    "pandoc": ["--version"],
    "gdalinfo": ["--version"],
    "node": ["--version"],
    "hyperframes": ["--version"],
}


def inspect_tool(item):
    name, arguments = item
    executable = shutil.which(name)
    result = {"tool": name, "on_path": executable is not None, "path": executable,
              "version_checked": False, "functional_workflow_verified": False}
    if not executable:
        result["note"] = "Not found on PATH; it may exist elsewhere in the environment"
        return result
    try:
        run = subprocess.run([executable, *arguments], stdin=subprocess.DEVNULL,
                             capture_output=True, text=True, timeout=5)
        lines = (run.stdout or run.stderr).splitlines()
        result.update({"exit_code": run.returncode, "version_checked": run.returncode == 0,
                       "version_output": lines[0][:300] if lines else ""})
    except subprocess.TimeoutExpired:
        result["note"] = "Version check exceeded five seconds"
    except OSError as error:
        result["note"] = f"Could not execute version check: {type(error).__name__}"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--label", default="current process environment")
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=4) as executor:
        tools = list(executor.map(inspect_tool, TOOLS.items()))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(),
              "environment_label": args.label, "operating_system": platform.system(),
              "architecture": platform.machine(), "tools": tools,
              "limits": "Checks PATH and version commands only; does not install, inspect secrets or certify workflows. The caller must verify this is the requested workstation."}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
