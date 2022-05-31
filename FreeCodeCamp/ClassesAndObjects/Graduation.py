class Student:
    def __init__(self, name, course ,gpa):
        self.name = name
        self.course = course
        self.gpa= gpa

    def category(self):
        if self.gpa >= 3.5:
            return "First Class"
        elif self.gpa >= 3.0:
            return "Upper Second Class"
        elif self.gpa >= 2.5:
            return "Lower Second Class"
        elif self.gpa >= 2.0:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return "Student: {}\tCourse: {}\tGPA: {}\tCategory: {}".format(self.name, self.course, self.gpa, self.category())
        