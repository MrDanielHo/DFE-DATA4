'''
Argos
From typing import final
'''
# def stock_stuff(input_variable1,input_variable2):
#     product_code_length = len(input_variable1)
#     if int(input_variable2)%2 == 0:
#         quantity = "It is even number of products."
#     else:
#         quantity = "It is odd number of products."
#     return (product_code_length,quantity)

# product_code = input("What do you want to buy?\n")
# product_quantity = input("How many?\n")

# returnvar = stock_stuff(product_code,product_quantity)
# print(returnvar)

'''
Create a program that works out a grade based on marks with the use of functions.
The program should take inputs:
 - students name,
 - homework score (/25),
 - assessment score (/50), and 
 - final exam score (/100)
output:
 - name 
 - final ICT grade as a percentage.
Reminder: inputs and prints should not be included inside the function definition, and should strictly be done outside.
Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)
'''
# Final Grade
# def calcFinalScore(int_homeworkScore, int_assessmentScore, int_examScore):
#     finalScore = (int(int_homeworkScore) + int(int_assessmentScore) + int(int_examScore)) / 175 * 100
#     if int(finalScore) >= 95:
#         gradedScore = "A*"
#     elif int(finalScore) >= 85:
#         gradedScore = "A"
#     elif int(finalScore) >= 75:
#         gradedScore = "B"
#     elif int(finalScore) >= 65:
#         gradedScore = "C"
#     elif int(finalScore) >= 55:
#         gradedScore = "D"
#     elif int(finalScore) >= 45:
#         gradedScore = "E"
#     else:
#         gradedScore = "F"
#     return (finalScore, gradedScore)

# studentName = input('Student Name:\n')
# homeworkScore = input('What did ' + studentName + ' score on their homework?\n')
# assessmentScore = input('What did ' + studentName + ' score on their assessment?\n')
# examScore = input('What did ' + studentName + ' score on their final exam?\n')

# totalScore = calcFinalScore(homeworkScore, assessmentScore, examScore)
# # print(totalScore)
# print(studentName + " got a " + totalScore[1] + " (" + str(round(totalScore[0],2)) + ").")

'''
https://www.w3resource.com/python-exercises/python-functions-exercises.php
01. Write a Python function to find the Max of three numbers. 
'''
# def maximum(x, y, z):
#     if ( x > y ) and ( x > z ):
#         largest = x
#     elif ( y > x ) and ( y > z ):
#         largest = y
#     else:
#         largest = z
#     return largest
# x = input("1st Number: ")
# y = input("2nd Number: ")
# z = input("3rd Number: ")
# biggest = (maximum(x,y,z))
# print(biggest)

'''
02. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20 
'''
def sumOfNum(*listOfIntegers):
    total = 0
    for x in listOfIntegers:
        total += x
    return total

print(sumOfNum(8, 2, 3, 0, 7))