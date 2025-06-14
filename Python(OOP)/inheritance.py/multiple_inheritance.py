class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):  # Multiple inheritance
    pass

c = Child()
c.skill()
c.talent()
