class Login:

    def __init__(self):
        self.loginid='bibHACKER'
        self.pwd='098765'

    def get_loginid(self):
        return self.loginid

    def get_pwd(self):
        return self.pwd

    def set_loginid(self):
        return self.loginid

    def set_pwd(self):
        return self.pwd
# class Login:
#     def _init_(self): # Constractor
#         self.loginid="malay"  # Self.id is the instance variable
#         self.pwd=1234         # self it is the object reference who is calling the function
        
#     def get_loginid(self):
#         return self.loginid    
#     def get_pwd(self):
#         return self.pwd    
#     def set_loginid(self,loginid):
#         self.loginid=loginid       
#     def set_pwd(self,pwd):
#         self.pwd=pwd
# log=Login()     
# print(log.get_loginid())