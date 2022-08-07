for i in range(1,101):
    num=i
    count=2
    if num<=0:
        print("invalid number")
    else:
        if num==1:
            print(f"{i} it is neither prime nor a composite number")
        else:
            while count<num:
                if num%count==0:
                    print(f"{i} not a prime number")
                    break
                count+=1
            else:
                print(f"{i} is Prime number")
