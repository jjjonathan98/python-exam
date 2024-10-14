# A) Define the student class.
class Student:
    # Class variable that determines the passing mark.
    passing_mark = 60

    # Constructor to initialize the Student object.
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    # A method for string representation of the student object.
    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

    # B) Instance method to determine pass or fail.
    def pass_or_fail(self):
        if self.mark >= self.passing_mark:
            return "Pass"
        else:
            return "Fail"


# main function to run the code
def main():
    # C) Create an instance of the Student Class, call pass_or_fail method and print.
    student1 = Student("John", 52)
    status1 = student1.pass_or_fail() # or status1 = student1 to get full info.
    print(status1)

    # D) Again we do the same with new student values.
    student2 = Student("Jenny",69)
    status2 = student2.pass_or_fail() # or status2 = student2 to get full info.
    print(status2)


# Runs the code
main()