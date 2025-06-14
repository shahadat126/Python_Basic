class Grandparent:
    def property(self):
        print("Land")

class Parent(Grandparent):
    def house(self):
        print("House")

class Child(Parent):
    def bike(self):
        print("Bike")

c = Child()
c.property()
c.house()
c.bike()
