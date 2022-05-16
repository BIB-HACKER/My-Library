n = int(input("how many score"))
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[(arr.index(max(arr)))-1])
if n<2 or n>10:
    print("error")
else:
    li=[]
    for i in range(n):
        li.append(int(input("enter a score")))
    li.sort()
    pos=li.index(max(li))
    print("score of runner_up",li[pos-1])