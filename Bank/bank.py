bank_users = { "ram" : 2000 ,"shyam":10000, "hari" : 20000, "sita" : 25000 ,"rita" : 500000 , "gita" : 300000}

# =============================================== Functions===============================================================
def create_account(balance = 0):
    a = get_name()
    bank_users [a] = balance


def show_amount ( name ):
    print(f"Hello {name} your bank balance is { bank_users [name] }")


def deposit (name , amount ):
    bank_users [name] += amount
    print( f" Dear {name.capitalize()} The amount of {amount} have been deposited succesfully ")


def withdraw (name , amount ):
    bank_users [name] -= amount
    print( f" Dear {name.capitalize()} The amount of {amount} have been withdrawn from your account")


def check_user (name):
    return True if name in bank_users else False


def get_name ():
    return input("Enter your name :\n")


def get_amount ( name ):
    return bank_users [ name ] 


def set_amount ():
    return int( input ( "enter the amount\n"))


def valid_name():
    print("Please enter a valid name ")


# ==================================================================CODE==========================================================================
while True:
    a = int( input( "Please enter 1 to create new account 2 to show your amount 3 to deposit 4 to withdraw \n") )

    if a == 1:
        b = int ( input ( "Please enter 1 to create zero balance account and 2 to create normal account\n"))
        if b == 1:
            create_account()
        elif b == 2:
            c = set_amount()
            create_account(c)
        else :
            print('please enter values between 1 and 2\n')
            continue
    elif a == 2:
        b = get_name().lower()
        if check_user(b) == True:
            show_amount(b)
        else:
            valid_name()
            continue
    elif a == 3:
        b = get_name().lower()
        c = set_amount()
        if check_user(b) == True:
            deposit(b,c)
        else:
            valid_name()

    elif a == 4:
        b =get_name().lower()
        c = set_amount()
        if check_user(b) == True:
            if get_amount(b) >= c:
                withdraw( b , c)
            else:
                print(f"Dear {b.capitalize()} You do not have enough balance to make this transaction \n")
                continue
        else:
            valid_name()

    else :
        print("Please enter values from 1 to 4\n")

    print("----------------------------------------------------------------------------------------------")


        



    





    