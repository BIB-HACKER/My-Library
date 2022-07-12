def push(key):
    global PRODPUSH
    PRODPUSH.append(key)
    # print(PRODPUSH)

#main
PRODPUSH=[]
product=eval(input("create a product & price dictionary-> "))

for key in product:
    if product[key]<6000:
        push(key)
item=[]
for i in range(len(PRODPUSH)):
    P=PRODPUSH.pop()
    item.append(P)

print(item)

# {"TV":10000,"MOBILE":4500,"PC":12500,"FURNITURE":5500}
