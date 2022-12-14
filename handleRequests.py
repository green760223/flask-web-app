import os

path = "/templates/index.html"
start = "/templates"
index_path = os.path.relpath(path=path, start=start)