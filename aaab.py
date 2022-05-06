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

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#     def speak(self):
#         print("aaaaaaa")

# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color            
#     def speak(self):
#         print("mjal")
        
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and ajm {self.color}")
        
# class Dog(Pet):
#     def speak(self):
#         print("halu")
        
# p = Pet("Tim", 19)
# p.speak()
# c = Cat("bill", 666, "wajt")
# c.show()
# d = Dog("jill", 16)
# d.speak()


# def valuecheck(text):
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     value = 0 
#     for element in text:
#         value += alphabet.index(element) + 1
#     return value
    

# def high(x):
#     x_elements = x.split()
#     listofvalues = []
#     for word in x_elements:
#         functionadd = valuecheck(word)
#         listofvalues.append(functionadd)
#     highestval = sorted(listofvalues)[-1]
#     bestword = listofvalues.index(highestval)
#     print(x_elements[bestword])

# high('man i need a taxi up to ubud')

def timer(seconds):
    if seconds < 60:
        if seconds == 1:
            return "1 second"
        else:
            return f"{seconds} seconds"
    elif seconds >= 60 and seconds < 3600:
        if seconds == 60:
            return "1 minute"
        else:
            minutes = seconds // 60
            seconds = seconds - (minutes * 60)
            if seconds == 1:
                return f"{minutes} minutes and 1 second"
            else:
                return f"{minutes} minutes and {seconds} seconds"
    minutes = seconds // 60
    if minutes >= 60:
        hours = minutes // 60
        if minutes == 60:
            return f"1 hour"
        else:
            minutes = minutes - (hours * 60)
            seconds = seconds % minutes * 60
            return f"{hours} hours, {minutes} minutes and {seconds} seconds"
            
            
def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        time = timer(seconds)
        print(time)
        
        
format_duration(3661)