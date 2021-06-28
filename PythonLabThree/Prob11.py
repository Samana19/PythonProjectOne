'''Write a program to find the factorial of a number using functions.'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number : "))
print(factorial(n))