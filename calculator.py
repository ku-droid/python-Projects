def add(a):
    ind = a.index('+')
    return int(a[:ind]) + int(a[ind+1:])

# def paran(a):
#     ind1 = a.index('(')
#     ind2 = a.index(')')
#     return a[ind1+1 : ind2]

# a = input ("Please enter the addition :")

# if "(" or ")" in a :
#     a = paran(a)
# for i in a :
#     if 

 
a = list()
n = input ("Please enter the addition :")
i = 0
while i != len(n): 
    if n[i] in '+-/*':
        a.append(i) 
    i +=1
def str_slic():
    print (a)

str_slic()


