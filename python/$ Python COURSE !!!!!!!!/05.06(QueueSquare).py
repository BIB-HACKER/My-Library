def insertion(num):
    global queue
    queue.append(num)
def deletion():
    global queue
    if queue==[]:
        val=-999
    else:
        val=queue.pop(0)
    return val
#main
queue=[]
list=eval(input("enter few numbers in a list"))
for val in list:
    insertion(val*val)
print("Queue is= ")
while True:
    item=deletion()
    if item==-999:
        break
    else:
        print(item)