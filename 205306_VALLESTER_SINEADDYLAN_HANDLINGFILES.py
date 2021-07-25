products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    subtotal = 0
    total = 0
    orders_dict = {}
    name_list =[]
    subtotal_list=[]

    try:
        while True:
            clerk_input = input("Input customer's orders: ")
            if clerk_input == "/":
                break

            else:
                split_input = clerk_input.split(",")
                code = split_input[0]
                quantity = int(split_input[1])

                #for products ordered multiple times in a single order
                if code in orders_dict:
                    orders_dict[code] += quantity

                else:
                    orders_dict[code] = quantity

                orders_dict = dict(sorted(orders_dict.items()))

                quantity_list = [q for q in orders_dict.values()]

        code_list = [c for c in orders_dict.keys()]
        for code in code_list:
            name_list.append(get_property(code,"name"))
            subtotal_list.append(get_property(code,"price")*orders_dict[code])

        total = sum(subtotal_list)

        with open("receipt.txt","w") as receipt:
            receipt.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
''')

            orders = list(zip(*[code_list,name_list,quantity_list,subtotal_list]))
            for rows in orders:
                receipt.write(f'''{rows[0]}\t\t\t{rows[1]}\t\t\t{rows[2]}\t\t\t{rows[3]}
''')

            receipt.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')
    except:
        print("An error occurred.")

main()
