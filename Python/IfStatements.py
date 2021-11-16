# Scoring Exercise
# userScore = int(input('What did the student score?\n'))
# if userScore > 85 and userScore <= 100:
#     print("Distinction")
# elif userScore > 65 and userScore <= 85:
#     print("Pass")
# elif userScore >= 0 and userScore < 65:
#     print("Fail")
# else:
#     print("Please enter a valid score.")
'''
Exercise 34: Even or Odd?
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd
'''
# intCheck = int(input("Please enter a number:\n"))
# if intCheck % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
'''
Exercise 35: Dog Years
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
'''
# humanYears = float(input("What is your age?\n"))
# if humanYears >= 1:
#     print("You are " + str( int( 10.5 + (humanYears - 2) * 4 ) ) + " in dog years.")
# else:
#     print("You are a dog.")
'''
Exercise 36:Vowel or Consonant
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant
'''
# letterCheck = str(input('Please enter a letter:\n'))
# lowerCheck = letterCheck.lower()
# if lowerCheck in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")
'''
Exercise 37:Name that Shape
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message
'''
# shape = int(input('Please enter a shape contains between 3 and 10 sides:\n'))
# if shape <= 10 and shape >= 3:
#     if shape == 3:
#         print('Triangle')
#     elif shape == 4:
#         print('Square')
#     elif shape == 5:
#         print('Pentagon')
#     elif shape == 6:
#         print('Hexagon')
#     elif shape == 7:
#         print('Heptagon')
#     elif shape == 8:
#         print('Octagon')
#     elif shape == 9:
#         print('Nonagon')
#     elif shape == 10:
#         print('Decagon')
# else:
#     print('Please enter a shape containing 3-10 sides.')
'''
Exercise 38:Month Name to Number of Days
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
    January – 31 days
    February – 28 days or 29 days
    March – 31 days
    April – 30 days
    May – 31 days
    June – 30 days
    July – 31 days
    August – 31 days
    September – 30 days
    October – 31 days
    November – 30 days
    December – 31 days
'''
# thirtyone = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
# month = str(input('Please enter a Month:\n'))[0:3].lower()
# if month == 'feb':
#     print('28 or 29')
# elif month in thirtyone:
#     print('31')
# else:
#     print (30)
'''
Exercise 39:Sound Levels
+---------------+----------------+
|Noise          |Decibel lv (dB) |
|---------------+----------------|
|Jackhammer     |             130|
|Gas lawnmower  |             106|
|Alarm clock    |              70|
|Quiet room     |               4|
+---------------+----------------+
The following table lists the sound level in decibels for several common noises.
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
'''
# listeningLevel = int(input('What is the current noise level?\n'))
# if listeningLevel > 130:
#     print('This is louder than a Jet engine!')
# elif listeningLevel > 106:
#     print('This is as loud as a Jackhammer.')
# elif listeningLevel > 70:
#     print('This is as loud as an Alarm clock.')
# elif listeningLevel > 40:
#     print('This is a quiet room.')
# else:
#     print('This is as loud as a whisper.')
'''
Exercise 40:Name thatTriangle
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle
'''
# side1 = int(input('What is the length a side of the triangle?\n'))
# side2 = int(input('What is the length another side of the triangle?\n'))
# side3 = int(input('What is the length the last side the triangle?\n'))
# if side1 == side2 and side2 == side3:
#     print('That is an equilateral triangle.')
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print('That is an isosceles triangle.')
# else:
#     print('That is an scalene triangle.')
'''
Exercise 41:NoteTo Frequency
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
Note    Frequency (Hz)
C4      261.63
D4      293.66
E4      329.63
F4      349.23
G4      392.00
A4      440.00
B4      493.88
Begin by writing a program that reads the name of a note from the user and
displays the note's frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes inadjacent octaves. Inparticular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement.
'''
# listeningNote = str(input('Please enter a note: (A-G)\n')).upper()
# listeningOctv = float(input('And in which octave? (0-8)\n'))
# if listeningNote == 'C':
#     print('The frequency is ' + str( 261.63 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'D':
#     print('The frequency is ' + str( 293.66 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'E':
#     print('The frequency is ' + str( 329.63 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'F':
#     print('The frequency is ' + str( 349.23 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'G':
#     print('The frequency is ' + str( 392.00 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'A':
#     print('The frequency is ' + str( 440.00 / 2**(4-listeningOctv)) + ' Hz.')
# elif listeningNote == 'B':
#     print('The frequency is ' + str( 493.88 / 2**(4-listeningOctv)) + ' Hz.')
'''
Exercise 42:Frequency To Note

Inthepreviousquestionyouconvertedfromnotenametofrequency.Inthisquestion
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.

Note    Frequency (Hz)
C4      261.63
D4      293.66
E4      329.63
F4      349.23
G4      392.00
A4      440.00
B4      493.88
'''
# listeningFreq = float(input('Please enter a frequency between 260 Hz and 494 Hz:\n'))
# if (listeningFreq >= 260) or (listeningFreq <= 262):
#     print('That is C4 (middle C)')
# elif (listeningFreq >= 292) or (listeningFreq <= 294):
#     print('That is D4')
# elif (listeningFreq >= 328) or (listeningFreq <= 330):
#     print('That is E4')
# elif (listeningFreq >= 348) or (listeningFreq <= 349):
#     print('That is F4')
# elif (listeningFreq >= 391) or (listeningFreq <= 393):
#     print('That is G4')
# elif (listeningFreq >= 439) or (listeningFreq <= 441):
#     print('That is A4')
# elif (listeningFreq >= 492) or (listeningFreq <= 494):
#     print('That is B4')