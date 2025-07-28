class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Students(Person):
    def __init__ (self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def display (self):
        print("Name of the student is :"+str(self.name) +"\n age is :" +str(self.age) +"\n grade  :" +str(self.grade))  
student=Students("Aman",21,3.1)
student.display()