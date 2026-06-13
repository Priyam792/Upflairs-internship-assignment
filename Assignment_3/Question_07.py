#Create a class named Animal with a method sound().             
#Create a child class Dog that overrides the sound() method and prints "Bark"

class Animal:
    def sound(self):
        print("Making sound")

class Dog(Animal):
    def sound(self):
        print("Bark")


d = Dog()
d.sound()