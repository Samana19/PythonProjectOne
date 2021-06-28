'''Given a positive real number, print its fractional part.
'''
num=float(input('Enter a positive real number: '))
integer=int(num)
fraction=num-int(num)
print(f'The fractional part is {fraction}')