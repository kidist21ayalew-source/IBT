# Qation No1
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def describe(self):
        print(f"Title: {self.title} | Author: {self.author} | Pages: {self.pages}")

#create object's
book_one = Book("fikr","addis",250)

book_one.describe()

 # quation No2

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    

    def restock(self,n):
        self.quantity += n
        print(f"stock quantity is {self.quantity}")

    def sell(self,n):
        self.quantity -= n
        print(f"sell quantity is {self.quantity}")

## test task 2
product_one = Product("rice",100,10)

product_one.restock(200)
product_one.sell(150)


# quation No 3


class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity #private
    
    @property   #getter  quantity
    def aaa(self):
        print(self.__quantity)

    def restock(self,n):
        self.__quantity += n
        print(f"stock quantity is {self.__quantity}")

    def sell(self,n):
        self.__quantity -= n
        print(f"sell quantity is {self.__quantity}")


# # test task 2
product_one = Product("rice",100,10)

product_one.restock(200)
product_one.sell(150)

product_one.aaa

# Qation No 4

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity #private
    
    @property   #getter  quantity
    def quantity(self):
        return (self.__quantity)

    @quantity.setter
    def quantity(self, n):
        if n < 0:
            print("Can not Set Quantity")
        else:
            self.__quantity = n

    def restock(self,n):
        self.__quantity += n
        print(f"stock quantity is {self.__quantity}")

    def sell(self,n):
        if n > self.__quantity:
            print("inseficetn Quantityt")
        else:
            self.__quantity -= n
            return (f"sell quantity is {self.__quantity}")

#quation No 5


product_one = Product("phone",10000,14)
product_two = Product("Laptop", 15000,20)
product_three = Product("Tv", 20000, 18)

print("Before Change:")

print(f"{product_one.name} : {product_one.quantity}")
print(f"{product_two.name} : {product_two.quantity}")
print(f"{product_three.name} : {product_three.quantity}")

product_three.sell(5)
print("After Change")


print(f"{product_one.name} : {product_one.quantity}")
print(f"{product_two.name} : {product_two.quantity}")
print(f"{product_three.name} : {product_three.quantity}")