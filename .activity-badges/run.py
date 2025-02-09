import re
from pathlib import Path
import subprocess

subprocess.run("sh ./.activity-badges/run.sh", shell=True)
with open(".activity-badges/README_TABLE.md") as f:
    lines = []
    for line in f:
        match = re.search(r"github\.com\/(.+?)\)", line)
        if match:
            line = f"|![GitHub last commit](https://img.shields.io/github/last-commit/{match.group(1)})" + line
            #line = f"|![GitHub last commit](https://badgen.net/github/last-commit/{match.group(1)})" + line
            line = f"|![GitHub last commit](https://img.shields.io/github/commit-activity/y/{match.group(1)})" + line
        elif line.startswith("|-"):
            line = "|-|-" + line
        elif line.startswith("| | |"):
            line = "|activity|last commit|package|explanation|\n"
        elif line.startswith("|"):
            line = "||" + line
        lines.append(line)
    Path("README_WITH_ACTIVITY_BADGES.md").write_text("".join(lines))
