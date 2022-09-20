get_name = input("What is your name? ")
print("Hello " + get_name)

# DataTypes

# Numbers
age = 27
parsed_age = int("27")

price = 99.99
parsed_price = float("99.99")

# String
name = "Karla"

# Boolean
has_pets = True

# lists

# array of names
names = ["Karla", "Ana", "Mary", "Ben", "Jon"]
print(names[0:2]) # it doesn't modify the original

# array of numbers
ages = [1, 2, 3, 4, 5, 6, 7]
ages.insert(0, "Test") # inserts "Test" on index 0
ages.remove(3) # removes element on index 3
len(ages) # number of elements in ages

# tuples
# immutables

numbers = (1, 2, 3, 4, 5)
