a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# To store items that are in 'a' but not in 'b'
c = []

# Loop through each value in list 'a'
for val in a:

    # Check if the current value is not in list 'b'
    if val not in b:
        # If it's not in 'b', append it to list 'c'
        c.append(val)

print(c)