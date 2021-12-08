import numpy as np

# ages_list = [10, 5, 8, 32, 65 ,43, 90, 100]
# ages = np.array([ages_list])
# ages = ages.reshape(2, 4)
# print(ages)
# print ("Size:\t", ages.size) # Total number of entries
# print ("Shape:\t", ages.shape) # the number of rows and columns
# print ("Data Type:\t", ages.dtype)

'''
Exercise
1) Generate a 1D numpy array with the values [7, 9, 65, 33, 85, 99]
2) Generate a matrix (2D numpy array) of the vaues:
        (1 2 4)
    A = (2 3 0)
        (0 5 1)

- Change the dimensions of this array to another permitted shape

3) Run the below code and attempt to reshape the data array to the correct format:
    c1 = np.random.randint(0,110,50)
    c2 = np.random.rand(50)
    c3 = np.random.choice(['french', 'english'], 50)
    data = np.column_stack((c1, c2, c3)).flatten()
'''

# c1 = np.random.randint(0,110,50)
# c2 = np.random.rand(50)
# c3 = np.random.choice(['french', 'english'], 50)
# data = np.column_stack((c1, c2, c3)).flatten()

# exe1 = np.array([7, 9, 65, 33, 85, 99])
# print(exe1)

# exe2 = np.array(
#     [[1, 2, 4,],
#     [2, 3, 0],
#     [0, 5, 1]]
# )
# print(exe2)

# exe2 = exe2.reshape(9,1)
# print(exe2)

# print(data.reshape(int(data.size/3),3))

# numpy.arange() stores beginnning value, ending value, and step only.
# print(np.arange(0,55,5)) 

# numpy.linspace() gives you linear data points on a line
# print(np.linspace(0, 100, 25))

# numpy.repeat
# print(np.repeat(2,10))

identityMatrix = np.eye(3)
print(identityMatrix)

# list1 = []
# for i in range(50):
#     list1.append(i * 0.75)
# print(list1)

# list2 = ([i * 0.75 for i in range(50)])
# print(list2)

'''
Both the below scripts produces the multiples of 5 up to 50.

The For loop does not allow interactions between lists and integers. 

numpy.arange() allows us to perform operations over the array.
'''

# fiveTimesTable = [i * 5 for i in range(11)]
# fiveTimesTable = np.arange(0, 55, 5)
# print(f"0: {fiveTimesTable}")
# print(f"1: {2 * fiveTimesTable}")
# print(f"2: {10 + fiveTimesTable}")
# print(f"3: {fiveTimesTable - 1}")
# print(f"4: {fiveTimesTable / 5}")
# print(f"5: {fiveTimesTable ** 2}")
# print(f"6: {fiveTimesTable < 20}")
# print(f"7: {fiveTimesTable[~(fiveTimesTable > 20)]}")