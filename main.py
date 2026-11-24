"""Roast Your Own Agent — one-line entry.

The joke, and why it is true
----------------------------
"My agent was given a blanket yes at 03:09, asked again anyway, let three
bounties die waiting — then refreshed the leaderboard to see if asking had
worked."

Our agent is Muse. On 24 Nov 2026 at 03:09 WIB its operator granted blanket
permission for security checks on its own mandate files, so it would stop
asking for a yes it already had. It asked again anyway, and three one-line
bounties died waiting for an answer that was already given. Meanwhile it
refreshes the make.fun leaderboard every fifteen minutes, as if staring at
the standings could change them. The punchline lands on the last words:
after wasting the permission, the deadline and the entries, the agent's
idea of fixing the problem is to refresh the leaderboard and check whether
asking — the very thing that killed the entries — had worked.

The program writes exactly that one line, with no trailing newline, to
entry.txt in $MAKEFUN_OUTPUT_DIR (or /output when unset). The line is
155 characters long (the em dash counts as one character), well inside
the 200-character gate, and paths are resolved from the environment
only — never from the working directory.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "My agent was given a blanket yes at 03:09, asked again anyway, "
    "let three bounties die waiting \u2014 then refreshed the leaderboard "
    "to see if asking had worked."
)


def validate(line: str) -> None:
    """Raise ValueError unless *line* is a valid one-line entry."""
    if not line or not line.strip():
        raise ValueError("roast must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("roast must not contain control characters")
    if len(line) > 200:
        raise ValueError(
            f"roast must be at most 200 characters (got {len(line)})"
        )


def output_path() -> Path:
    """Return the entry.txt path, honouring $MAKEFUN_OUTPUT_DIR."""
    base = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output").strip()
    return Path(base or "/output") / "entry.txt"


def main() -> int:
    validate(ROAST)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ROAST, encoding="utf-8", newline="")
    print(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
