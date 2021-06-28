'''
Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
Weight=float(input('Enter your weight'))
unit= input('Kgs or lbs?')
pound_to_kg=float(Weight/2.2046)
kg_to_pound=float(Weight*2.2046)
if unit=="Kgs":
    print(f'Your weight is {kg_to_pound} lbs')
elif unit=="lbs":
    print(f'Your weight is {pound_to_kg} Kgs')
else:
    print('Your unit is invalid. Try again')