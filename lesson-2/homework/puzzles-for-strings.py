<<<<<<< HEAD


#1


st = input('Input a string: ')
stlength = len(st)
print(stlength)


#2



st = input('Input a string: ')

first2 = st[0:2]
last2 = st[::-1][0:2][::-1]
print(f'{first2}{last2}')



#3


str = 'valailavalavalaaxlavala'

first_str_value = str[0]
#print(first_str_value)

replace = str.replace(first_str_value,'$')
#print(replace)

filnal_str = f'{first_str_value}{replace[1:]}'
print(filnal_str)



#4



# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str1 = 'alfa'
str2 = 'betta'

result = (f'{str2[0:2]}{str1[2:]} {str1[0:2]}{str2[2:]}')
print(result)



#5



index = int(input('Input an index: '))

str = 'nodir'  

len(str)

if index > len(str)-1:
    print('Your input index is higher than the string\'s max index!')

first_part = str[:index]
second_part = str[index+1:]

result = f'{first_part}{second_part}'
print(result)


#6


str = 'terminator'

middle_part = str[1:len(str)-1]
left_part = str[len(str)-1]
right_part = str[0]
exchanged = f'{left_part}{middle_part}{right_part}'

print(exchanged)


#7



sentence = 'Welcome to our hotlel. Nice to meet you. tomorrow.. you '
word = 'to'

print(sentence.count(word))


#8


text = input('Input smth: ')

print(text.upper())
print(text.lower())


#9


str = input('Write smth: ')
last_2char = str[len(str)-2:]

print(last_2char * 4)


#10


str = input('Write smth: ')

result = str[:3]
print(result)



#11



str = input('Write smth: ')
print(str[::-1])


#12



str = 'oltin'
character = 'ol'

result = str.startswith(character)
print(result)


















=======


#1


st = input('Input a string: ')
stlength = len(st)
print(stlength)


#2



st = input('Input a string: ')

first2 = st[0:2]
last2 = st[::-1][0:2][::-1]
print(f'{first2}{last2}')



#3


str = 'valailavalavalaaxlavala'

first_str_value = str[0]
#print(first_str_value)

replace = str.replace(first_str_value,'$')
#print(replace)

filnal_str = f'{first_str_value}{replace[1:]}'
print(filnal_str)



#4



# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str1 = 'alfa'
str2 = 'betta'

result = (f'{str2[0:2]}{str1[2:]} {str1[0:2]}{str2[2:]}')
print(result)



#5



index = int(input('Input an index: '))

str = 'nodir'  

len(str)

if index > len(str)-1:
    print('Your input index is higher than the string\'s max index!')

first_part = str[:index]
second_part = str[index+1:]

result = f'{first_part}{second_part}'
print(result)


#6


str = 'terminator'

middle_part = str[1:len(str)-1]
left_part = str[len(str)-1]
right_part = str[0]
exchanged = f'{left_part}{middle_part}{right_part}'

print(exchanged)


#7



sentence = 'Welcome to our hotlel. Nice to meet you. tomorrow.. you '
word = 'to'

print(sentence.count(word))


#8


text = input('Input smth: ')

print(text.upper())
print(text.lower())


#9


str = input('Write smth: ')
last_2char = str[len(str)-2:]

print(last_2char * 4)


#10


str = input('Write smth: ')

result = str[:3]
print(result)



#11



str = input('Write smth: ')
print(str[::-1])


#12



str = 'oltin'
character = 'ol'

result = str.startswith(character)
print(result)


















>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
