class login:

    def __init__(self,loginid,pwd): # Constructor
        self.loginid=loginid # self.id is the instance variables
        self.pwd=pwd  # self is the object reference whoo is calling the function


    def get_loginid(self):
        return self.loginid

    def get_pwd(self):
        return self.pwd
