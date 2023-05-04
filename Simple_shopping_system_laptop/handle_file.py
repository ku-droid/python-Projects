from Laptop_class import Laptop_Details
data = []
buyer_bill_no = 0

def create_object_list():
    with open ('laptop_specs_and_price.txt', 'r') as f:
        for line in f:
            line = line.split(')')[1]
            name, info = line.split(':')
            info = info.split(',')

            data.append(Laptop_Details(name, info[0], info[1], info[2], info[3], info[4], info[5], info[6]))
    # return data



def create_bill_customer(data):
    global buyer_bill_no
    with open(str(buyer_bill_no)+'.txt' , 'w') as f:
        buyer_bill_no += 1
        f.write("Name\t\t|\t\tCPU\t\t|\t\tGPU\t\t|\t\tRAM\t\t|\t\tmemory\t\t|\t\tdisplay\t\t|\t\tprice\t\t|\t\tquantity\n")
        for item in data:
            f.write(item.get_name() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_CPU() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_GPU() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_memory() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_display() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_price() + '\t\t')
            f.write('|\t\t')
            f.write(item.get_quantity() + '\t\t')



create_object_list()
buying_data = []
buying_data.append( data[0])
buying_data[0].set_quantity(3)


# print (buying_data[0].get_quantity())
