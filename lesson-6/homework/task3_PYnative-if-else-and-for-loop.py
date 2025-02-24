<<<<<<< HEAD
#Exercise 1 



i = 1
while i<=10:
    print(i)
    i+=1




#Exercise 2



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print('')




#Exercise 3

# my solution
user_number = int(input('enter a number: '))
n = 0
for i in range(1,user_number + 1):
    n+=i
print(n)

# Solution 2: 
n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)




#Exercise 4


num = 2

for i in range(1,11):
    print(num*i)





#Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)



#Exercise 6


n = 758696666
count = 0
while n != 0:
   n = n // 10
   count +=1
print(count)



#Exercise 7

# my solution
line = 5

for i in range(line,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print('')

# second solution
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()



#Exercise 8


list1 = [10, 20, 30, 40, 50,50,12,6565,6454,5]

    # my solution
for i in range(len(list1)-1,-1,-1):
    print(list1[i])

    # second solution

new_list = reversed(list1)
for item in new_list:
    print(item)

#Exercise 9



for i in range(-10,0,1):
    print(i)



#Exercise 10


for i in range(5):
    print(i)
else:
    print('done!')



#Exercise 11


# range
start = 25
end = 50

for i in range(start,end +1):
    # all prime numbers are greater than 1
    if i > 1:    
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)





#Exercise 12


num1 = 0
num2 = 1
for i in range(11):
    fib = num1 + num2
    num1 = num2
    num2 = fib
    print(num1)
        

#Exercise 13


num = 5
fl = 1
for i in range(num,0,-1):
    fl = fl*i
print(fl)



#Exercise 14


num = 76542
rnum = 0
while num != 0:
    digit = num % 10
    num = num//10
    rnum = rnum * 10 + digit
print(rnum)



#Exercise 15

# my soulution
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for n,i in enumerate(my_list):
    if n%2==1:
        print(i, end=' ')

# second solution

# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")




#Exercise 16


input_number = 6
cube = 1
for i in range(1,input_number+1):

    cube = i * i * i
    print('Current Number is :', i,  'and the cube is ', cube)



#Exercise 17

    #  my solution  
n = 5
s = 0

sum = 0
for i in range(1,n+1):
    for j in range(i):
        s = s * 10 + 2
    sum = sum + s
    s = 0
print(sum)

    # second solution
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)




#Exercise 18

# my solution
line = 9
for i in range(1,line + 1):
    if i <=5: #1-5
        for j in range(i):
            print('*', end = ' ')
        print('')
    elif i <= line: #6-9
        i = 10 - i
        for j in range(i):
            print('*', end = ' ')
        print('')

    

# second solution
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
=======
#Exercise 1 



i = 1
while i<=10:
    print(i)
    i+=1




#Exercise 2



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print('')




#Exercise 3

# my solution
user_number = int(input('enter a number: '))
n = 0
for i in range(1,user_number + 1):
    n+=i
print(n)

# Solution 2: 
n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)




#Exercise 4


num = 2

for i in range(1,11):
    print(num*i)





#Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)



#Exercise 6


n = 758696666
count = 0
while n != 0:
   n = n // 10
   count +=1
print(count)



#Exercise 7

# my solution
line = 5

for i in range(line,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print('')

# second solution
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()



#Exercise 8


list1 = [10, 20, 30, 40, 50,50,12,6565,6454,5]

    # my solution
for i in range(len(list1)-1,-1,-1):
    print(list1[i])

    # second solution

new_list = reversed(list1)
for item in new_list:
    print(item)

#Exercise 9



for i in range(-10,0,1):
    print(i)



#Exercise 10


for i in range(5):
    print(i)
else:
    print('done!')



#Exercise 11


# range
start = 25
end = 50

for i in range(start,end +1):
    # all prime numbers are greater than 1
    if i > 1:    
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)





#Exercise 12


num1 = 0
num2 = 1
for i in range(11):
    fib = num1 + num2
    num1 = num2
    num2 = fib
    print(num1)
        

#Exercise 13


num = 5
fl = 1
for i in range(num,0,-1):
    fl = fl*i
print(fl)



#Exercise 14


num = 76542
rnum = 0
while num != 0:
    digit = num % 10
    num = num//10
    rnum = rnum * 10 + digit
print(rnum)



#Exercise 15

# my soulution
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for n,i in enumerate(my_list):
    if n%2==1:
        print(i, end=' ')

# second solution

# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")




#Exercise 16


input_number = 6
cube = 1
for i in range(1,input_number+1):

    cube = i * i * i
    print('Current Number is :', i,  'and the cube is ', cube)



#Exercise 17

    #  my solution  
n = 5
s = 0

sum = 0
for i in range(1,n+1):
    for j in range(i):
        s = s * 10 + 2
    sum = sum + s
    s = 0
print(sum)

    # second solution
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)




#Exercise 18

# my solution
line = 9
for i in range(1,line + 1):
    if i <=5: #1-5
        for j in range(i):
            print('*', end = ' ')
        print('')
    elif i <= line: #6-9
        i = 10 - i
        for j in range(i):
            print('*', end = ' ')
        print('')

    

# second solution
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
    print("\r")