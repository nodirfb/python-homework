<<<<<<< HEAD

#Homework1:-----------------------------------------------------------
#1

cardinal_numbers = ('first', 'secon', 'third')

#2
print(cardinal_numbers[1])

#3
position1, position2, position3 = cardinal_numbers[0],cardinal_numbers[1],cardinal_numbers[2]
print(position1)
print(position2)
print(position3)

#4

my_name = tuple(('n','o','d','i','r'))
print((type(my_name)))

#5

if 'x' in my_name:
    print("yes")
else: 
    print("no")

#6

new_name = my_name[1:]
print(new_name)
print(type(new_name))

#Homework2:-----------------------------------------------------------


food = ['rice', 'beans']

food.append('broccoli')
print(food)

food.extend(['bread','pizza'])
print(food)

print(food[:2])

print(food[-1])

breakfast = "eggs, fruit, orange juice".split(', ')
print(breakfast)
print(type(breakfast))

print(len(breakfast))

#8

lengths = [len(breakfast[0]) for x in breakfast]

print(lengths)


#Homework3:-----------------------------------------------------------

#1
list = [4,2,4,6,7,5,8,8,5,3,1]
list.sort()
print(list[0])
#2

#Expected Output : ['Green', 'White', 'Black']
#removing the 0th, 4th and 5th elements.


colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del colors[0],colors[4-1],colors[5-2]
print(colors)


# 3. Write a Python program to calculate the difference between the two lists

list1 = ['a','b','d']
list2 = ['a','b','c']

list3 = set(list1).symmetric_difference(set(list2))

print(list3)


# 4. Write a Python program to find the index of an item in a specified list. 


list1 = ['d','a','d',1,3,'a',2,]

r = list1.index('a')

print(r)


# 5. Write a Python program to append a list to the second list.


list1 = ['a','b','d']
list2 = ['a','b','c']


list1.append(list2)
print(list1)



# 6. Write a Python program to find the second smallest number in a list.


list = [4,2,4,6,7,5,8,8,5,3,1]

list.sort()
print(list[1])



# 7. Write a Python program to find common items in two lists.

list1 = ['a','b',2,1,'d',5,'g','r',3,'n']
list2 = ['a','b',3,'g','c','d',2,1]

list3 = [i for i in list1 if i in list2]
print(list3)


# 8. Write a Python program to split a list into different variables


list = [4,2,4,6]

a,b,c,d = list
print(a,b,c,d)



# 9. Write a Python program to select the odd items from a list

list = [4,2,4,6,7,5,8,8,5,3,1]

list2 = [i for i in list if i%2!=0]
print(list2)




# 10. Write a Python program to replace the last element in a list with another list.
# Sample data : 
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

def list_element_replacer(l1,l2):
    l1.pop()
    l1.extend(l2)
    return l1
res = list_element_replacer(list1,list2)
print(res)


=======

#Homework1:-----------------------------------------------------------
#1

cardinal_numbers = ('first', 'secon', 'third')

#2
print(cardinal_numbers[1])

#3
position1, position2, position3 = cardinal_numbers[0],cardinal_numbers[1],cardinal_numbers[2]
print(position1)
print(position2)
print(position3)

#4

my_name = tuple(('n','o','d','i','r'))
print((type(my_name)))

#5

if 'x' in my_name:
    print("yes")
else: 
    print("no")

#6

new_name = my_name[1:]
print(new_name)
print(type(new_name))

#Homework2:-----------------------------------------------------------


food = ['rice', 'beans']

food.append('broccoli')
print(food)

food.extend(['bread','pizza'])
print(food)

print(food[:2])

print(food[-1])

breakfast = "eggs, fruit, orange juice".split(', ')
print(breakfast)
print(type(breakfast))

print(len(breakfast))

#8

lengths = [len(breakfast[0]) for x in breakfast]

print(lengths)


#Homework3:-----------------------------------------------------------

#1
list = [4,2,4,6,7,5,8,8,5,3,1]
list.sort()
print(list[0])
#2

#Expected Output : ['Green', 'White', 'Black']
#removing the 0th, 4th and 5th elements.


colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

del colors[0],colors[4-1],colors[5-2]
print(colors)


# 3. Write a Python program to calculate the difference between the two lists

list1 = ['a','b','d']
list2 = ['a','b','c']

list3 = set(list1).symmetric_difference(set(list2))

print(list3)


# 4. Write a Python program to find the index of an item in a specified list. 


list1 = ['d','a','d',1,3,'a',2,]

r = list1.index('a')

print(r)


# 5. Write a Python program to append a list to the second list.


list1 = ['a','b','d']
list2 = ['a','b','c']


list1.append(list2)
print(list1)



# 6. Write a Python program to find the second smallest number in a list.


list = [4,2,4,6,7,5,8,8,5,3,1]

list.sort()
print(list[1])



# 7. Write a Python program to find common items in two lists.

list1 = ['a','b',2,1,'d',5,'g','r',3,'n']
list2 = ['a','b',3,'g','c','d',2,1]

list3 = [i for i in list1 if i in list2]
print(list3)


# 8. Write a Python program to split a list into different variables


list = [4,2,4,6]

a,b,c,d = list
print(a,b,c,d)



# 9. Write a Python program to select the odd items from a list

list = [4,2,4,6,7,5,8,8,5,3,1]

list2 = [i for i in list if i%2!=0]
print(list2)




# 10. Write a Python program to replace the last element in a list with another list.
# Sample data : 
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

def list_element_replacer(l1,l2):
    l1.pop()
    l1.extend(l2)
    return l1
res = list_element_replacer(list1,list2)
print(res)


>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
