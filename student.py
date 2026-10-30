class Student:
    def __init__(self, first_name, last_name, address, id_student, pesel_number, gender, field_of_study, grades=None, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.id_student = id_student
        self.pesel_number = str(pesel_number)
        self.gender = gender
        self.field_of_study = field_of_study
        self.grades = grades if grades is not None else []
        self.courses = courses if courses is not None else[]


    def ValidatePESEL(self):
        pesel = self.pesel_number


        if len(pesel) != 11 or not pesel.isdigit():
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

        total = 0

        for i in range(10):
            total += int(pesel[i]) * weights[i]

        checksum = (10 - total % 10) % 10

        return checksum == int(pesel[10])
    


    def display_students(self):
     print("\n============= STUDENT INFORMATION =============")
     print(f"Name: {self.first_name} {self.last_name}")
     print(f"Gender: {self.gender}")
     print(f"ID: {self.id_student}")
     print(f"PESEL: {self.pesel_number}")
     print(f"Address: {self.address}")

     print(f"Field of Study: {self.field_of_study}")

     print(f"Grades: {self.grades}")
     print(f"Average grade: {self.calculated_average():.2f}")

     print("Enrolled courses: ")

     if self.courses:
         for course in self.courses:
             print(f"- {course}")
     else:
         print("No enrolled courses!!")

     print("=======================================")

    def add_grade(self, grade):

        if grade < 2 or grade > 5:
            print("The grade must be between 2 and 5!")
            return

        
        self.grades.append(grade)
        print("Grade added succesfully.")


    def enroll_course(self, course):

        if course in self.courses:
            print("Student is already enrolled in this course1")
            return

        self.courses.append(course)
        print("Course has been added succesfully!")


    def calculated_average(self):

        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)



