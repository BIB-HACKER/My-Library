term = 1
tom = 2
tan = 3
print("print tribonacii series :")
print(term,end="")
print(tom,end="")
print(tan,end="")
for frth in range(1,21):
    frth = term+tom+tan
    print(frth,end="")
    term=tom
    tom=tan
    tan=frth






# first = 0 
# second = 1
# print("all the fibonacci number between 0 and 100 are")
# print(first)
# print(second)
# while True:
#     third=first+second
#     if third>100:
#         break
#     print(third,end="")
#     first=second
#     second=third