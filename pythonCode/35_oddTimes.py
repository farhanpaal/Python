"""
This program prints the elements of a list that occurs odd number of times.
3 methods are used her
"""


def find_it(seq):
    result = 0
    for num in seq:
        result = result ^ num # this xor operator, it will only check if only any 1 element is odd times
    return result

# print(find_it([11,11,11,3,3]))




def oddTimes():
    from collections import Counter

    seq=[22, 34, 34, 22, 34, 1, 1, 1]
    freq = Counter(seq).items()
    for num, count in freq:
        if count % 2 !=0:
            print(num," occurs odd times")
    #or
    # #even_numbers = [num for num, count in freq.items() if count % 2 == 0]
    # #print(even_numbers)
# oddTimes()


def oddTime():
    list=[33,45,67,44,45,45,33,67]
    count=[]
    for i in list:
        if list.count(i)%2 !=0 and i not in count:
            count.append(i)
    print(count)
oddTime()