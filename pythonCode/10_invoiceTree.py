from prettytable import PrettyTable

def main():
    invoice={
        "invoiceNo":1,
        "customerName":"Er Saurav",
        "contact":"+123-456-7890",
        "Address":"63 Ivy road, Hawkville, GA, USA 31036",
        "Date":"16 june 2025",
        "items":[
            {
                "item":"Egg shell camisol Top",
                "quantity":1,
                "unitPrice":123,
                "Total":123
            },
            {
                "item":"Cubban color shirt",
                "quantity":2,
                "unitPrice":127,
                "Total":254
            },
            {
                "item":"Floral cotton dress",
                "quantity":1,
                "unitPrice":123,
                "Total":123
            }
        ],
        "subTotal":500,
        "Tax":0,
        "Total":500
    }
    table= PrettyTable()
    table2= PrettyTable()
    table3= PrettyTable()

    table.field_names=["InvoiceNo","CustomerName","mobile","address","date"]
    table.add_row([
        invoice["invoiceNo"],
        invoice["customerName"],
        invoice["contact"],
        invoice["Address"],
        invoice["Date"]
        ])


    table2.field_names=["Item","Quantity","Unit price","Total"]
    for item in invoice["items"]:
        table2.add_row([
            item["item"],
            item["quantity"],
            item["unitPrice"],
            item["Total"]
    ])

    table3.field_names=["Sub Total","Tax","Total"]
    table3.add_row([
        invoice["subTotal"],
        invoice["Tax"],
        invoice["Total"]
        ])
    
    print("\n Customer Details:")
    print(table)
    print("\n Product Details:")
    print(table2)
    print("\n Invoice Details:")
    print(table3)

main()