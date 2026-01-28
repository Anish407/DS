# while loop example

# program to print tables of number entered by user
num = int(input("Enter a number: "))
i=1
limit= int(input("Enter a limit: "))

print(f"Table of {num}: odd number using while loops")
while i <= limit:
    if i % 2 != 0:
     print(f"{num} x {i} = {num*i}")
    i+=1    
print("-----")

# for loop example
print(f"Table of {num}: using for loops only even numbers")
for number in range(1,limit):
    if number % 2 == 0:
     print(f"{num} x {number} = {num*number}")
    
print("-----")