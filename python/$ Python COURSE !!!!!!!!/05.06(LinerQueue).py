#menu driven approch to insert and delete element from liner queue
queue=[]
front=None
rear=None
def isEmpty(queue):
    if queue==[]:
        return True
    else:
        return False

def insertion(item):
    global queue
    global rear,front
    queue.append(item)
    if len(queue)==1:
        rear=front=0
    else:
        rear=len(queue)-1

def deletion(queue):
    global rear,front
    if isEmpty(queue):
        print("underflow")
    else:
        item=queue.pop(0)
        print("deleted item is =",item)
        if len(queue)==0:
            front=rear=None
        else:
            rear=rear-1

def display(queue):
    global rear,front
    if isEmpty(queue):
        print("queue is empty")
    else:
        print("queue is =")
        for i in range(front,rear+1):
            print(queue[i])

def peek(queue):
    global front
    if isEmpty(queue):
        print("queue is empty")
    else:
        print("element at front end =",queue[front])

def down(queue):
    global rear
    if isEmpty(queue):
        print("queue is empty")
    else:
        print("element at front end =",queue[rear])

#main
while True:
    print("menu:~\n 1. Insertion\n 2. Deletion\n 3. Get the 1st item\n 4. Get the last item\n 5. Display the queue content\n 6. Exit")
    choice = int(input("enter a number to insert ->"))
    if choice==1:
        item=int(input("enter a number to insert ->"))
        insertion(item)
    elif choice==2:
        deletion(queue)
    elif choice==3:
        peek(queue)
    elif choice==4:
        down(queue)
    elif choice==5:
        display(queue)
    else:
        break
