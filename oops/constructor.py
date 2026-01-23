#1. Create a class called Student that has:
# Attributes: name, age, grade
# Method: display_info() to print all details
class Student:
    def __init__(self,name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def display_info(self):
        print(f"name: {self.name} age: {self.age} grade: {self.grade}")
    st1=Student("Anu",15,"A")
    st1.display_info()