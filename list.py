from cs50 import get_int

numbers = []

while True:

    number = get_int("Number: ")

    if not number: 
        break
    
    # Avoid duplicates
    if numbeer not in numbers:
        # Add to list
        numbers.append(number)

print()
for number in numbers:
    print(number)
