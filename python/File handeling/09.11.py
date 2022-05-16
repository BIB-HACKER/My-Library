#one file content transfer to other file and delete first file.

import os

oldname = "File IO/sample2.txt"
newname = "File IO/rename_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)