#WHILE LOOP
# while condition:
#   ........(what I want to excute)

# i = 1
# while i <= 5:
#   # print(i)
#   print("*" * i)
#   i = i + 1
# print("Done")

#Guess Game
# secret_number = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#   user_guess = int(input("Make a guess. hint: it is a digit "))
#   guess_count = guess_count + 1
#   if user_guess == secret_number:
#     print("You won ")
#     break
#   else:
#     print("try again ")
# else:
#   print("Sorry, you failed ")


secret_num = 6
count_guess = 0
guess_limit = 3
while count_guess < guess_limit:
  user_guess = int(input("Make a guess. hint: a digit number "))
  count_guess = count_guess + 1
  if (user_guess == secret_num):
    print("You won!")
    break
  #Meaning 2 chances left
  elif count_guess == 1:
    print("You have two chances ")
    #Meaning last chance
  elif count_guess == guess_limit-1:
    print("Try your last chance ")
else:
  print("You failed! ")




#Car game
# car_game = ["start", "stop", "quit"]
# for help in car_game:
#   user_input = input("type help to get a help")
#   print(help)
#   action = input("enter an option for a quick action").lower()
#   if action == "start":
#     print("Car is ready go ...............")
#   elif action == "stop":
#     print("Car has stopped")
#   elif action == "quit":
#     break
# else:
#   print("Invalid command")