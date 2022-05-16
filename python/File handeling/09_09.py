words = ["donkey", "kutta", "mote", "bal", "bc", "sala"]

with open("File IO/sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"@#$%^&&*")

    with open("File IO/sample.txt", "w") as f:
        f.write(content)