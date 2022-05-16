with open("File IO/log.txt") as f:
    content = f.read().lower()

if 'python' in content:
    print("yes python is presnt")
else:
    print("no python is not present")
