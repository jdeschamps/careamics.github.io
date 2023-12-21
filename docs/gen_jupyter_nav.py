"""Generate navigation items for the jupyter notebooks."""
from pathlib import Path

def index_text():
    return "---\n" \
            "icon: octicons/file-media-24\n" \
            "description: Applications\n" \
            "---\n" \
            "# Applications\n\n"

# source folder
SRC = Path("applications")
INDEX = SRC / "index.md"

# iterate over notebooks
notebooks_list = []
for path in sorted(SRC.rglob("*.ipynb")):
    # get parent folder name
    parent = path.parent.name