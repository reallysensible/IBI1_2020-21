class Student:
    def __init__(self, first_name, last_name, undergraduate_programme):
        self.first_name = first_name
        self.last_name = last_name
        self.undergraduate_programme = undergraduate_programme
    def info(self):
        print(self.first_name, self.last_name,'    ', self.undergraduate_programme)

# example
me = Student('Jiayi', 'Fan', 'BMI')
Student.info(me)
