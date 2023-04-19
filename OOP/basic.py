class Person:
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address
        print (id (self))


x = Person ("hari" , 24 , "lalitpur")
print (id (x))
y = Person ("shyam" , 21 , "kathmandu")
print ( id (y))
print (f" {x.name} is {x.age} years old and lives in {x.address}")