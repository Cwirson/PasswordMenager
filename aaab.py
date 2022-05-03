# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def get_grade(self):
#         return self.grade
    
# class Course:
#     def __init__(self, name, max):
#         self.name = name
#         self.max = max
#         self.students = []
#     def add_student(self, student):
#         if self.max > len(self.students):
#             self.students.append(student)
#             print(True)
#         else:
#             print(False)
#     def grade_avr(self):
#         value = 0
#         for x in self.students:
#             value += x.get_grade()
#         return value / len(self.students)
        
# st1 = Student("kutasiarz", 14, 96)
# st2 = Student("sawicki", 15, 99)
# st3 = Student("sobczak", 14, 69)
# course = Course("englisz", 2)
# course.add_student(st1)
# course.add_student(st2)
# course.add_student(st3)
# print(course.students)
# print(course.grade_avr())

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("aaaaaaa")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color            
    def speak(self):
        print("mjal")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and ajm {self.color}")
        
class Dog(Pet):
    def speak(self):
        print("halu")
        
p = Pet("Tim", 19)
p.speak()
c = Cat("bill", 666, "wajt")
c.show()
d = Dog("jill", 16)
d.speak()