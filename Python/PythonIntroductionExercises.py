# Errors
# PRINT "Hello World" - needs to be lowercase print and needs parenthesis around the inverted commas
# print(Hello World) - needs inverted commas inside the parenthesis
# Print("Hello World") - capital P needs to be lowercase
# priint("Hello World") - needs to be print, not priint

print( "What is your first name?")
firstname = input()
print ( "What is your family name?")
familyname = input()
print ( "Hello " + firstname + " " + familyname + "!" )

print( "Please enter the first number:" )
number1 = float( input ())
print( "Please enter the second number:" )
number2 = float( input ())
answer = number1 + number2
# print(number1, "+", number2, "=", answer)
print(f"{number1}+{number2}")
# We can use print(f"{variable}") to print the value of the variable.