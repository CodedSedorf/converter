#Type conversion: 
#Below will show an error. Explain how to read the error in the terminal for them.
birth_year = input("Birth year: ")
# age = 2019 - birth_year
#wwhat python sees: 2019 - "1990" 
#To fix this line 4 error:
age = 2019 - int(birth_year)
print(age)
#To convert:
#int() this converts variable to integer
#float() this convert variable to decimal number
#bool() converts a sting to booleam
#str() converts number to string

#Getting type of variable:
print(type(birth_year))
print(type(age))


#Exercise: Ask a user their weight (in pounds), convert it to kilogram and print on the terminal
#solution
weight_lbs = int(input("Weight (lbs): "))
weight_kg = weight_lbs * 0.45
print("Hello, weight in lbs is " + str(weight_kg) )