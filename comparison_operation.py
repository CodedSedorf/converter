



#Exercise
#If name is less than 3 characters long, print name must be at least 3 characters. Otherwise if it's more than 50 characters, print name cannot be a maximum of 50 characters. Otherwise, print name looks good!
# name = input("Enter your full name ")
# if (len(name) < 3):
#   print("name must be at least 3 characters ")
# elif (len(name) > 50):
#   print("Name can be a maximum of 50 characters ")
# else:
#   print("Congratulation! Name looks good.")


#Exercise
#Weight conversion
weight = float(input("Weight: "))
unit = input("(L) bs or (K)g: ").lower()
if (unit == "l"):
  result = weight * 0.45
  print(f"You are {result} kilos ")
elif (unit == "k"):
  result = weight / 0.45
  print(f"You are {result} pounds")