a=int(input('Enter the students in class a'))
b=int(input('Enter the students in class b'))
c=int(input('Enter the students in class c'))
inclassa=a//2
print (f'the num of desk in class a is {inclassa}')
inclassb=b//2
print (f'the num of desk in class a is {inclassb}')
inclassc=c//2
print (f'the num of desk in class a is {inclassc}')
rema=a%2
print (f'the num of  rem desk in class a is {rema}')
remb=b%2
print (f'the num of  rem desk in class a is {remb}')
remc=c%2
print (f'the num of  rem desk in class a is {remc}')
total=inclassa+inclassb+inclassc+rema+remb+remc

print(f'Num of desks is {total}')