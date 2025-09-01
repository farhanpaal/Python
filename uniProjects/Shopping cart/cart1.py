num=1

import pandas as pd
def viewCustomerDetails(customer_name):
    df = pd.read_excel("user_data.xlsx")
    
    customer_data = df[df["Customer Name"].str.contains(customer_name, case=True)]
    print(customer_data.iloc[2,:])
    
    if not customer_data.empty:
        print(f"Details for {customer_name}:")
        print(customer_data.to_string(index=False))  # show without row index
        orderConfirm= df[df["ID"] == num]
        print(orderConfirm)
    else:
        print(f"No records found for {customer_name}.")

viewCustomerDetails("farhan")