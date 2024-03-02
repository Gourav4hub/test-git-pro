from person import Person
class Faculty(Person):
    def __init__(self, name=None, age=None,facid=None,salary=None):
        super().__init__(name, age)
        self._facid = facid 
        self._salary = salary
    def input(self):
        super().input()
        self._facid = input("FacID : ") 
        self._salary = float(input("Salary : "))
    def show(self):
        super().show()
        print("FacID : " , self._facid)
        print("Salary : " , self._salary)   
    def payTax(self):
        print("Pay Tax !")   