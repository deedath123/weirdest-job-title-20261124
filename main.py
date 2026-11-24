"""Weirdest Job Title entry — writes the locked entry line to entry.txt.

Entry: "Chief Apology Officer, Self-Driving Cars" (40 chars, 40 bytes).

Verified 2026-11-24: entry length 40 chars / 40 bytes, no trailing newline,
sha256 ed98c22792df489da37b3062193824878250d053cf46e5fc083ebedcbdb2b196.
3 fresh-dir runs + 1 clean-env (env -i python3 -P -s) run, all byte-identical;
re-verified after this docstring edit with 2 fresh-dir runs + 1 clean-env run,
all byte-identical.
"""
import os

ENTRY = "Chief Apology Officer, Self-Driving Cars"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
