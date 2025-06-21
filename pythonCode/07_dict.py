

from prettytable import PrettyTable
def app():
    phone= PrettyTable()
    phone.field_names=["Name","class","row","payable"]
    phone.add_row(["farhan",1,2])
    phone.add_row(["Zahid",1,2])
    phone.add_row(["Burhan",1,2])

    print(phone)
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
        "name":"Nokia",
        "price":23700,
        "currency":"$",
        "discount":23
    },
    {
        "name":"Redmi note 11T 5G",
        "price":18500,
        "currency":"$",
        "discount":10
    },
    ]
    Amount(products)
    for product in products:
        print("Name: ",product["name"])
        print("Price: ",product["price"])
        print("========================")

app()