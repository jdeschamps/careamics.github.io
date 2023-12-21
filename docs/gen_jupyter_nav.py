"""Generate navigation items for the jupyter notebooks."""
from pathlib import Path

import mkdocs_gen_files

def index_text():
    return "---\n" \
            "icon: octicons/file-media-24\n" \
            "description: Applications\n" \
            "---\n" \
            "# Applications\n\n" \
            "Use the navigation index on the left to explore the applications."


# source folder
SRC = Path("applications")
INDEX = SRC / "index.md"

# create mkdocs navigation
nav = mkdocs_gen_files.Nav()

# create index file
with mkdocs_gen_files.open(INDEX, "w") as index_md:
    index_md.write(index_text())

# loop over all notebooks recursively 
for path in SRC.rglob("*.ipynb"):
    print(path)

    # relatve path to applications
    rel_path = path.relative_to(SRC).with_suffix("")
    file_path = path.relative_to(SRC).with_suffix(".ipynb")

    # parts
    parts = tuple(rel_path.parts)

    # add to navigation
    nav[parts] = file_path.as_posix()