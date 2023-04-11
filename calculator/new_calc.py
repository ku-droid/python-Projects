# ---------------------CALCULATOR TO TAKE INPUT STRING AND CALCULATE THE ANSWER------------------------------


# slice the string into operation to perform calculation step by step

def slice_string(string , position) :
    left_position = position -1
    right_position = position +1

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


    # print (string[left_position+1 :right_position])
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
        output = str (  - int (a[index_of_operator + 1 : ]) *  int (  a[1:index_of_operator]))
        # return add_positive_before_replace(output)
        return output
    else :
        output = str (   int (a[index_of_operator + 1 : ]) *  int (  a[:index_of_operator]))
        # return add_positive_before_replace(output)
        return output
    
def div_string (a):
    index_of_operator = a[1:].index('/') + 1 
    if a[0] == '-':
        output = str (  - int (  a[1:index_of_operator]) / int (a[index_of_operator + 1 : ]))
        # return add_positive_before_replace(output)
        return output
    else :
        output = str (  int (  a[:index_of_operator]) / int (a[index_of_operator + 1 : ]))
        # return add_positive_before_replace(output)
        return output

# a = "1+3+5-56-200" 
a = "-47-20-200+55-3000*23 /3"
# print(slice_string (a,3))
# i = 1

def replace_string(b,c):
    global a
    a = a.replace(b,c)

while '/' in a [1:] :
    pos = a[1:].index('/') +1
    b = slice_string(a,pos)
    c = div_string(b)
    replace_string (b,c)
    if a[0] == '+':
        a = a[1:]
    print (a)

while '*' in a [1:] :
    pos = a[1:].index('*') +1
    b = slice_string(a,pos)
    c = mul_string(b)
    replace_string (b,c)
    if a[0] == '+':
        a = a[1:]
    print (a)

while '+' in a [1:] :
    pos = a[1:].index('+') +1
    b = slice_string(a,pos)
    c = add_string(b)
    replace_string (b,c)
    if a[0] == '+':
        a = a[1:]
    print (a)

while '-' in a [1:] :
    pos = a[1:].index('-') +1
    b = slice_string(a,pos)
    c = sub_string(b)
    replace_string (b,c)
    print (a)

# print(sub_string(a))
# print (a[1:].index('-')+1)
