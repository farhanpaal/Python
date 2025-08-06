"""
This Python script demonstrates fundamental operations using NumPy, one of the most powerful libraries for numerical computing. It covers:

- Creating and filtering NumPy arrays
- Basic Statistical Operations with NumPy
- check shape, log, sqrt, exp
- Basic statistical computations (sum, mean, median, etc.)
- Array reshaping, logarithmic and exponential functions
- Random number generation with NumPy
- Frequency count of randomly generated integers

Each function in the script (num1 to num5) showcases a specific set of NumPy capabilities, making this code a useful reference or practice material for beginners learning NumPy.
"""

import numpy as np

def num1():

    #➤ Q1: Create an array from 1 to 10 and print all even numbers.
    print("1---------------")
   
    arry = np.arange(1, 11) 
    even_arr = arry[arry % 2 == 0]  # 0 1 0 1 1 0 0 1 0 0 1 --> 1 1 1 1 1    # boolean masking or filtering
    print("Even numbers:", even_arr) 

    print("2---------------")
    
    #➤ Q2: Create a 3x3 matrix filled with 0s, then change the center to 9.
    matric=np.zeros((3,3), dtype=int)
    matric[1,1]=9
    print(matric)

    
    # matric=np.zeros(10).astype(int)
    # print(matric)

    #3
    print("3---------------")
    #➤ Q3: Multiply two 2D arrays of the same shape element-wise.

    TwodArr1=np.array([
        [1,2,3,4],
        [5,4,3,2]
    ])
    TwodArr2=np.array([
        [6,7,5,4],
        [5,4,3,7]
    ])
    print(TwodArr1*TwodArr2)

# num1()


def num2():
    arr1=np.array([2,3,4,5,6,7,4])
    print("sum: ",np.sum(arr1))
    print("mean: ",np.mean(arr1))
    # print(np.mode(arr1))
    print("median: ",np.median(arr1))
    print("max: ",np.max(arr1))
    print("min: ",np.min(arr1))
    print(np.linspace(20, 1, 20))

# num2()

def num3():
    """
    this function is used to check shape, log, sqrt, exp
    """
    arr=np.array([[2,3,4,5,6,7]])
    print(arr.shape)
    b=arr.reshape((2,3))
    print(b)
    print(b.shape)
    print("-------------")

    a = np.array([8, 2, 3])
    sqrt_a = np.sqrt(a) 
    print("sqrt= ",sqrt_a)
    print("-------------")

    log_a = np.log(99)  #WHAT POWER DO WE NEED TO USE ON E TO GET 99 [e=2.718]
    print("log= ",log_a)
    print("-------------")
    c=np.exp(arr)
    print("exponention= ",c)

# num3()


def num4():
    rolls=np.random.randint(1,45,2).tolist()
    print(type(rolls).__name__)
    print(rolls)

    arr2= np.linspace(50,101,45) #(high-low)/elements-1 [it basically finds evenly numbers between high and low and the 3rd value is the qty]
    print(arr2)

# num4()


def num5():
    a=np.random.randint(1,40,20).tolist()
    a1= set(a)
    countDict={}
    for i in a1:
        countDict[i] = a.count(i)
    print(countDict)
    # countNum={i:a.count(i) for i in a1}
    # print(countNum)
num5()