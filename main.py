import os
from pathlib import Path

LINE = "Tell everyone I didn't die at 1%. I died at 0%, like a professional."
# Last words, sent at 0% battery and 100% confidence.

out = Path(os.environ.get("OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
target = out / "entry.txt"
target.write_text(LINE, encoding="utf-8")
os.chmod(target, 0o644)
