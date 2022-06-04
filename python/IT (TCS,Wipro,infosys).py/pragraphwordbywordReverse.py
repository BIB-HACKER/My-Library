#LETS PLAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# line='''Python was developed by Guido van Rossum and was released first on February 20,1991!! It is one of the most widely-used and loved programming languages and is interpreted in nature thereby providing flexibility of incorporating dynamic semantics. It is also a free and open-source language with very simple and clean syntax. This makes it developers easy to learn python. Python also supports objectoriented programming and is most commonly used to perform general-purpose programming? Due to its simplistic nature and the ability to achieve multiple functionalities in fewer lines of code, python’s popularity is growing tremendously.Python is also used in Machine Learning Artificial Intelligence? Web Development? Web Scraping? and various other domains due to its ability to support powerful computations using powerful libraries. Due to this, there is a huge demand for python developers in India and across the world!!'''

# paragraph=line.split()
# print(paragraph)

# # paragraph=line.split('.')
# # paragraph1=line.split('?')
# # paragraph2=line.split('!!')
# # golpo=paragraph+paragraph1+paragraph2
# # # print(golpo)
# sentnce=""
# s=""
# p=""
# o=""
# b=" "
# for i in paragraph:
    
#     # if i.endswith("!!"):
#     #   s+=i[len(i)-3::-1]
#     #   p+=i[len(i)-2]
#     #   o+=i[len(i)-1]
#     #   b+=s+p+o+" "
#     #   sentnce+=b
#     #   b=" "
#     # elif i.endswith("."):
#     #    s+=i[len(i)-2::-1] 
#     #    p+=i[len(i)-1]
#     #    b+=s+p+" "
#     #    sentnce+=b
#     #    b=""
#     # elif i.endswith("?"):
#     #    s+=i[len(i)-2::-1] 
#     #    p+=i[len(i)-1]
#     #    b+=s+p+" "
#     #    sentnce+=b
#     #    b=""
#     # else:
#         sentnce+=i[len(i)-1::-1]+" "
# print(sentnce)

# # s=p=o=""
# # # l='20,1991!!'
# # # s+=l[len(l)-3::-1]
# # # p+=l[len(l)-2]
# # # o+=l[len(l)-1]
# # # u=s+p+o
# # # print(u)
# # g='syntax.'
# # s=g[len(g)-2::-1]
# # p=g[len(g)-1]
# # u=s+p
# # print(u)


##############################################################



line='''Python was developed by Guido van Rossum and was released first on February 20,1991!! It is one of the most widely-used and loved programming languages and is interpreted in nature thereby providing flexibility of incorporating dynamic semantics. It is also a free and open-source language with very simple and clean syntax. This makes it developers easy to learn python. Python also supports objectoriented programming and is most commonly used to perform general-purpose programming? Due to its simplistic nature and the ability to achieve multiple functionalities in fewer lines of code, python’s popularity is growing tremendously.Python is also used in Machine Learning Artificial Intelligence? Web Development? Web Scraping? and various other domains due to its ability to support powerful computations using powerful libraries. Due to this, there is a huge demand for python developers in India and across the world!!'''

# List=[]
# def adding(line):
#     global List
#     golpo=[]
#     golpo.append(line)
#     last=""
    
#     for i in golpo:
#         last=i[len(i)-1::-1]+" "
#     List.append(last[0:len(last)-1]+'.'+" ")
#     return List

paragraph1=line.split('?' )
# for i in paragraph1:
#     for j in i:
#         List.append(i)
# print(List)
# print(line)
paragraph2=[]
for i in paragraph1:
    paragraph2.append(i.split('.'))
# print(paragraph2)
paragraph3=[]
for i in paragraph2:
    for j in i:
        paragraph3.append(j.split("!!"))
# print(paragraph3)

result=[]
for i in paragraph3:
    for j in i:
        result.append(j.split())
# print(result)

List=[]
for i in result:
    for j in i:
        List.append(j.split())
# print(List)
last=""
for i in List:
    for word in i:
        last+=word[len(word)-1::-1]+" "
print(last)
    
###################################################################

# paragraph='''Reindexing is the process of conforming a dataframe to a new index with optional filling logic. If the values are missing in the previous index, then NaN/NA is placed in the location. A new object is returned unless a new index is produced that is equivalent to the current one. The copy value is set to False. This is also used for changing the index of rows and columns in the dataframe.'''

# lines=paragraph.split('.')
# # print(lines)
# sentence=[]
# golpo=[]

# for line in lines:
#     sentence.append(line.split())
# # print(sentence)
# for j in sentence:
#     # print(j)
#     last=""
#     for i in j:
#         # print(i) #########
#         last+=i[len(i)-1::-1]+" "
#     golpo.append(last[0:len(last)-1]+'.'+" ")
# # print(golpo)
# paragraph=""
# for line in golpo:
#     if line==". ":
#         continue
#     else:
#         paragraph+=line
# print()
# print("OUTPUT:-")
# print(paragraph)






    
