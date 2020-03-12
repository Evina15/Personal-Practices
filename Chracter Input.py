'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

import datetime

#get user input for their name and age
name = input("Please enter your name: ")
age = input("Please enter your age: ")

#get the current year
now = datetime.datetime.now()

#difference between 100yrs and their age
diff = 100 - int(age)

#show the exact year they will turn 100yrs old
print(f"Hi {name}, you will turn 100yo in {now.year+diff}")







