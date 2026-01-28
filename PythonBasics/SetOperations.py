# 1 x 10^308 or 1 followed by 308 zeros is the largest number that can be represented in Python
print(1e308) # this is the limit for integer representation in Python

# 1.7 x 10^308 or 1.7 followed by 308 zeros is the largest float number that can be represented in Python
print(1.7e308) # this is the limit for float representation in Python

print("----- Set Operations in Python -----")

# Demonstrating set operations in Python
A = {1, 2, 2, 3}
B = {3, 4, 5}

print("Set A:", A) # duplicates in set A will be removed
print("Set B:", B)

# union
C = A | B
print("Union of A and B:", C)

# intersection
D = A & B
print("Intersection of A and B:", D)

# difference means elements in A but not in B
E = A - B
print("Difference of A and B (A - B):", E)

# symmetric difference means elements in either A or B but not in both
F = A ^ B
print("Symmetric Difference of A and B:", F)

# Adding an element to set A
A.add(6)
print("Set A after adding 6:", A)
# Removing an element from set B
B.remove(4)
print("Set B after removing 4:", B)

# Checking membership
print("Is 2 in Set A?", 2 in A)
print("Is 4 in Set B?", 4 in B)

# Set comprehension
squared_set = {x**2 for x in range(5)}
print("Set of squares from 0 to 4:", squared_set)

# Frozen set (immutable set) , this cannot be changed after creation
frozen_A = frozenset(A)
print("Frozen Set A:", frozen_A)
# Attempting to add an element to frozen set will raise an error
# frozen_A.add(7) # Uncommenting this line will raise an AttributeError

# Length of set A
print("Length of Set A:", len(A))
# Clear all elements from set B
B.clear()
print("Set B after clearing all elements:", B)  

# Copying set A
copy_of_A = A.copy()
print("Copy of Set A:", copy_of_A)

# Checking if set A is a superset of set D
print("Is Set A a superset of Set D?", A.issuperset(D))

# Checking if set D is a subset of set A
print("Is Set D a subset of Set A?", D.issubset(A)) 

# Removing and returning an arbitrary element from set A
removed_element = A.pop()
print("Removed element from Set A:", removed_element)
print("Set A after popping an element:", A) 

# Updating set A with elements from set B
A.update(B)
print("Set A after updating with Set B:", A)

# Removing an element from set A if it exists
A.discard(10) # No error if 10 is not present
print("Set A after discarding 10 (no error if not present):", A)
# Removing an element from set A, raises KeyError if not found
# A.remove(10) # Uncommenting this line will raise a KeyError if 10
# print("Set A after removing 10:", A)

# Clearing all elements from set A
A.clear()
print("Set A after clearing all elements:", A)

# Final state of sets
print("Final Set A:", A)
print("Final Set B:", B)



