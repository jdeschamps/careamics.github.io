"""Generate the code reference pages and navigation.

see: https://mkdocstrings.github.io/recipes/
"""

from pathlib import Path

import mkdocs_gen_files

def sub_index_text(module_name):
    return f"# {module_name} \n" \
              f"Use the navigation index on the left to explore the documentation" \


index_text = "# Code Reference \n" \
             "In this page, you will find all the code documentation for " \
             "the various repositories in this suite: \n\n"


# create mkdocs navigation
nav = mkdocs_gen_files.Nav()

# add index page to the navigation
modules_index = Path("index.md")
nav[tuple(modules_index.parts)] = modules_index.as_posix()

# iterate over modules
module_list = []
for path in sorted(Path("src").iterdir()):

    # if it is a python module
    if Path(path, "__init__.py").exists():
        # add to list
        module_list.append(path.name)

        # set up path to its own module index
        module_path = Path(path.name, "index.md")

        # add to navigation
        nav[tuple(module_path.parts)] = module_path.as_posix()


        # create module index
        with mkdocs_gen_files.open(Path("reference", module_path), "w") as fd:
            fd.write(sub_index_text(path.name))

# add modules to index
with mkdocs_gen_files.open(Path("reference", modules_index), "w") as fd:
    fd.write(index_text)

    for name in module_list:
        fd.write(f"- [{name}]({name})\n")

# build docstring references
for path in sorted(Path("src").rglob("*.py")):
    if path.name != "__init__.py":
        # set up paths
        module_path = path.relative_to("src").with_suffix("")
        doc_path = path.relative_to("src").with_suffix(".md")
        full_doc_path = Path("reference", doc_path)

        parts = tuple(module_path.parts)

        if parts[-1] == "__init__":
            parts = parts[:-1]
        elif parts[-1] == "__main__":
            continue

        # progressively build the navigation index
        nav[parts] = doc_path.as_posix()

        # add doc to mkdocs
        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.write(f"::: {ident}")

        # set the edit_uri on the pages
        mkdocs_gen_files.set_edit_path(full_doc_path, path)

# Write the navigation as a Markdown list in the literate navigation file
with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
