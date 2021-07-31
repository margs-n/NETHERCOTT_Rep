products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
    information = products[code]
    return information
def get_property(code, prop):
    information = products[code][prop]
    return information

def main():
    orders=[]
    while True: #generate a list of orders, reject any orders that throw errors
        order = input("Please input the product code and quantity. Ex: espresso, 2")
        if order=="/":
            break
        else:
            try:
                cluster = order.split(",")
                cluster[1]=int(cluster[1])
                get_product(cluster[0])
                orders.append(cluster)
                continue
            except:
                print("You entered the wrong product code, or did not follow proper format. Try again.")
                continue
    orders.sort()
    #If a drink appears multiple times, overwrite the current quantity with the total of multiple orders.
    new_quants = []
    for group in orders:
        current_drink = group[0]
        current_quant = group[1]
        new_quantity = 0
        for multiple in orders:
            if multiple[0]==current_drink:
                new_quantity+= multiple[1]
                current_quant = new_quantity
                continue
            else:
                continue
        new_quants.append((current_drink,current_quant))
    final_orders = list(set(new_quants)) #remove duplicate orders
    final_orders.sort() #sort alphabetically

    with open("receipt.txt","w") as receipt:
        receipt.write("==")
        receipt.write("\n")
        receipt.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
        receipt.write("\n")
        running_total=0
        for order in final_orders:
            code = order[0]
            quant = order[-1]
            name = get_product(code)["name"]
            subtotal = int(quant)*get_property(code, "price")
            running_total+=subtotal
            receipt.write(code+"\t\t"+name+"\t\t"+str(quant)+"\t\t\t\t"+str(subtotal)+"\n")
        receipt.write("\n")
        receipt.write("Total: \t\t\t\t\t\t\t\t\t\t"+str(running_total)+"\n")
        receipt.write("==")
main()
