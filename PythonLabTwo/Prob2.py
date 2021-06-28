'''WAP which accepts marks of four subjects and display total marks, percentage and grade.
 Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail'''
marks_eng=float(input('Enter marks in English'))
marks_comp=float(input('Enter marks in Computer'))
marks_maths=float(input('Enter marks in maths'))
marks_sci=float(input('Enter marks in Science'))
total_marks=marks_eng+marks_comp+marks_maths+marks_sci
result=(total_marks/400)*100
print(f'Your total marks is {total_marks}')
if result>=70:
    print('You secured distinction')
    print('Your grade is A')
elif result>=60:
    print('First Division')
    print('Your grade is B')
elif result>=40:
    print('Pass')
    print('Your grade is C')
else:
    print('You failed')