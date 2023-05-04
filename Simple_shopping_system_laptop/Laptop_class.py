# data = []
class Laptop_Details:
    def __init__(self, name, CPU, GPU, RAM, storage, display, price, quantity):
        self.__name = name
        self.__CPU = CPU
        self.__GPU = GPU
        self.__RAM = RAM
        self.__storage = storage
        self.__display = display
        self.__price = price
        self.__quantity = quantity 
    
    def get_name(self):
        return self.__name
    
    def get_CPU(self):
        return self.__CPU
    
    def get_GPU(self):
        return self.__GPU
    
    def get_RAM(self):
        return self.__RAM
    
    def get_storage(self):
        return self.__storage
    
    def get_display(self):
        return self.__display
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def add_stock (self):
        self.__quantity += 1
    
    def sold_product (self):
        self.__quantity -= 1
    
    def set_quantity(self, qty):
        self.__quantity = qty


