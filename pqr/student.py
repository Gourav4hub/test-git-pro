from person import Person
class Student(Person):
    def __init__(self, name=None, age=None,roll=None,marks=None):
        super().__init__(name, age)
        self._roll = roll 
        self._marks = marks
   
    def show(self):
        super().show()
        print("Roll Number: " , self._roll)
        print("Marks : " , self._marks) 
    def giveExam(self):
        print("Exam Given !")         