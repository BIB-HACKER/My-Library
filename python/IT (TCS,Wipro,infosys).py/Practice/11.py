# factorial and fibonacci using RECURTION

def factoral(num):
    if num==0 or num==1:
        return 1
    return num * factoral(num-1)

def fibonacci(num):
    if num==0 or num==1:
        print(num)
        return num
    
    return fibonacci(num-1) + fibonacci(num-2)


# fact=1
num=4
# for i in range(1,num+1):
#     fact*=i
# print(fact)
print(factoral(num))
print(fibonacci(num))