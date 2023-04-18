class Person:
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address


x = Person ("hari" , 24 , "lalitpur")
y = Person ("shyam" , 21 , "kathmandu")

print (f" {x.name} is {x.age} years old and lives in {x.address}")