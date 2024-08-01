# __init__
# class Student:
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age
        

#  __str__
# class Student:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __str__(self) -> str:
#         return f"Student(name={self.name} age={self.age})"

# student1 = Student(name="Shahwar", age="26")
# print(student1)


# __repr__

        
# class Student:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __repr__(self) -> str:
#         return f"Student(name={self.name} age={self.age})"

# student1 = Student(name="Shahwar", age="26")
# print(student1)



# __len__

# class MyList:
#     def __init__(self, incoming_list) -> None:
#         self.incoming_list = incoming_list
        
#     def __len__(self):
#         return len(self.incoming_list)
    
# sending_list = MyList([1,2,3,4])
# print(len(sending_list))


# __getitem__

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

# my_list = MyList([1, 2, 3])
# print(my_list[1]) 

# __setitem__

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __setitem__(self, index, value):
#         self.items[index] = value

# my_list = MyList([1, 2, 3])
# my_list[1] = 10
# print(my_list.items) 


# __delitem__

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __delitem__(self, index):
#         del self.items[index]

# my_list = MyList([1, 2, 3])
# del my_list[1]
# print(my_list.items)  


# iter

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __iter__(self):
#         return iter(self.items)

# my_list = MyList([1, 2, 3])
# for item in my_list:
#     print(item)



# call

class Greet:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}!")

greet = Greet("Shahwar")
greet() 

