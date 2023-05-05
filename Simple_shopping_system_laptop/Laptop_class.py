import handle_file

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


class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def set_username(self, username):
        self.__username = username
    
    def set_password(self, password):
        self.__password = password
    @staticmethod
    def show_data():
        handle_file.show_data()


class Customer_login(Login):
    @staticmethod
    def get_bill(data):
        handle_file.create_bill_customer(data)
        print("Your bill have been succesfully made")

class Admin_login(Login):

    @staticmethod
    def add_new_items():
        handle_file.add_new_items()
        print("New product have been succesfully added")

login_list = []

login_list.append(Customer_login('kushal','1234'))
login_list.append(Customer_login('Bogati','123'))


a = input("Enter your name")
b = input("Enter your password")

for user in login_list:
    if user.get_username() == a and user.get_password() == b:
        print (f"Logged in as {a}")
        break
else:
    print("username or password mismatch")
