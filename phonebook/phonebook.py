# contact book using dictonaries
# user input to register new search or edit 

def get_name():
    return input("Please enter the name ").lower()

contacts = { "ram":1234567890 ,"shyam": 2121212121 ,"hari": 1234567341}
while True:
    print("enter the thing you want to do ") 
    a =  int(input( "1 for register , 2 for search , 3 for edit , 4 for show , 5 for delete\n" ))

    if a ==1:
        # name = input ( " enter the name you want to register ").lower()
        name = get_name()
        phone = int( input( f" enter the number of { name } "))
        contacts[name] = phone
        print (contacts)

    elif a == 2:
        search = get_name()
        if search in contacts.keys() :
            print( f" The phone number of { search.capitalize()} is { contacts[search]}")
        else:
            print("The name do not exist enter the name again ")

    elif a == 3:
        edit = get_name()
        if edit in contacts.keys() :
            num = int (input( " enter the phone number "))
            contacts[edit] = num
        else :
            print( "The name doesnot exist " )

    elif a == 4:
        print( "\t\t NAME \t\t\t | \t\t PHONE" )
        for k,v in contacts.items():
            print(f"\t\t {k} \t\t\t | \t\t {v}")

    elif a == 5:
        delete = get_name()
        if delete in contacts.keys() :
            del ( contacts[delete] )
            print ( f"contacts of { delete .capitalize() } deleted succesfully ")
        else :
            print(f" {delete} entry not found ")
        print (contacts)
        
    else :
        print("please enter the values from 1 to 5")

    a = input ("Enter 0 to exit 1 to continue :")
    if a == '0':
        break
    else :
        continue 




        




