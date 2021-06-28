'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.'''
def string(s):
    up = sum(1 for i in s if i.isupper())
    low = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (up,low))

string("HeLlO WoRld")