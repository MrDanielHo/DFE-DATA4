from electrical import *
from navigation import *

print(f'''{current()}
{voltage()}
{amps()}
''')

'''
The current output is slow as the last module loaded was navigation.
What we actually wanted was the current 'AC' from electrical

'''