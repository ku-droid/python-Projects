class Bank:
    intrest_rate = 12

    def __init__(self, fname, lname, address, balance = 0) :
        self.__fname = fname
        self.__lname = lname
        self.__address = address
        self.__balance = balance
        print (f"Please remember your id \n Your id is {Bank.id}")

    def check_balance (self):
        return self.__balance
    
    def deposit_amount (self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"Amount of {amount} have been deposited succesfully")
        else :
             print ("Please enter correct parameter")

    def withdraw_amount (self , amount):
            if self.__balance >= amount:
                self.__balance -= amount
                print (f"Amount of {amount} have been withdrawn succesfully")
            else:
                 print ("Couldnot withdraw amound due to unsufficient balance ")
    @classmethod
    def get_intrest_rate(cls):
         return cls.intrest_rate
    
    @classmethod
    def set_intrest_rate(cls , new_rate):
         cls.intrest_rate = new_rate
         print (f"New intrest rate of {new_rate} have been applied succesfully")
    
    @staticmethod
    def get_gov_holidays ():
         print ("Baishakh 18 : International Labour Day")
         print ("Baishakh 22 : Buddha Jayanti")

acc = []

while True:
    print ("------------------------------Welcome to Bank -----------------------")
    print ("Enter 0 to exit")
    print ("Enter 1 to create new account ")
    print ("Enter 2 to check balance")
    print ("Enter 3 to deposit")
    print ("Enter 4 to withdraw")
    print ("Enter 5 to check intrest rate")
    print ("Enter 6 to set intrest rate")
    print ("Enter 7 to list holidays")
    a = input ()
    if a == '0':
        break
    
    elif a == '1':
        b = input ("Please enter your first name ")
        c = input ("Please enter your last name ")
        d = input ("Please enter your address")
        e = input ("1 to create zero balance account 2 to create normal account ")

        if e == '1':
            acc = Bank (b, c, d)
        if e == '2':
            f = input ("Enter balance to add to new account ")
            acc = Bank (b, c, d, f)

    elif a == '2':
        print (f" Your balance is {acc.check_balance()}")
    elif a == '3': 
        b = input ("Enter the amount to deposit")
        acc.deposit_amount(b)
    elif a == '4':
         b = input ("Enter the amount to withdraw")
         acc.withdraw_amount(b)

    elif a == '5':
        print(f"The intrest rate of bank = {Bank.get_intrest_rate()}") 

    elif a == '6':
        b = input ("Enter new intrest rate of bank")
        Bank.set_intrest_rate (b)
    elif a == '7':
        Bank.get_gov_holidays()
    
    else :
        print ("Please enter the valid choice")

    input ()
        
