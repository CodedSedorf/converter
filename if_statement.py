#If statement in python is essential in python because it allows us to build some programs that can make decision on their own if certain condition is met.
is_hot = False
is_cold = True

if is_hot:
  print("It's a hot day, " )
  print("Drink plenty of water ")
elif is_cold:
  print("It's a colde day ")
  print("Wear warm clothes")
else:
  print("It's a lovely day")



#Imagine the price of a house is $1M. If a buyer has good credit credit, they need to put down 10%. Otherwise they need to put down 20%. Print the down payment

price_of_a_house = 1000000
has_good_credit = False
if has_good_credit:
  down_payment = 0.1 * 1000000
else:
  down_payment = 0.2 * 1000000
print(f"Down payment is ${down_payment} ")
