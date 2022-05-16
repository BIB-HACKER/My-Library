with open("File IO/this.txt") as f:
    content = f.read()

with open("File IO/copy.txr", 'w') as f:
    f.write(content)