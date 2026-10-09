class Laptop:
    def __init__(self,brand,ram,storage,price):
        self.brand=brand
        self.ram=ram
        self.storage=storage
        self.price=price

    def display_info(self):
        return f"Brand: {self.brand}\nRam: {self.ram} GB \nStorage: {self.storage} \nPrice:{self.price}"
    
    def get_category(self):
        if self.price < 500:
            return "Category: Budget"
        
        if self.price >= 500 and self.price < 1000:
            return "Category: Mid-Range"
        
        if self.price > 1000:
            return "Category: Premium"
        
    def apply_discount(self,percent):
        self.price=self.price - (self.price * (percent/100))
    
    
laptop1 = Laptop("Dell", 8, 256, 450)
laptop2 = Laptop("HP", 16, 512, 850)
laptop3 = Laptop("Apple", 16, 512, 1400)

print("Laptop Information")
print("------------------")
print(laptop1.display_info())
print(laptop1.get_category())
print("")
print(laptop2.display_info())
print(laptop2.get_category())
print("")
print(laptop3.display_info())
print(laptop3.get_category())
print("")

discount_precent=int(input("Please enter the discount for the laptop in percentage: "))

print("")

print("After Discount")
print("--------------")
laptop3.apply_discount(discount_precent)
print(laptop3.display_info())
print(laptop3.get_category())