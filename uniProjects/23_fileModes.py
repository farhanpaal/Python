# File name
filename = "text.txt"

# 1 Write mode ('w') - creates or overwrites a file
with open(filename, "w") as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")
print("Written to file using 'w' mode.")

# 2 Append mode ('a') - adds at the end of file
with open(filename, "a") as f:
    f.write("This line is appended.\n")
print("Appended to file using 'a' mode.")

# 3 Read mode ('r') - read contents
with open(filename, "r") as f:
    content = f.read()
print("Reading file using 'r' mode:")
print(content)

# 4 Read and write ('r+') - read first, then write
with open(filename, "r+") as f:
    data = f.read()
    f.write("Adding a new line using r+.\n")
print("Used 'r+' mode to read and write.")

# 5 Write and read ('w+') - overwrite then read
with open("example2.txt", "w+") as f:
    f.write("File created using w+ mode.\n")
    data = f.read()
print("Content of example2.txt using 'w+' mode:", data)

# 6 Append and read ('a+') - append and then read
with open("example3.txt", "a+") as f:
    f.write("First line in a+ mode.\n")
    f.seek(0)
    data = f.read()
print("Content of example3.txt using 'a+' mode:")
print(data)
