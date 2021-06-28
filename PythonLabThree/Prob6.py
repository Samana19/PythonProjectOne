'''Write a Python program to reverse a string'''
def string(a):

    rev_a = ''
    length = len(a)
    while length > 0:
        rev_a += a[ length - 1 ]
        length = length - 1
    return rev_a
print(string('Hello World'))