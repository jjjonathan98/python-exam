# Person class holds the most basic information of a person.
class Person:
    # Constructor to initialize the Person object.
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    # Method to access and print the initialized values from the Person constructor.
    def get_info(self):
        print("Full name:", self.fname, self.lname)
        print("Age:", self.age)


# Student class which is a subclass and inherits from the Person class.
class Student(Person):
    # Constructor to initialize the Student object.
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.student_id = student_id

    # Method to access and print the initialized values from the Student constructor.
    def get_stuinfo(self):
        super().get_info()
        print("Students ID:", self.student_id)


# Employee class, another subclass of the Person class and also inherits from it.
class Employee(Person):
    # Constructor to initialize the Employee object.
    def __init__(self, fname, lname, age, employee_id, salary):
        super().__init__(fname, lname, age)
        self.employee_id = employee_id
        self.salary = salary

    # Method to access and print the initialized values from the Employee constructor.
    def get_empinfo(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# main function to test the implementation.
def main():
    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_stuinfo()

    print("=" * 23)

    new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
    new_employee.get_empinfo()


# Runs the code
main()
