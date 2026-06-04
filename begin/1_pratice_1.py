class Laptop:
    def __init__(self, brand : str , ram : str) :
        self.brand = brand
        self.ram = ram

    def show(self):
        print(f"Company: {self.brand} , RAAM {self.ram}")


class Student:
    def __init__(self, name , roll_num , laptop) -> None:
        self.name = name
        self.roll_num = roll_num
        self.laptop = laptop    

# lapt1 = Laptop("HP", "4GB")
# student1 = Student("Zain", "FA-24", lapt1)
# print(student1.laptop.show())

class Product:
    def __init__(self , item_name , price) -> None:
        self.item_name = item_name  
        self.price = price

class Cart:
    def __init__(self, p1,p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def total(self):
        print(f"Total bill is {self.p1 + self.p2} . ")

pr1 = 200
pr2 = 400
my_cart = Cart(pr1, pr2)
print(my_cart.total())