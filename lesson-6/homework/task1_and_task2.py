<<<<<<< HEAD

#  1----------------------------------------------------

list1 = [1,1,2]
list2 = [2,3,4]

# list1 = [1,2,3]
# list2 = [4,5,6]

# list1 = [1,1,2,3,4,2]
# list2 = [1,3,4,5]
def uncommon_element_list(l1,l2):
    list3 = []
    for i in l1:
        if i not in l2:
            list3.append(i)
    for i in l2:
        if i not in l1:
            list3.append(i)
    return list3

print(uncommon_element_list(list1, list2))


#  2----------------------------------------------------

# put underscore after index 2
# if the sign is vowel or is there underscore behind it,
    # the underscore will putted after next sign
# if the sign is the last sign of string, don't put the underscore 


txt = 'abcabcdabcdeabcdefabcdefg'
last_index = len(txt) - 1

vowels = ['a','e','i','o','u','A','E','I','O','U']
r = ''
und = []

n = 1
for j, i in enumerate(txt):
    
    r = r + i

    if n % 3 == 0:
        if i in vowels or i in und:
            n = n-1
        else:
            und.append(i)
            if j != last_index:
                r = r + '_'
    n += 1

print(r)
    


=======

#  1----------------------------------------------------

list1 = [1,1,2]
list2 = [2,3,4]

# list1 = [1,2,3]
# list2 = [4,5,6]

# list1 = [1,1,2,3,4,2]
# list2 = [1,3,4,5]
def uncommon_element_list(l1,l2):
    list3 = []
    for i in l1:
        if i not in l2:
            list3.append(i)
    for i in l2:
        if i not in l1:
            list3.append(i)
    return list3

print(uncommon_element_list(list1, list2))


#  2----------------------------------------------------

# put underscore after index 2
# if the sign is vowel or is there underscore behind it,
    # the underscore will putted after next sign
# if the sign is the last sign of string, don't put the underscore 


txt = 'abcabcdabcdeabcdefabcdefg'
last_index = len(txt) - 1

vowels = ['a','e','i','o','u','A','E','I','O','U']
r = ''
und = []

n = 1
for j, i in enumerate(txt):
    
    r = r + i

    if n % 3 == 0:
        if i in vowels or i in und:
            n = n-1
        else:
            und.append(i)
            if j != last_index:
                r = r + '_'
    n += 1

print(r)
    


>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
