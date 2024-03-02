from student import Student
from faculty import Faculty

# ob1 = Student("Vikas",21,"3242",321.12)
# ob1.show()
# ob2 = Faculty("Rajesh",29,"12wse",23321)
# ob2.show()

ob1 = Student()
ob2 = Faculty()

ob1.input()
ob2.input()

ob1.show()
ob1.giveExam()

ob2.show()
ob2.payTax()