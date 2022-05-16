from cgi import print_arguments


emailid=input("Enter your email id ->")
index=emailid.find("@")
if index==-1:
    print("Invalid Email id")
else:
    username=emailid[0:index]
    domain=emailid[index+1:]
    print("User name =",username)
    print("Domain name =",domain)
