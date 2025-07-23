
mainLst = []

while True:
    Lst = []

    while True:
        num = int(input("Enter num: "))
        if num == -1:
            break
        Lst.append(num)

    # Only add the list if it has data
    if Lst:
        mainLst.append(Lst)

    # Ask if user wants to add another list
    choice = input("Add another list? (y/n): ").lower()
    if choice != 'y':
        break

print(mainLst)
