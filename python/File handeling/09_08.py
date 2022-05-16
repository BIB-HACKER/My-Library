with open("File IO/sample.txt") as f:
    content = f.read()

content = content.replace("donkey","@#$%^&&*")

with open("File IO/sample.txt", "w") as f:
     f.write(content)