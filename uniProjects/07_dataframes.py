import pandas as pd
import numpy as np

my_dict={
    'Test1':[1,3,4,6,8,9],
    'Test2':[2,3,4,6,8,9],
    'Test3':[8,2,3,6,8,9],
    'Test4':[5,6,4,6,8,9],
    'Test5':[6,3,1,6,8,5],
}
 
# result=[]

# flattenDict= my_dict.values()
# for i in flattenDict:
#     for j in i:
#         if j>3:
#             result.append(j)
# print(result)

 
# dictionary to DataFrame
df = pd.DataFrame(my_dict)

# Print the whole DataFrame
print("DataFrame:\n", df)

# range of rows (0 to 2) 
print("\nRow 0-2: \n", df.loc[0:2])

# Select only columns Test1 to Test3
print("\nColumns Test1 to Test3:\n", df.loc[:,"Test1":"Test3"])

# Select specific rows (0,2) and specific columns (Test2, Test4)
print("\nRows 0 & 2, Columns Test2 & Test4:\n", df.loc[[0,2], ["Test2", "Test4"]])