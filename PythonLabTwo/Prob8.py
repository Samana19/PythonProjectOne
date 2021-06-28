'''8. Given a three-digit number. Find the sum of its digits.
'''
n=int(input("Enter a number: "))
sum=0
while(n>0):
    digit=n%10
     summ=sum+digit
    n=n//10
print("The total sum of digits is:",)
