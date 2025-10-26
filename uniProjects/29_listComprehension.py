def syn1():
    # Traditional way
    squares = []
    for x in range(5):
        squares.append(x ** 2)
    print(squares)  # [0, 1, 4, 9, 16]

    # List comprehension way
    squares = [x ** 2 for x in range(5)]
    print(squares)  # [0, 1, 4, 9, 16]

def syn2():
    # Double each number
    numbers = [1, 2, 3, 4, 5]
    doubled = [x * 2 for x in numbers]
    print(doubled)  # [2, 4, 6, 8, 10]

    # Convert to uppercase
    words = ["hello", "world", "python"]
    upper_words = [word.upper() for word in words]
    print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

def syn3():
    # Square only even numbers
    numbers = [1, 2, 3, 4, 5, 6]
    result = [x ** 2 for x in numbers if x % 2 == 0]
    print(result)  # [4, 16, 36]

    # Mark numbers as even/odd
    numbers = [1, 2, 3, 4, 5]
    labeled = [f"{x} is even" if x % 2 == 0 else f"{x} is odd" for x in numbers]
    print(labeled)
    # ['1 is odd', '2 is even', '3 is odd', '4 is even', '5 is odd']

def syn4():
    # Traditional nested loop
    pairs = []
    for i in range(3):
        for j in range(2):
            pairs.append((i, j))
    print(pairs)  # [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]

    # List comprehension way
    pairs = [(i, j) for i in range(3) for j in range(2)]
    print(pairs)  # Same result

    # Matrix flattening
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]