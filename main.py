"""Write one joke about AI coding agents to /output/entry.txt.

Fixed string, standard library only: no clock, no randomness, no network,
no files outside the repository. Two runs write byte-identical output.
"""

import os

JOKE = "My coding agent's favorite debugging tool is me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
# No trailing newline: the gate counts a line end as a character, and the
# judge reads exactly the bytes written, so write nothing extra.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
