#While Loop: This is used to execuse a block of codes multiple times. It's used to build an iteractive programmes and games.
#while condition:
#     ..(As far as the condition is true, this line of code will keep repeating)

i = 1
while (i <= 5):
  print(i)
  #trying expression
  print("*" * i)
  i = i + 1 #This is added to increase the value of i else i will always be less than 5 and we'll run into infinite loop
print("Done")


guess_count = 0
guess_limit = 3
secret_num = 5
while (guess_count < guess_limit):
  guess = int(input("Guess: "))
  guess_count += 1
  if (guess == secret_num):
    print("You won!")
    break
  else:
    print("Try again")
else:
  print("Sorry, you failed!")

