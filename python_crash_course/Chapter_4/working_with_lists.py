# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

# Making Numerical Lists
for value in range(1,5):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(6))
print(numbers)
# Using range() to Make a List of Even Numbers
even_numbers = list(range(2,15,2)) # The third argument tells it to count every 2 numbers
print(even_numbers)
# Using range() to Make a List of Square Numbers
squares = []
for value in range(1,11):
    square = value ** 2 # Using the operation ** means "to the power of"
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = list(range(11))
print(f"The least value was {min(digits)}")
print(f"The greatest value was {max(digits)}")
print(f"The sum of all values is {sum(digits)}")

# List Comprehensions