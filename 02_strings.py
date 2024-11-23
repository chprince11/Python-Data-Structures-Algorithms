""" 

Strings:
- They are immutable, unchangeable objects.
- If append 'd' to 'a,b,c' , need to cretae new string.
- Strings have indices.
- S[1] : 0(1), will provide the string at index 1 in constant time.
- Can't modify, can't change, can't delete

     Operation                  | Strings
i.   Appending to end           | O(n)
ii.  Popping from end           | O(n)
iii. Insertion, not from end    | O(n)
iv.  Deletion, not from end     | O(n)
v.   Modifying an element       | O(n)
vi.  Random access              | O(1)
vii. Checking if element exists | O(n)

"""
# Append to end of string - O(n)

s = 'hello'
b = s + 'z'
print(b) # helloz

# Check if something is in string - O(n)
if 'e' in s:
    print(True)
    
# Access positions - O(n)

print(s[0]) # h

# length of string - O(1)

print(len(s)) # 5
print(len(b)) # 6