# create dir, write a file in it

import os

try:
    os.mkdir("testDir")
    with open ("testDir\\nine.txt", "w") as file:
        file.write("This is the text of my file 1")
        print("Directory and file created successfully")
except FileExistsError:
    print("Directory already exists")
except Exception as e:
    print("error",e)