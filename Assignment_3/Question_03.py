# Create a class named Employee and use a constructor (__init__) to initialize: 
# o employee_id  
# o name  
# o salary              
# Print the employee details

#Solution -->

class Employee :
    def __init__(self):
        self.employee_id = "24EBKAI046"
        self.name = "Priyam"
        self.salary = 120000

e = Employee()
print(e.employee_id)
print(e.name)
print(e.salary)