#and & or
#AND: both condition should be true
#OR: At least one condition should be true
#NOT: This will change true to false and false to true

has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
  print("Eligible for loan")
else:
  print("Not eligible for loan")


has_car = True
has_house = False
if has_car and not has_house:
  print("You are eligible to get marry")