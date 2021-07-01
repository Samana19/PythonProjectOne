'''Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).'''

From=1500
to=2700
for i in range(From, to+1):
    if (i%7==0 and i%5==0):
        print(i)
    