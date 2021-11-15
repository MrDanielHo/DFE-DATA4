userScore = int(input('What did the student score?\n'))
if userScore > 85 and userScore <= 100:
    print("Distinction")
elif userScore > 65 and userScore <= 85:
    print("Pass")
elif userScore >= 0 and userScore < 65:
    print("Fail")
else:
    print("Please enter a valid score.")