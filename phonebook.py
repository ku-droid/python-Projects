# contact book using dictonaries
# user input to register new search or edit 

contacts = { "ram":1234567890 ,"shyam": 2121212121 ,"hari": 1234567341}
while True:
    print("enter the thing you want to do ") 
    a =  int(input( "1 for register , 2 for search , 3 for edit , 4 for show , 5 for delete\n" ))

    if a ==1:
        name = input ( " enter the name you want to register ").lower()
        phone = int( input( f" enter the number of { name } "))
        contacts[name] = phone
        print (contacts)

    elif a == 2:
        search = input ( "enter the name you want to search number of ").lower()
        if search in contacts.keys() :
            print( f" The phone number of { search.capitalize()} is { contacts[search]}")
        else:
            print("The name do not exist enter the name again ")

    elif a == 3:
        edit = input ("enter the name of number you want to edit").lower()
        if edit in contacts.keys() :
            num = int (input( " enter the phone number "))
            contacts[edit] = num
        else :
            print( "The name doesnot exist " )

    elif a == 4:
        print (contacts)

    elif a == 5:
        delete = input ("enter the name of number you want to delete ").lower()
        if delete in contacts.keys() :
            del ( contacts[delete] )
            print ( f"contacts of { delete .capitalize() } deleted succesfully ")
        else :
            print(f" {delete} entry not found ")
        print (contacts)
        
    else :
        print("please enter the values from 1 to 5")




        




