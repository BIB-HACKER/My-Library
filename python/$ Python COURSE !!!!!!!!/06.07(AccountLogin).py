from Library import login

user=login.Login()
# print(user.get_loginid())
# print(user.get_pwd())
# print(userid)
# print(password)

# userid=input("Enter Your Login id ->")
# password=input("Enter your Password ->")
# if user.get_loginid() and user.get_pwd() == userid and password:
#     print("Login Successfull")

while True:

    userid=input("Enter Your Login id ->")
    if user.get_loginid() == userid:
        print("Next")
    else:
        print("Invlaid login id!!")
        continue
        
    password=input("Enter your Password ->")
    if user.get_pwd() == password:
        print("Login Successfull")
        break
    else:
        print("Invalid Password!!!!")
        print()
        print("Please Try Again")

    


    
