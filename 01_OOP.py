class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        
    def display_info(self):
        print(f"Student Name : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        

student1 = Student(name="Shahwar", roll_number=47)
student2 = Student(name="Alam", roll_number=3)
        
student1.display_info()
student2.display_info()

