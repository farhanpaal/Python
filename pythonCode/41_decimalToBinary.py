
"""
Decimal to binary using while loop
"""

num = int(input("Enter number: "))
# rule of conversion : eg 1 -> 01, 2 -> 10, 3 -> 11, 4 -> 100

if num == 0:
    print("0")
else:
    a = ""
    while num > 0:
        a=str(num % 2)+a  # Get remainder (0 or 1)
        num = num // 2     # Integer division by 2

    print(f"Binary representation: {a}")
