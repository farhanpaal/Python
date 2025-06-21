from prettytable import PrettyTable

def main():
    infoTable= PrettyTable()
    productTable= PrettyTable()
    invoiceTable= PrettyTable()
    invoice={
        "products":[]
    }
    subtotal=0
    invoice["customerName"]=input("Enter Customer name: ")
    invoice["contact"]=int(input("Enter Customer Contact: "))
    invoice["address"]=input("Enter Customer Address: ")
    invoice["date"]=input("Enter Date: ")

    productNum=int(input("How many products you want to add: "))

    for index in range(productNum):
        print("================")
        item=input("Enter Item name: ")
        qty=int(input("Enter Qty: "))
        unitPrice=int(input("Enter unit price: "))
        total=qty*unitPrice
        subtotal=subtotal+total

        invoice["products"].append({
            "item":item,
            "quantity":qty,
            "unitPrice":"₹"+str(unitPrice),
            "Total":"₹"+str(total)
        })

    invoice["Tax"]=int(input("Enter tax rate in percentage"))
    invoice["subtotal"]=subtotal
    invoice["total"]=  float(invoice["subtotal"]-(invoice["Tax"]/100* subtotal))

    infoTable.field_names=["Name","Contact","Address","Date"]
    infoTable.add_row([
        invoice["customerName"],
        invoice["contact"],
        invoice["address"],
        invoice["date"],
    ])

    productTable.field_names=["Item name","Qty","Unit price","Total"]
    for prod in invoice["products"]:
        productTable.add_row([
            prod["item"],
            prod["quantity"],
            prod["unitPrice"],
            prod["Total"]
    ])
        
    invoiceTable.field_names=["Tax","total","Subtotal"]
    invoiceTable.add_row([
        f"{invoice['Tax']}%",              # Add % sign to tax
        f"₹{invoice['total']:.2f}",        # Add ₹ and format to 2 decimal places
        f"₹{invoice['subtotal']:.2f}"      # Add ₹ and format to 2 decimal places
    ])

    print("\n Customer Info:")
    print(infoTable)

    print("\n Product Info:")
    print(productTable)

    print("\n Invoice Info:")
    print(invoiceTable)
main()