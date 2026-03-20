from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "scripts" / "harvest.py"

sys.path.insert(0, str(ROOT))
runpy.run_path(str(SCRIPT), run_name="__main__")
