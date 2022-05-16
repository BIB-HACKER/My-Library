#class attribute
class Employee:
    company = "google"
    salary =500000

bibhakar = Employee()
malay = Employee()

print(bibhakar.salary)
print(malay.salary)

# instance attribute
malay.salary=100

print(bibhakar.company)
print(malay.company)
print(malay.salary)
print(bibhakar.salary)
print(malay.address)#no attribute object and ERROR output