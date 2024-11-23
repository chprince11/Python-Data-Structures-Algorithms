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