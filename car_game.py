# command = ""

# while True:
#   command = input("> ").lower()
#   if command == "start":
#     print("Ready to go........ Car has started")
#   elif command == "stop":
#     print("Car has stopped")
#   elif command == "quit":
#     print("game quitted")
#     break
#   elif command == "help":
#     print("""
#  > start - to start
#  > stop - to stop
#  > quit - to quit
#  """)
#   else:
#     print("Sorry, I don't understand this")


#Car Game
command = ""
started = False

while command != "quit":
  command = input("> ").lower()
  if command == "start":
    if started:
      print("Car is started already")
    else:
      started = True
      print("Ready to go..... Car has started")
  elif command == "stop":
    if started:
      print("Car is stopped stopped already")
    else:
      started = True
      print("car is stopped")
  elif command == "help":
    print("""
 >start - to start the car 
 >stop - to stop the car 
 >quit - to quit the game
  """)
  elif command == "quit":
    print("game quitted ")
  else:
    print("I don't understand")

  