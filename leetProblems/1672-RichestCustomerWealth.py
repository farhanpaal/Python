"""
This program will take the amount of money of a customer in different banks and then compare it with other customers and will return which user has more wealth in banks.
"""


def wealth():
    print(">> RICHEST CUSTOMER WEALTH CALCULATOR")
    print(">> INSTRUCTIONS : ------------------")
    print("• Enter wealth amounts for each customer across different banks")
    print("• Press '-1' to finish adding banks for current customer")
    print("• Press '-2' to stop adding customers and find the richest")
    print(35 * "-")

    all_customers = []  # Store all customer wealth data
    customer_num = 1

    while True:
        print(f"\n--- CUSTOMER {customer_num} ---")
        customer_wealth = []
        bank_num = 1

        while True:
            try:
                amount = int(
                    input(
                        f"Enter Customer {customer_num} wealth in Bank {bank_num} (or -1 to finish this customer): "
                    ))

                if amount == -1:
                    if customer_wealth:  # Only add if customer has some wealth data
                        all_customers.append(customer_wealth)
                        customer_num += 1
                    break
                elif amount == -2:
                    if customer_wealth:  # Add current customer if they have data
                        all_customers.append(customer_wealth)
                    # Exit both loops
                    break
                else:
                    customer_wealth.append(amount)
                    bank_num += 1

            except ValueError:
                print("Please enter a valid number!")

        # Check if user wants to stop adding customers
        if amount == -2:
            break

        # Ask if user wants to add another customer
        if customer_wealth:  # Only ask if we successfully added a customer
            continue_choice = input("Add another customer? (y/n): ").lower()
            if continue_choice != 'y':
                break

    # Calculate and display results
    if not all_customers:
        print("No customer data entered!")
        return

    print(f"\n{35*'='}")
    print("WEALTH ANALYSIS:")
    print(f"{35*'='}")

    max_wealth = 0
    richest_customer = 0

    for i, customer in enumerate(all_customers):
        total_wealth = sum(customer)
        print(
            f"Customer {i+1}: Banks: {customer} | Total Wealth: {total_wealth}"
        )

        if total_wealth > max_wealth:
            max_wealth = total_wealth
            richest_customer = i + 1

    print(f"\n🏆 RICHEST CUSTOMER: Customer {richest_customer}")
    print(f"💰 Maximum Wealth: {max_wealth}")


# Alternative simple version for testing
def simple_wealth_test():
    """Simple test function with predefined data"""
    customers = [
        [1, 2, 3],  # Customer 1: total = 6
        [3, 2, 1],  # Customer 2: total = 6  
        [1, 5],  # Customer 3: total = 6
        [7, 3],  # Customer 4: total = 10 (richest)
        [3, 5]  # Customer 5: total = 8
    ]

    max_wealth = 0
    for customer in customers:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth

    print(f"Test Result - Maximum Wealth: {max_wealth}")
    return max_wealth


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Interactive wealth calculator")
    print("2. Run test with sample data")

    try:
        choice = int(input("Enter choice (1 or 2): "))
        if choice == 1:
            wealth()
        elif choice == 2:
            simple_wealth_test()
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter 1 or 2!")
