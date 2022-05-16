class Employee:
    company = "google"
    def getsalary(self):
    # def getsalary(): #error
        # print("salary is 500k")
        print(f"salary for this employee working in {self.company} is {self.salary}")

bibhakar = Employee()
bibhakar.salary = 1000000
# bibhakar.getsalary()
Employee.getsalary(bibhakar) #10 or 11 line are same