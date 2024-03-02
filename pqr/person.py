class Person:
    def __init__(self,name=None,age=None):
        self._name = name 
        self._age = age
    def input(self):
        self._name = input("Name : ") 
        self._age = int(input("Age : "))
    def show(self):
        print("\nName : " , self._name)
        print("Age : " , self._age)        