'''8. Given a three-digit number. Find the sum of its digits.
'''
num=int(input("Enter a number: "))
a = num // 100
b = num // 10 % 10
c = num % 10
sum_of_digits=a + b + c
print(f'Sum of digits is : {sum_of_digits}')
