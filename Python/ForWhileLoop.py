# # While Loop
# Score = 500
# while Score > 100:
#     Score = int(input("Please enter a score:\n"))
#     if Score > 100:
#         print("Invalid score. Try again.")
# if Score >= 85:
#     print(" - Distinction - ")
# elif Score >= 65:
#     print(" - Pass - ")
# else:
#     print(" - Fail - ")

# QA Community Exercise - Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"
# count = 0
# while count < 5:
#     name = str((input("Please enter a name:\n")))
#     print(name, "is awesome!\n")
#     count += 1

# - https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php -

# 01. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 
# i = 0
# for i in range (1500, 2701):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)

# 02. Write a Python program to convert temperatures to and from celsius, fahrenheit
# metricOrImperial = input(str("Are you using Celsius or Fahrenheit?\n")).lower()
# workingTemperature = input(str("What is the temperature?\n"))
# if metricOrImperial[0] == "c":
#     print(str(int(workingTemperature) / 60 * 140) +"\N{DEGREE SIGN}f")
# else:
#     print(str(int(workingTemperature) / 45 * 7) +"\N{DEGREE SIGN}c")

# 03. Write a Python program to guess a number between 1 to 9. 
# import random
# print("I am thinking of a number between 1 and 10.\nCan you guess what it is?")
# secretNumber, guessNumber = random.randint(1,10), 0
# guessCount = 0
# while secretNumber != guessNumber:
#     guessNumber = int(input('Guess a number between 1 and 10:\n'))
#     guessCount +=1
#     if guessNumber > secretNumber:
#         print('Too high. Please try again.')
#     elif guessNumber < secretNumber:
#         print('Too low. Please try again.')
# print('Nice. It was ' + str(secretNumber) + ".\nIt took you " + str(guessCount) + " guesses.")

# 04. Write a Python program that accepts a word from the user and reverse it.
userWord = input("Please enter a word:\n")
# reverseWold = userWord[::-1]
# print(reverseWord)
reverseWord = ""
letterCount = len(userWord)
for i in range(letterCount-1,-1,-1):
    reverseWord = reverseWord + userWord[i]
print(reverseWord)

# The Python Workbook

# Exercise 61: Average
# scoresList = []
# print("Let us find the average scores.")
# while True:
#     scoreSingle = int(input("Please enter a score:\n"))
#     if scoreSingle == 0:
#         break
#     scoresList.append(scoreSingle)
#     print(scoresList)
# print("The average score is " + str(sum(scoresList) / len(scoresList)))

# The Python Workbook - Exercise 62: Discount Table
