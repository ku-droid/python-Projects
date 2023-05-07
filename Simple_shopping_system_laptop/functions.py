import Laptop_class
import handle_file

customer_object_list = []
admin_object_list = []

def create_object_login_details():
    a = handle_file.return_from_login_details()
    for item in a:
        if item[0].strip().lower() == 'customer':
            customer_object_list.append(Laptop_class.Customer_login(item[1] , item[2]))
        elif item[0].strip().lower() == 'admin':
            admin_object_list.append(Laptop_class.Admin_login(item[1] ,item[2]))


# create_object_login_details()

# print(customer_object_list)
# for items in customer_object_list:
#     print(items.get_username())


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
                break
            else:
                print("Incorrect name or password")
                break


def logged_in_operations_customer():
    print ("Please enter 1 to buy \n2 to recieve bill \n3 to logout\n")
    user_input = input()
    if user_input == 1:
        # print ("Select the sn of the item you want to buy")
        handle_file.show_data()

def logged_in_operations_admin():
    pass


create_object_login_details()
# for i in customer_object_list:
#     print (i.get_username())
login()

# logged_in_operations_customer()