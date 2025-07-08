"""
This program prints the elements of a list that occurs odd number of times.
5 methods are used her
"""


def find_it(seq):
    result = 0
    for num in seq:
        result = result ^ num  # this xor operator, it will only check if only any 1 element is odd times
    return result


# print(find_it([11,11,11,3,3]))


def oddTimes():
    from collections import Counter

    seq = [22, 34, 34, 22, 34, 1, 1, 1]
    freq = Counter(seq).items()
    for num, count in freq:
        if count % 2 != 0:
            print(num, " occurs odd times")
    #or
    # #even_numbers = [num for num, count in freq.items() if count % 2 == 0]
    # #print(even_numbers)


# oddTimes()


def oddTime():
    list = [33, 45, 67, 44, 45, 45, 33, 67]
    count = []
    for i in list:
        if list.count(i) % 2 != 0 and i not in count:
            count.append(i)
    print(count)


# oddTime()


def myOdd():
    print("Enter elements and use -1 to finish ")
    list = []
    while True:

        a = int(input("Enter num: "))
        if a == -1:
            break
        else:
            list.append(a)

    for i in set(list):
        countNum = list.count(i)
        if countNum % 2 != 0:
            print(i, " is odd")
        else:
            print(i, "is even")


# myOdd()


def shortMet():
    a=[22,34,555,67,22,56,78,22,22]
    for i in set(a): print(f"{i} appears {'even' if a.count(i)%2==0 else 'odd'} times")

shortMet()