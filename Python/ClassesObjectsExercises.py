'''
QA Community Exercise
In a new Python file, create a class of students.
It should contain the following attributes: name, age, and class with default value "student".
It should also contain a method which takes in 3 test scores and prints the students average test score.
'''
# class Student:
#     def __init__(self, name, age, classification = "student"):
#         self.name = name
#         self.age = age
#         self.classification = classification

#     def avgScore(self, test1, test2, test3):
#         self.test1 = test1
#         self.test2 = test2
#         self.test3 = test3
#         return((test1 + test2 + test3) / 3)

# John = Student("John", "21")
# JohnScore = John.avgScore(80, 70, 66)

# Jane = Student("Jane", "22")
# JaneScore = Jane.avgScore(90, 88, 71)

# print(f"{John.name} scored an average of {JohnScore})
# print(f"{Jane.name} scored an average of {JaneScore})
'''
https://towardsdatascience.com/3-useful-projects-to-learn-python-classes-cf0076c36297
1. Budget App
Goal:
“Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
- Create Class that will make a few objects
- catag1 = Class()
- catag2 = Class()
  - catag = food clothing etc

These objects should allow for depositing and withdrawing funds from each category, 
- Action, therefore we need to write methods
  def deposit

as well computing category balances and 
- Classes arfe not just for code, they are also data! Therefore a balance variable
- all transactions must use the balance var

transferring balance amounts between categories”
- what do we need?
 -- from catag name - this is the object we created
 -- to catag name - this is the deposit method in another class object
 -- balance amount

Considerations:
This is a very interesting project as it allows not only to comprehend how a class is initialized and used, but also represented and used as input to other functions.
You will learn how to add methods to your classes and print them in a way that allows complex representation of your class object at different points in the program.
As a bonus, you will define a function that computes how much money you are spending across class categories as a % of your total expenses, something that can be very useful for the money-savvy programmers among you.

Approach:
Define the purpose and flexibility of a class object; 
    build its class methods using a modular approach,
    and develop an understanding for how different instances of the same class can interact.

Key concepts:
Class initialization, instance methods and instance representation.
    Defining and using functions that take class instances as input parameters
'''
class Budget:
    def __init__(self):
        self.balance = 0.0
    def deposit(self,moneyIn):
        self.balance += moneyIn
    def withdraw(self,moneyOut):
        self.balance -= moneyOut
    def transferTo(self,account,moneyTrsf):
        self.withdraw(moneyTrsf)
        account.deposit(moneyTrsf)

food = Budget()
clothes = Budget()
entertainment = Budget()

food.deposit(100)
clothes.deposit(100)
entertainment.deposit(80)

food.withdraw(30) # Groceries
clothes.withdraw(50) # Pair of jeans
entertainment.withdraw(20) # Cinema ticket

print(f"Food balance:\t|\tClothes balance:\t|\tEntertainment balance:\n\t{food.balance}\t|\t\t{clothes.balance}\t\t|\t\t\t{entertainment.balance}\n")

entertainment.transferTo(food, 30)

print(f"Food balance:\t|\tClothes balance:\t|\tEntertainment balance:\n\t{food.balance}\t|\t\t{clothes.balance}\t\t|\t\t\t{entertainment.balance}\n")
