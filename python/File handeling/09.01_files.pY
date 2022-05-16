# use open function to read the contant of a file

# f = open('sample.txt','r')
f = open("ss.txt") # by default the mode is r
data = f.read()
print(data)
f.close()