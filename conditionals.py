title = 'House of the Dragon'
print('House' in title) # returns a boolean

temperature = 14

# not curly braces, just indentation (why lord?)
if temperature > 25:
  print("It's a hot summer day")
elif temperature > 15:
  print("It's a nice day!")
elif temperature > 10:
  print("It's a bit cold")
else:
  print("It's cold")

# while loops
i = 0
j = 1

while i <= 1_000:
  i += 100
  print(i)

# mario piramid/blocks
while j <= 10:
  print(j * "*")
  j += 1

# for loops

numbers = [1, 2, 3, 4, 5] # range(1, 5), a third number would be the steps

for item in numbers:
  print(item)

k = 0

while k < len(numbers): # same output/result from for loop
  print(numbers[k])
  k += 1

