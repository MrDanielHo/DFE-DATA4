'''
In the following example, assume we have a file called "filename.txt" which has 10 lines in it.
We only want to keep the even lines, so discard the odd ones.
'''
# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()
'''
The outfile is the variable in which we are storing the data we wish to keep.
The readline in the else statement skips the lines which are odd.
'''


'''
QA Community Exercise Part 1a
Create a Python file which does the following:
    Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
'''
file = open("teams.txt", "w")

# newline = 'Red Socks \nTeam Rocket \nTeam Edward \nMicrosoft Teams \nRedbull Racing'
teamlist = ["Red Socks", "Team Rocket", "Team Edward", "Microsoft Teams", "Redbull Racing"]
newline = ''
for i in teamlist:
    newline = newline + i + '\n'
file.write(newline)

file.close()
'''
QA Community Exercise Part 1b
Create a Python file which does the following:
    Reads and displays the names of the 1st and 4th team in the file.
'''
# file = open("teams.txt", "r")
# chars = file.readlines()

# for i in range(5):
#     print(chars[0]+chars[2])

# file.seek(0)
# print(chars[0],end="")
# print(chars[3],end="")

# file.close()
'''
Create a new Python file which does the following:
    Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
    Print out the edited file line by line.
'''
file = open("teams.txt", "r")

outfile = ""

for line in range (1,5):
    outfile += file.readline()
    
file = open("teams.txt", "w")
file.write("This is a new line\n")
file.write(outfile)
file.close()
