
class Product:
# Constructor (used to initialize object values)
    def __init__(self, name, price, quantity):
        self.name = name          
        self.price = price        
        self.quantity = quantity  # Instance variable
        print(f"{self.name} object created..")
# Member function (method)
    def display_product(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
    def total_value(self):
        return self.price * self.quantity
# Creating objects
product1 = Product("Pen", 10, 5)
product2 = Product("Notebook", 50, 3)
product3 = Product("pencil", 5, 13)

product1.display_product()
product2.display_product()
print(product1.name)

print("total value of product1",product1.total_value())