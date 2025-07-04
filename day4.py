#string
course = "Python for Beginners"
#Multiline string
email = '''
  Hi John,
  Here is our first email to you.
  Thank you,
  The support team

'''
print(course[-5]) #This will start from the last letter in the string
print(course[0:6]) #This will omit the letter on index six itself
print(email)
another = course[:]
print(another)

#exercise: what will the code below return?
name = "Jennifer"
print(name[1:-1])



#Formatted string
firstName = "John"
lastName = "Smith"
message = f"Hello {firstName} [{lastName}] is a coder "
print(message)


#String methods
my_course = "Python for Beginners"
#len()
print(len(my_course))
#uppercase and lowercase
print(my_course.upper())
#find, replace
print(course.find("for"))
print(my_course.replace("Beginner", "Absolute Beginner"))
#Note that while you try to replace, you should consider the case of the word you're trying to replace else it will not replace the word. Eg if i try to replace the Beginner like this "beginner" whereas it started with capital letter in the variable.
#single character too can also be replace in the string eg
print(my_course.replace("P", "C"))
#checking existence of character or sequence of character, in operator is used
print("Python" in my_course)
print("python" in my_course)
#Everything learned in this class
#len(), lower(), upper(), find(), replace(), title(), in
print(my_course.title())


print(len(my_course[1:6]))


hobby = "I am learning coding"
print(hobby.find("learning"))
print(hobby[4:13])


#Augmented operator
num = 15
# num = 15 + 1
num += 1
print(num)