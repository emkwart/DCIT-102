# EMMANUEL KOFI KWARTENG
# 10949837
# Finding prime numbers within a given range
print("This is a program that prints a list of even numbers less than a given number, finds their sum and their average in python.")
b = int(input("Enter a number to test the program: "))
j = 0
evenlist = []
for num in range(1,b):
    if num%2==0:
        evenlist.append(num)
        j += 1
add = int(sum(evenlist))
average = (add/j)
print ("There are",j,"even numbers less than the number",b,",that is",evenlist,"and thier sum is",add,"and their average is",average)
print("This is a program that prints a list of prime numbers less than a given number, finds their sum and their average in python.")
# b = int(input("Enter a number to test the program: "))
j = 0
primelist = []
for num in range(1,b):
    isPrime = True
    if num < 2:
        continue
    for x in range(2,num):
        if num%x==0:
            isPrime= False
            break
    if isPrime == True:
            primelist.append(num)
            j += 1
add = int(sum(primelist))
average = (add//j)
print ("There are",j,"prime numbers less than the number",b,",that is",primelist,"and thier sum is",add,"and their average is",average)