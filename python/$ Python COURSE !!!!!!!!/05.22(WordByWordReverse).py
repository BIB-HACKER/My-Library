line='''Python is a high-level, interpreted, general-purpose programming language. Being a general-purpose language, it can be used to build almost any type of application with the right tools/libraries. Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management which help in modeling real-world problems and building applications to solve these problems.'''
#accessing each letter/character of the list in a loop
#word by word access
words=line.split()
print(words)
print("|word|  |reverse|")
reverse=""

for word in words:
    print(word)
    List=list(word)
    List.reverse()  #Reverse function work on only LIST datatype
######
# for word in words:
#     List=word[len(word)-1::-1]
######
# for word in words:
#     print(word,'#######')
#     List=""
#     for j in range(0,len(word)):
#         List=word[j]+List

    for ch in List:
        reverse+=ch
    print(word,"    ",reverse)
    reverse="" #reset reverse