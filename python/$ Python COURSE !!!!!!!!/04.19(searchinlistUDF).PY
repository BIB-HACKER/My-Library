def search(list,value):
    if value in list:
        print("Found")
    else:
        print("Not found ")

list=eval(input("create a list"))
value=int(input("enter a number"))
search(list,value)