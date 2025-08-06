import random as rand

a=rand.randrange(88,100,5) # it prints random number from range and sets the gap of 5
print(a)

b=rand.randint(88,100) # it takes only 2 arguments 
print(b)


colors = ['red', 'green', 'blue',"orange"]
print(rand.choice(colors))  # prints random element
print(rand.choices(colors, k=4))  # prints random elements along with qty
print(rand.sample(colors, k=4))  # It prints unique elements


rand.shuffle(colors) #it shuffles the list in-plac
print(colors)


print(rand.uniform(1,4)) #it returns random float



