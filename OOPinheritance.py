class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age


class Students(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade  
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        self.__grade = grade
    def display(self):
        print("Name of the student is: " + self.get_name())
        print("Age is: " + str(self.get_age()))
        print("Grade: " + str(self.get_grade()))

student = Students("Aman", 21, 3.1)
student.display()
