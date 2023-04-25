class Bank:
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
    
    def withdraw_amount (self , amount):
        self.__balance -= int(amount)

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


def return_id(name , password):
    for i in people:
        if i.check_name() == name and i.check_password() == password:
            print (f"Logged in as {name}")
            return i.get_id() , True
        else :
            print ("Invalid name or Password")
            return None , False

def login ():
    a = input ("Enter your name ")
    b = input ("Enter your password ")
    return return_id (a , b)

people = []
while True:
    a = input ("Enter 1 to register new \nEnter 2 to login \nEnter 3 to close app\n")
    if a == '1': #register new account
        b = input("Register your name \n")
        c = input ("Register your password \n")
        d = input ("Enter your address \n")

        people.append (Bank (b, c, d))
    
    elif a == '2': # login and functions after login
        id , checklog = login ()
        if checklog == False :
            break
        while True:
            print ("------------------------------Welcome to Bank -----------------------")
            print ("Enter 0 to logout")
            print ("Enter 1 to check balance")
            print ("Enter 2 to deposit")
            print ("Enter 3 to withdraw")
            print ("Enter 4 to check intrest rate")
            print ("Enter 5 to set intrest rate")
            print ("Enter 6 to list holidays")
            print ("Enter 7 to print your details ")
            a = input ()

            if a == '0':
                print ("-------------------------------------------------------")

                print(f"Logged out as { people [id].check_name()}")
                print ("-------------------------------------------------------")
                break

            elif a == '1':
                print (f" Your balance is {people[id].check_balance()}")

            elif a == '2': 
                b = int (input ("Enter the amount to deposit \n"))

                if b > 0:
                    people[id].deposit_amount(b)
                    print (f"Amount of {b} have been deposited succesfully")
                    print (f"Your new balance is : {people[id].check_balance()}")
                else:
                    print ("Please enter correct parameter")


            elif a == '3':
                b = int (input ("Enter the amount to withdraw \n"))
                if b <= people[id].check_balance():
                    people[id].withdraw_amount(b)
                    print (f"Amount of {b} have been withdrawn succesfully")
                else:
                    print ("Insufficient balance in your account")

            elif a == '4':
                print(f"The intrest rate of bank = {Bank.get_intrest_rate()} %") 

            elif a == '5':
                b = input ("Enter new intrest rate of bank\n")
                Bank.set_intrest_rate (b)
                print (f"New intrest rate of {Bank.get_intrest_rate()}% have been applied succesfully")


            elif a == '6':
                Bank.get_gov_holidays()

            elif a == '7':
                print (f"Name : {people [id].check_name() }")
                print (f"Address : {people [id].get_address() }")
                print (f"Balance : {people [id].check_balance()}")
            
            else :
                print ("Please enter the valid choice\n")

            input ()

    elif a == '3': #logout end terminal
        break

    else:       #number out of bounds
        print ("Please enter valid number\n")
