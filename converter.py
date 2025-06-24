userName = input(" Enter your name ")
userAge = input(" Enter your age ")
showAge = input(" Show age in days, hours, minutes, seconds or all ").lower()

if showAge == "days" or showAge == "day":
  resDays = int(userAge) * 365
  print(f" Hello {userName}, your age in days is {resDays} ")
elif showAge == "hour" or showAge == "hours" :
  resHrs = int(userAge) * 365 * 24
  print(f" Hello {userName}, your age in hour is {resHrs} ")
elif showAge == "minutes" or showAge == "minute":
  resMins = int(userAge) * 365 * 24 * 60
  print(f" Hello {userName}, your age in minutes is {resMins} ")
elif showAge == "second" or showAge == "seconds":
  resSecs = int(userAge) * 365 * 24 * 60 * 60
  print(f" Hello {userName}, your age in seconds is {resSecs} ")
elif showAge == "all":
  resDays1 = int(userAge) * 365
  resHrs1 = int(userAge) * 365 * 24
  resMins1 = int(userAge) * 365 * 24 * 60
  resSecs1 = int(userAge) * 365 * 24 * 60 * 60
  print(f" Hello {userName}, you are {resDays1} days, {resHrs1} hours, {resMins1} minutes and {resSecs1} seconds")
else:
  print("Print invalid input")