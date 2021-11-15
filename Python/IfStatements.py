userScore = int(input('What did the student score? '))
if type(userScore) == int:
    if int(userScore) > 85:
        print("Distinction")
    elif int(userScore) > 65:
        print("Pass")
    else:
        print("Fail")
else:
    print("Please enter a valid score.")