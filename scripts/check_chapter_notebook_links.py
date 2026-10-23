"""Check the Part 1 to Part 3 notebook links and consistent chapter exercises."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/"src/content"
chapters=list(root.glob("chapter_*/chapter-*.md"))
required={2,3,4,5,6,7}
seen=set()
for p in chapters:
    match=re.search(r"chapter_(\d+)",str(p))
    if not match:continue
    n=int(match.group(1))
    if n not in required:continue
    text=p.read_text(encoding="utf-8")
    assert "## Try it yourself" in text, f"Missing activity section: {p}"
    targets=re.findall(r"\]\((\.\./notebooks/[^)#?]+\.ipynb)\)",text)
    assert targets, f"No linked notebooks in {p}"
    for rel in targets:
        dest=(p.parent/rel).resolve()
        assert dest.is_file(), f"Broken notebook link from {p}: {rel}"
        seen.add(str(dest))
    print(f"PASS Chapter {n}: {len(targets)} linked notebook(s)")
assert len(seen)>=12, f"Unexpectedly few unique notebook targets: {len(seen)}"
