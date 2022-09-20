weight = float(input("Enter your weight: "))
unit = input("Kilograms (K) or pounds (L)? ")

if unit.lower() == "k":
  print("Weight in Lbs:", int(weight * 2.2))
else:
  print("Weight in Kg:", int(weight * 0.45))
