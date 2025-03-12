# ## 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
from math import pi
class Circle:
    
    def __init__(self,diameter):
        self.diameter = diameter

    def calc_area(self):
        
        return pi * (self.diameter/2)**2

    def calc_perimeter(self):
        return 2 * pi * (self.diameter/2)

circle1 = Circle(12)
# print(circle1.calc_area())
# print(circle1.calc_perimeter())


# ## 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.


from datetime import date, datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        # Convert date_of_birth from string to date object
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    def age_calc(self):
        today = date.today()
        birth_date = self.date_of_birth
        age = today.year - birth_date.year
        if birth_date.month > today.month or (birth_date.month == today.month and birth_date.day > today.day):
            age -= 1
        return age


person1 = Person('Nodir', 'Uzbekistan', '2003-03-18')
# print(person1.age_calc())


# ## 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def addition(self,number1,number2):
        return number1 + number2
    def subtraction(self,number1,number2):
        return number1 - number2
    def multiplication (self,number1,number2):
        return number1 * number2
    def division(self,number1,number2):
        return number1 / number2
    
a = Calculator()
# print(a.addition(50,20))

# ## 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

# class Shape:
#     def calc_area(self,diameter):
#         return pi * (diameter/2)**2

#     def calc_perimeter(self,diameter):
#         return 2 * pi * (diameter/2)
# class Circle(Shape):
    






# class Triangle(Shape):
# class Square(Shape):

# ## 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.






# ## 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# ## 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# ## 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# ## 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

# ## 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# ## 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

