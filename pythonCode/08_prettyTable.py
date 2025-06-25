from prettytable import PrettyTable


def Amount(amount):
    price= amount["price"]
    currency= amount["currency"]
    discount= amount["discount"]
    savedMoney= discount/100*price 
    return {
        "discount":savedMoney
        
    } 

def app():
    table= PrettyTable()
    table.field_names=["Name","Price","Discount","payable"]
   
    products=[
    {
        "name":"Samsung Galaxy J7",
        "price":18000,
        "currency":"$",
        "discount":23
    },
    {
        "name":"One plus nord 4",
        "price":29700,
        "currency":"$",
        "discount":29
    },
    {
        "name":"Redmi note 11T 5G",
        "price":18500,
        "currency":"$",
        "discount":10
    },
    ]

    # Amount(products)
        
    for product in products:
        calc = Amount(product) #Amou()
        table.add_row([product["name"],product["price"],product["discount"], calc["discount"]])
    print(table)

app()