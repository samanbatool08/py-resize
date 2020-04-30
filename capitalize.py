from cs50 import get_string

s = get_string("Name: ")
# for every charact in the string s
for c in s: 
    print(c.upper)
# to avoid skipping to next line:
#     print(c, end="")
