'''
Tutorial 1
Now when you run the program it will show the line, a = "aaa". If you try entering p a, you will get an error as you have to pass the line for the variable to be defined so type in n and press enter. Then try p a again, you should get a return of 'aaa'.

Now if you type q and press enter you will quit the program.

Now run the program again go the final line by typing n and enter repeatedly. Now type p final and you should get aaabbbccc returned.
'''
# import pdb

# pdb.set_trace()

# a = "aaa"
# b = "bbb"
# c = "ccc"

# final = a + b + c
# print(final)
'''
Tutorial 2
Note: pdb.set_trace() will not trace within functions unless it is called within the function's block of code:
'''
# import pdb
# a = "aaa"
# b = "bbb"
# c = "ccc"

# def final(var1,var2,var3):
#     pdb.set_trace()
#     return(var1+var2+var3)

# print(final(a,b,c))
'''
Exercise 1
Debug the following programs.
For the first 2 perform static analysis.
For the 3rd and 4th exercises use dynamic analysis either manually or through PDB.
'''
# import pdb
# pdb.set_trace()

# price = {"Burger":9.95,"Fries":4.45}
# user_funds = 10.31
# item_price = price["Burger"]
# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds:
#     print("Sorry you don't have enough money")
'''
Exercise 2
'''
# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))
'''
Exercise 3
The only even prime number is 2.
    All other even numbers can be divided by 2.

If the sum of a number's digits is a multiple of 3,
    that number can be divided by 3.

No prime number greater than 5 ends in a 5.
    Any number greater than 5 that ends in a 5 can be divided by 5.

Zero and 1 are not considered prime numbers.
    Except for 0 and 1, a number is either a prime number or a composite number. A composite number is defined as any number, greater than 1, that is not prime.

Test the is_prime function with 2, 3, 4, 5, 6, 7, 15, 20 & 25
'''
# import pdb
# pdb.set_trace()

# def is_prime(x):
#     if x < 2:
#         return True
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#     return True
# print(is_prime(61))
'''
Exercise 4
'''
# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n < 5:
#     n += 1
#     for i in item_list:
#         print(i)
# print(item_list[4])