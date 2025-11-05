
class NormalPrice:
    def calculate(self, price):
        return price

class DiscountPrice:
    def calculate(self, price):
        return price * 0.9  

class SalePrice:
    def calculate(self, price):
        return price * 0.7
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.strategy = NormalPrice() 
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def get_final_price(self):
        return self.strategy.calculate(self.price)

phone = Product("iPhone", 1000)

print("Normal price:", phone.get_final_price()) 

phone.set_strategy(DiscountPrice())
print("Discount price:", phone.get_final_price())    

phone.set_strategy(SalePrice())
print("Sale price:", phone.get_final_price())    