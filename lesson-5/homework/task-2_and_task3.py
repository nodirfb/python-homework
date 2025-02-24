<<<<<<< HEAD
#1

is_known_SQL = input('eneter "yes" if you know SQL else "no": ').lower()
is_known_python = input('eneter "yes" if you know python else "no": ').lower()

if is_known_SQL == 'yes':
    if is_known_python == 'yes':
        print('You can be BI developer')
    else:
        print('you can be data analyst')
elif is_known_python == 'yes':
    print('you can be data engineer')
else: 
    print('learn sql or python')



#2
# A year is a leap year if it is evenly divisible by four, except for years that are divisible by 100 but not by 400.

# For example, 2000 was a leap year, but 1700, 1800, and 1900 were not. The next year that will not be a leap year is 2100. 


year = int(input('Input a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('a leap year')
        else:
            print('not a leap year')
    else:
        print('a leap year')
else:
    print('not a leap year')
=======
#1

is_known_SQL = input('eneter "yes" if you know SQL else "no": ').lower()
is_known_python = input('eneter "yes" if you know python else "no": ').lower()

if is_known_SQL == 'yes':
    if is_known_python == 'yes':
        print('You can be BI developer')
    else:
        print('you can be data analyst')
elif is_known_python == 'yes':
    print('you can be data engineer')
else: 
    print('learn sql or python')



#2
# A year is a leap year if it is evenly divisible by four, except for years that are divisible by 100 but not by 400.

# For example, 2000 was a leap year, but 1700, 1800, and 1900 were not. The next year that will not be a leap year is 2100. 


year = int(input('Input a year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('a leap year')
        else:
            print('not a leap year')
    else:
        print('a leap year')
else:
    print('not a leap year')
>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
