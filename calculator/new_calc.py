# ---------------------CALCULATOR TO TAKE INPUT STRING AND CALCULATE THE ANSWER------------------------------


# slice the string into operation to perform calculation step by step

def slice_string(string , position) :
    left_position = position -1
    right_position = position +1
    if string [right_position] == '-':
        right_position += 1

    while left_position >= 0 and string [left_position] not in "+/*":
        if string [left_position] == '-'  :
            if left_position == 0:
                left_position -= 1
                break
            elif string[left_position - 1] not in "+-/*":
                left_position -= 1
                break
            else :
                left_position -=1
                print (string [left_position])
                continue
        else :
            left_position -= 1
    while right_position <= len(string) -1 and string [right_position] not in "+-/*":
        right_position += 1

    return string [left_position +1 : right_position ]



#------------------- no sign means positive sign--------------------------
def add_positive_before_replace(str):
    if str [0] == '-':
        return str
    else :
        return '+' + str 
    
def add_string (a):
    index_of_operator = a[1:].index('+') + 1 
    if a[0] == '-':
        output = str (   int (a[index_of_operator + 1 : ]) -  int (  a[1:index_of_operator]))
        return add_positive_before_replace(output)
    else :
        output = str (   int (a[index_of_operator + 1 : ]) +  int (  a[:index_of_operator]))
        return add_positive_before_replace(output)

def sub_string (a):
    index_of_operator = a[1:].index('-') + 1 
    if a[0] == '-':
        output = str(- int (a[index_of_operator + 1 : ]) -  int (  a[1:index_of_operator]))
        return add_positive_before_replace(output)
    else :
        output = str (     int (  a[:index_of_operator]) - int (a[index_of_operator + 1 : ]) )
        return add_positive_before_replace(output)
    
def mul_string (a):
    index_of_operator = a[1:].index('*') + 1 
    if a[0] == '-':
        if a[index_of_operator + 1] == '-':
            output = '+' + str (  int (a[index_of_operator + 2 : ]) *  int (  a[1:index_of_operator]))
        else :
            output = str (  - int (a[index_of_operator + 1 : ]) *  int (  a[1:index_of_operator]))
    else :
        if a[index_of_operator + 1] == '-':
            output = str (  - int (a[index_of_operator + 2 : ]) *  int (  a[1:index_of_operator]))

        else :
            output = str (   int (a[index_of_operator + 1 : ]) *  int (  a[:index_of_operator]))
    return output
    
def div_string (a):
    index_of_operator = a[1:].index('/') + 1 
    if a[0] == '-':
        output = str (  - int (  a[1:index_of_operator]) / int (a[index_of_operator + 1 : ]))
    else :
        output = str (  int (  a[:index_of_operator]) / int (a[index_of_operator + 1 : ]))
    return output


def replace_string(b,c):
    global a
    a = a.replace(b,c)

def mul_all():
    global a
    while '*' in a [1:] :
        pos = a[1:].index('*') +1
        b = slice_string(a,pos)
        c = mul_string(b)
        replace_string (b,c)
        if a[0] == '+':
            a = a[1:]
        print (a)

def add_all():
    global a
    while '+' in a [1:] :
        pos = a[1:].index('+') +1
        b = slice_string(a,pos)
        c = add_string(b)
        replace_string (b,c)
        if a[0] == '+':
            a = a[1:]
        print (a)

def sub_all():
    global a
    while '-' in a [1:] :
        pos = a[1:].index('-') +1
        b = slice_string(a,pos)
        c = sub_string(b)
        replace_string (b,c)
        print (a)


def calculate_all():
    global a
    mul_all()
    add_all()
    sub_all()
    if a[0] == '+':
        a = a[1:]

while True :
    a = input("Enter problem to calculate \n")
    calculate_all()
    print (f"Your answer is = {a}")
    b = input ("Enter 0 to exit 1 to continue \n")
    if b == '1':
        continue
    elif b == '0':
        break
