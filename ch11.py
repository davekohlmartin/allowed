class Student(object):
    def __init__(self, name = "", school = "", grade = ""):
        if not name:
            name = input("What is the student's name? ")
        if not school:
            school = input("what is the student's school? ")
        if not grade:
            grade = self.get_grade()
        self.name = name
        self.school = school
        self.grade = grade

    def get_grade(self):
        while True:
            grade = input("What is the student's grade? {K, 1-5] ")
            if grade.lower() not in ['k', '1', '2', '3', '4', '5']:
                print ("I'm sorry, but {} isn't valid.".format(grade))
            else:
                return grade

    def print_student(self):
        print ("Name: {}".format(self.name))
        print ("School: {}".format(self.school))
        print ("Grade: {}".format(self.grade))

def main():
    student1 = Student()
    student2 = Student(name = "Julian Martin", grade = "2", school = "Francis Scott Key")

if __name__ == "__main__":
        main()

        

    
        
