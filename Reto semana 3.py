import random
t_discount = 0

name = input('Please fill out your name: ')
age = input('Please fill out your age: ')

while age.isnumeric() is False:
    print('Please enter a number')
    age = int(age)
    if age < 15:
        print(f'You mest be at least 15 years old')
        age = int(input('Please fill out your age: '))

salaries = float(input('Please enter the wage of your family: '))
salaries = float(salaries / 865000)

age = int(age)
if age > 25:
    a_discount = 0
if age < 25:
    if 22 <= age <= 25:
        a_discount = 10
    elif 19 <= age <= 21:
         a_discount = 15
    else:
        a_discount = 25


if salaries <= 1:
    s_discount = 30
if 3 < salaries <= 4:
    s_discount = 5
elif 2 < salaries <= 3:
    s_discount = 10
elif 1 < salaries <= 2:
    s_discount = 20
else:
    s_discount = 0


exam_score = random.randint(0,100)

if exam_score < 80:
    e_discount = 0
if 80 <= exam_score < 86:
    e_discount = 30
elif 86 <= exam_score < 91:
    e_discount = 30
elif 91 <= exam_score < 96:
    e_discount = 40
else:
    e_discount = 45

t_discount =  a_discount + s_discount + e_discount

print(f'For the candidate {name}, the total discount is {t_discount}% for the following attributes: age {a_discount}%, salaries {s_discount}%  and for exam score {e_discount}%')

