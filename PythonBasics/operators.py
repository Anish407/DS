# arithemetic operators
print(f"5/2 = {5/2}")    # Division, Output: 2.5
print(f"5//2 = {5//2}")  # Floor Division, Output: 2
print(f"5%2 = {5%2}")    # Modulus, Output: 1
print(f"5**2 = {5**2}")  # Exponentiation, Output: 25   
# comparison operators
print(f"5 == 2: {5 == 2}")   # Equality, Output: False
print(f"5 != 2: {5 != 2}")   # Inequality, Output: True
print(f"5 > 2: {5 > 2}")     # Greater than, Output: True
print(f"5 < 2: {5 < 2}")     # Less than, Output: False
print(f"5 >= 2: {5 >= 2}")   # Greater than or equal to, Output: True
print(f"5 <= 2: {5 <= 2}")   # Less than or equal to, Output: False
# logical operators
print(f"(5 > 2) and (3 < 4): {(5 > 2) and (3 < 4)}")  # Logical AND, Output: True
print(f"(5 > 2) or (3 > 4): {(5 > 2) or (3 > 4)}")    # Logical OR, Output: True
print(f"not (5 > 2): {not (5 > 2)}")  # Logical NOT, Output: False
# bitwise operators , they operate on binary representations of integers
print(f"5 & 3 = {5 & 3}")   # Bitwise AND, Output: 1, this is because 5 is 101 in binary and 3 is 011 in binary, so AND gives 001 which is 1
print(f"5 | 3 = {5 | 3}")   # Bitwise OR, Output: 7, this is because 5 is 101 in binary and 3 is 011 in binary, so OR gives 111 which is 7
print(f"5 ^ 3 = {5 ^ 3}")   # Bitwise XOR, Output: 6, this is because 5 is 101 in binary and 3 is 011 in binary, so XOR gives 110 which is 6
print(f"~5 = {~5}")     # Bitwise NOT, Output: -6, this is because NOT inverts all bits and in two's complement representation, ~n = -n-1
print(f"5 << 1 = {5 << 1}") # Left Shift, Output: 10,    
print(f"5 >> 1 = {5 >> 1}") # Right Shift, Output: 2
# assignment operators
x = 5
print(f"x = {x}")  # Output: 5
x += 2
print(f"x += 2 -> x = {x}")  # Output: 7
x -= 3
print(f"x -= 3 -> x = {x}")  # Output: 4
x *= 4 # x=4 now
print(f"x *= 4 -> x = {x}")  # Output: 16
x /= 2 # x=16 now
print(f"x /= 2 -> x = {x}")  # Output: 8.0, this is 8 because division operator always returns float
x //= 3 # x=8.0 now
print(f"x //= 3 -> x = {x}")  # Output: 2

# relational operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
    
print(f"a is b: {a is b}")   # Identity operator, Output: True
print(f"a is c: {a is c}")   # Identity operator, Output: False
print(f"a == c: {a == c}")   # Equality operator, Output: True , because values are same
print(f"a is not c: {a is not c}") # Identity operator, Output: True
print(f"a != c: {a != c}")   # Inequality operator, Output: False
# membership operators
my_list = [1, 2, 3, 4, 5]
print('A' in "Anish")  # Membership operator, Output: True
print('z' not in "Anish")  # Membership operator, Output: True
print(f"3 in my_list: {3 in my_list}")     # Membership operator, Output: True
print(f"6 not in my_list: {6 not in my_list}") # Membership operator, Output: True
print(f"2 in my_list: {2 in my_list}")     # Membership operator, Output: True

# operator precedence
result = 5 + 3 * 2  # Multiplication has higher precedence than addition
print(f"5 + 3 * 2 = {result}")  # Output: 11
result = (5 + 3) * 2  # Parentheses change the precedence
print(f"(5 + 3) * 2 = {result}")  # Output: 16  
# chaining comparison operators
x = 5
print(f"3 < x < 10: {3 < x < 10}")  # Output: True
print(f"3 < x > 10: {3 < x > 10}")  # Output: False 
print(f"3 <= x <= 5: {3 <= x <= 5}")  # Output: True






