#classname.__init(self)
# class Vehicle:
#     def __init__(self,type):
#         self.type = type
        
#     def get_type(self):
#         print(f"{self.type}")
        
# class Brand:
#     def __init__(self,brand_name):
#         self.brand_name= brand_name
#     def get_brand(self):
#         print(f"{self.brand_name}")
        
# class Car(Vehicle,Brand):
#     def __init__(self, type,brand_name):
#         Vehicle.__init__(self,type)
#         Brand.__init__(self,brand_name)
        
#     def show_car_info(self):
#         self.get_type()
#         self.get_brand()
        
# car = Car("Toyota","sujuki")
# car.show_car_info()

#super().__init__(**kwargs) where **kwargs take all the arguments and passes it into next class as order of MRO
class Vehicle:
    def __init__(self, type, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        
    def get_type(self):
        print(f"{self.type}")
        
class Brand:
    def __init__(self, brand_name, **kwargs):
        super().__init__(**kwargs)
        self.brand_name = brand_name
        
    def get_brand(self):
        print(f"{self.brand_name}")
        
class Car(Vehicle, Brand):
    def __init__(self, type, brand_name):
        super().__init__(type=type, brand_name=brand_name)
        
    def show_car_info(self):
        self.get_type()
        self.get_brand()
        
car = Car("Toyota", "sujuki")
car.show_car_info()

