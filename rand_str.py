import random
import string

str = input("Please enter your string: ")
length = len(str)
count = 0
gen =''

while gen != str:
    gen = random.choices(string.printable, k = length)
    gen = ''.join(gen)
    count = count + 1
    print(gen)
else:
    print(" Found your string is" , gen, "after", count, "tries")