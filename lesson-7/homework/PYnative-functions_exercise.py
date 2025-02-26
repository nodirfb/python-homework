
''''''
# 1 

def person(name,age):
    print(name,age)
person('Nodir',22)




# 2



def func1(*args):
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)





# 3



def calculation(a,b):
    r1 = a - b
    r2 = a + b 
    return r1, r2
    # return a - b,a + b
    
res = calculation(40,10)
print(res)




# 4



def show_employee(name, salary=9000):
    return f'{name}: {salary}'

r1 = show_employee("Ben", 12000)
r2 = show_employee("Jessa")
print(r1,r2)



# 5


def outer(a,b):
    def inner(a,b):
        return a+b
    return inner(a,b) + 5

res = outer(5,5)
print(res)





# 6


def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)





# 7



def display_student(name,age):
    print(name,age)

show_student = display_student

show_student('emma', 23)





# 8




def even_num(start,stop):
    for i in range(start,stop, 2):
        print(i)

even_num(4,30)


print(list(range(4,30,2)))

# 9

x = [4, 6, 8, 24, 12, 2]
print(max(x))








