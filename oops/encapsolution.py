#data prodtection
#controlled acess
#code modularity
#data hiding

# class Student: 
#     def __init__(self, name): 
#         self.name = name   # public variable 
# s = Student("Rahul") 
# print(s.name)

#..............product mebers..........
# class Student: 
#     def __init__(self, name, age): 
#         self._age = age     # protected variable 
 
# s = Student("Rahul", 20) 
# print(s._age)
#...........private................
# class Student: 
#     def __init__(self, name, marks): 
#         self.__marks = marks   # private variable 
 
# s = Student("Rahul", 85) 
 
# # print(s.__marks)   # This will give an error

#.................accesing method...........
# class Student: 
#     def __init__(self, marks): 
#         self.__marks = marks 
 
#     def get_marks(self): 
#         return self.__marks 
 
#     def set_marks(self, new_marks): 
#         if new_marks >= 0 and new_marks <= 100: 
#             self.__marks = new_marks 
#         else: 
#             print("Invalid marks") 
 
# s = Student(80) 
 
# print(s.get_marks())      # accessing private data 
# s.set_marks(90)           # modifying private data
