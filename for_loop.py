
# for x in range(6,2,-2):
#     print(x)

#     1. Print numbers from 1 to 10
# Write a program that prints numbers from 1 to 10 using a for loop.

# 2. Print even numbers from 1 to 20
# Modify the previous program to print only even numbers between 1 and 20.




#  Print all odd numbers from 0 - 50.

# for x in range(1,10):
#     print(x)

# for x in range(0,20,2):
#     print(x)

# 4. Print multiplication table
# Ask the user for a number and print its multiplication table up to 10.

# num = int(input("Enter a number: "))

# for x in range(1,11):
    # print( num, "*", x, "=", num*x)
    # print(num*x)

# continue - for loops

pokemon = ['pikachu', 'charizard', 'gyarados', 'scyther', 'lugia', 'arceus']
for pokey in pokemon:
    if pokey != 'arceus':
        continue

    print(pokey)
