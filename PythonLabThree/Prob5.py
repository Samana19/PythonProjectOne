'''Write a function called show_stars(rows).If rows is 5, it should print the following:
*
**
***
****
***** '''
def show_stars(rows):
    for i in range(1, rows+1):
        for j in range(0 , i):
            print("*", end="")
        print()
show_stars(50)