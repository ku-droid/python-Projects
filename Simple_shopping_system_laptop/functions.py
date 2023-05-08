import Laptop_class
import handle_file

customer_object_list = []
admin_object_list = []
laptop_object_list = []
laptop_list = []

def create_object_login_details():
    a = handle_file.return_from_login_details()
    for item in a:
        if item[0].strip().lower() == 'customer':
            customer_object_list.append(Laptop_class.Customer_login(item[1] , item[2]))
        elif item[0].strip().lower() == 'admin':
            admin_object_list.append(Laptop_class.Admin_login(item[1] ,item[2]))

def create_object_laptop_list():
    data = handle_file.create_object_list()
    for items in data:
        name = items[0]
        info = items[1]
        laptop_object_list.append(Laptop_class.Laptop_Details(name, info[0], info[1], info[2], info[3], info[4], info[5], info[6]))
    

def login():
    type = input("Enter 1 for admin login 2 for customer login")
    name = input("Enter your name")
    password = input("Enter your password")

    if type == '1':
        for items in admin_object_list:
            if name == items.get_username() and password == items.get_password():
                print(f"Logged in as {name}")
            else:
                print("Incorrect name or password")
    elif type == '2':
        for items in customer_object_list:
            if name == items.get_username() and password == items.get_password():
                print(f"Logged in as {name}")
                logged_in_operations_customer()
                break
            else:
                print("Incorrect name or password")
                break


def logged_in_operations_customer():
    print ("Please enter 1 to buy \n2 to recieve bill \n3 to logout\n")
    user_input = input()
    if user_input == '1':
        print ("Select the sn of the item you want to buy")
        handle_file.show_data()
        user_input = int(input("Enter the sn no of the items you want to buy\n"))
        input_quantity = int(input(f"Enter how many {laptop_object_list[user_input - 1 ].get_name()} you want to buy"))
        laptop_object_list[user_input - 1].sold_product(input_quantity)
    # if user_input == 2:


def logged_in_operations_admin():
    pass


def update_file_laptop_specs():
    list_laptop = []
    for items in laptop_object_list:
        list_laptop = [f'{items.get_name()} : {items.get_CPU()} , {items.get_GPU()} , {items.get_RAM()} , {items.get_storage()} , {items.get_display()} , {items.get_price()} , {items.get_quantity()}']
        laptop_list.append (list_laptop)
    handle_file.write_updated_list_laptop(laptop_list)




        


# create_object_login_details()
# create_object_laptop_list()

# login()
# update_file_laptop_specs()
# data = handle_file.create_object_list()


