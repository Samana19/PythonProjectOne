''' Given three integers, print the smallest one. (Three integers should be user input)
'''
Num1=int(input('First integer'))
Num2=int(input('Second integer'))
Num3=int(input('Third integer'))
if Num1<Num2<Num3 :
    print(f'{Num1} is smallest')
elif Num2<Num1<Num3:
    print(f'{Num2} is smallest')
else:
    print(f'{Num3}is smallest')
