'''Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter)'''
def sum_of_multiples(limit):
    summ=0
    for i in range(1,limit+1):
        if i%3 or i%5==0:
            summ=+i
    print(summ)
sum_of_multiples(20)