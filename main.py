"""One-line pitch for make.fun's 'A Day of One-Line Pitches'."""

import os
from pathlib import Path

PITCH = "You keep saying someone should build that app — why not you: say your idea in plain words on make.fun, let an AI agent build a first version you can try and tweak, and if you hate it, all you lost is a few minutes."


def main() -> None:
    print(PITCH)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        Path(output_dir, "entry.txt").write_text(PITCH, encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
