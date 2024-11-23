""" 
Static arrays: 
- It is basically a contiguous block of memory with a fixed size.
- They are mutable objects, which means they are changeable. 
- Can't change the size, but could change at particular index.
- Can check a value in an array.
- Python generally don't have like static arrays.

# Dynamic arrays:
- Also called list in Python.
- An array that can change size.
- Basically creates a new array and copy the elements from the previous array and the new array is double the size of old one.

     Operation                  | Arrays/List/Dynamic Arrays
i.   Appending to end           | *O(1)
ii.  Popping from end           | O(1)
iii. Insertion, not from end    | O(n)
iv.  Deletion, not from end     | O(n)
v.   Modifying an element       | O(1)
vi.  Random access              | O(1)
vii. Checking if element exists | O(n)

"""

A = [1,2,3]
# printing an array
print(A) # [1, 2, 3]

# Append - Insert element at end of array - On average: O(1)
A.append(5)
print(A) # [1, 2, 3, 5]

# Pop - Deleting the last element - O(1)
A.pop()
print(A) # [1, 2, 3]

# Insert ( not at end of array) - O(n)
A.insert(2, 5)
print(A) # [1, 2, 5, 3]

# Modify an element - O(1)
A[0] = 7
print(A) # [7, 2, 5, 3]

# Accessing element given index i
print(A[2]) # 5

if 7 in A: 
     print(True) # True
     
if 6 in A: 
     print(True)
else: 
     print(False) # False
     
# length of an array

print(len(A)) # 4