# Created by Kushal Bogati
# Date : 2023 / 4 / 25
class Bank:
    __bank_name = "Kushal's Bank" 
    __id = 0
    __intrest_rate = 12
    def __init__(self, name, password, address ,balance = 0) :
        self.__id = Bank.__id
        Bank.__id += 1
        self.__name = name 
        self.__password = password
        self.__address = address
        self.__balance = balance

    def check_balance (self):
        return self.__balance

    def check_name (self):
        return self.__name
    
    def check_password (self):
        return self.__password
    
    def deposit_amount (self, amount):
            self.__balance += amount

    def get_address (self):
        return self.__address
    
    def get_id (self):
        return self.__id
    
    @classmethod
    def get_bank_name (cls):
        return cls.__bank_name
    
    def withdraw_amount (self , amount):
        self.__balance -= amount

    @classmethod
    def get_intrest_rate(cls):
         return cls.__intrest_rate
    
    @classmethod
    def set_intrest_rate(cls , new_rate):
         cls.__intrest_rate = new_rate

    @staticmethod
    def get_gov_holidays ():
         print ("Baishakh 18 : International Labour Day")
         print ("Baishakh 22 : Buddha Jayanti")


def return_id_if_exists(name , password):
    for i in people:
        if i.check_name() == name and i.check_password() == password:
            return i.get_id() , True    #True for name and password matches
        else :
            return None , False

def login ():
    a = input ("Enter your name ")
    b = input ("Enter your password ")
    return return_id_if_exists (a , b)

people = []

while True:
    print ( "*" * 50)
    print ("*" * 13, end = '')
    print(f"Welcome to {Bank.get_bank_name()}", end = '')
    print ("*" * 13)
    print ( "*" * 50)

    user_choice = input ("Enter 1 to register new \nEnter 2 to login \nEnter 3 to close app\n")
    if user_choice == '1': #register new account
        name = input("Register your name \n")
        password = input ("Register your password \n")
        address = input ("Enter your address \n")

        people.append (Bank (name, password, address))
    
    elif user_choice == '2': # login and functions after login
        id , checklogin = login ()
        if checklogin == False :
            print("Incorrect username or password")
            break
        print ( "*" * 50)
        print (f"\t\tLogged in as {people[id].check_name()}")
        print ( "*" * 50)
    
        while True:
            print ("Enter 0 to logout")
            print ("Enter 1 to check balance")
            print ("Enter 2 to deposit")
            print ("Enter 3 to withdraw")
            print ("Enter 4 to check intrest rate")
            print ("Enter 5 to set intrest rate")
            print ("Enter 6 to list holidays")
            print ("Enter 7 to print your details ")
            logged_in_choices = input ()

            if logged_in_choices == '0':
                print ("*" * 50)
                print(f"\t\tLogged out as { people [id].check_name()}")
                print ("*" * 50)
                
                break

            elif logged_in_choices == '1':
                print (f" Your balance is {people[id].check_balance()}")

            elif logged_in_choices == '2': 
                deposit_amt = int (input ("Enter the amount to deposit \n"))

                if deposit_amt > 0:
                    people[id].deposit_amount(deposit_amt)
                    print (f"Amount of {deposit_amt} have been deposited succesfully")
                    print (f"Your new balance is : {people[id].check_balance()}")
                else:
                    print ("Please enter correct parameter")

            elif logged_in_choices == '3':
                withdraw_amt = int (input ("Enter the amount to withdraw \n"))
                if withdraw_amt <= people[id].check_balance():
                    people[id].withdraw_amount(withdraw_amt)
                    print (f"Amount of {withdraw_amt} have been withdrawn succesfully")
                else:
                    print ("Insufficient balance in your account")

            elif logged_in_choices == '4':
                print(f"The intrest rate of bank = {Bank.get_intrest_rate()} %") 

            elif logged_in_choices == '5':
                new_intrest = int(input ("Enter new intrest rate of bank\n"))
                Bank.set_intrest_rate (new_intrest)
                print (f"New intrest rate of {Bank.get_intrest_rate()}% have been applied succesfully")

            elif logged_in_choices == '6':
                Bank.get_gov_holidays()

            elif logged_in_choices == '7':
                print (f"Name : {people [id].check_name() }")
                print (f"Address : {people [id].get_address() }")
                print (f"Balance : {people [id].check_balance()}")
            
            else :
                print ("Please enter the valid choice\n")

            input ()        #wait for user

    elif user_choice == '3': #logout end terminal
        break

    else:       #number out of bounds
        print ("Please enter valid number\n")
