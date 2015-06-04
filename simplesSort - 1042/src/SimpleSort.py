__author__ = 'igor'

values = raw_input().split()

# Here we cast all the fields of a to int (using list comprehensions) and assigned to the tuple a, b, c
values = [int(i) for i in values]

sortedValues = list(values)

# Sort and print in ascending order
sortedValues.sort()
for value in sortedValues:
    print value

# Middle blank line
print('')

# Print it as it was read
for value in values:
    print value


