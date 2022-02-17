'''
Importing modules using import
'''

# import samplelib

# print('ok')

# samplelib.ham()
# samplelib.spam()    

'''
Importing modules using from 'module name' import 'function1', 'function2'
'''

from samplelib import spam, ham

print('ok')

ham()
spam()