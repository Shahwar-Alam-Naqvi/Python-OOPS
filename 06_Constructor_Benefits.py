# 1.OBJECT INITIALIZATION
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object creation
person1 = Person("Ahmed", 30)
person2 = Person("Sara", 25)

# Accessing the attributes
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")


# 2.CODE READABILITY
# LESS READABLE
class Student:
    pass

# Object creation
student1 = Student()
student1.name = "Ali"
student1.age = 20

student2 = Student()
student2.name = "Aisha"
student2.age = 22

# Displaying information
print(f"Name: {student1.name}, Age: {student1.age}")
print(f"Name: {student2.name}, Age: {student2.age}")


# 2.CODE READABILITY
# MORE READABLE

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object creation
student1 = Student("Ali", 20)
student2 = Student("Aisha", 22)

# Displaying information
print(f"Name: {student1.name}, Age: {student1.age}")
print(f"Name: {student2.name}, Age: {student2.age}")


# 3.DEFAULT VALUES

class Car:
    def __init__(self, model, year=2020):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}")

# Object creation with default year
car1 = Car("Toyota")
car2 = Car("Honda", 2022)

# Displaying information
car1.display_info()
car2.display_info()

# 4. Encapsulation 
# Check File : 08_Encapsulation_in_Constructor.py
