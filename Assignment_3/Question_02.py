# Create a class named Car with attributes: 
# o brand  
# o model  
# o price               
# Create two objects and display their details

#Solution -->

class Car :
    brand = "Audi"
    model = "Q3"
    price = 4300000

c = Car()

print(f"Using first object : \n{c.brand}\n{c.model}\n{c.price}")
c1 = Car()
print(f"Using second object : \n{c1.brand}\n{c1.model}\n{c1.price}")