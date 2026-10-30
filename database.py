from student import Student
class DataBase:
    def __init__(self):
        self.students = []

    
    def SortDataBase(self):
        print("How do you want to sort the database?")
        print("1. Sort by surname.")
        print("2. Sort by PESEL number.")

        choice = (input("Enter the way you want your database to be sorted :"))
        if choice == "1":
            self.students.sort(key=lambda student: student.last_name)
        elif choice == "2":
            self.students.sort(key=lambda student: student.pesel_number)
        else:
            print("Invalid input!")
            return

        print("Students have been sorted succesfully!!")

        for student in self.students:
            student.display_students()
    
  
    def addStudent(self):

            first_name = input("Enter the name of the student: ").strip()
            last_name = input("Enter the surname of the student: ").strip()
            address = input("Enter the address of the student: ")

   
            try:
                id_student = int(input("Enter an ID of the student: "))
            except ValueError:
                print("Invalid ID. Enter numbers only!")
                return

            if len(str(id_student)) != 5:
                print("ID number must contain exactly 5 digits!")
                return

    
            for student in self.students:
                if student.id_student == id_student:
                    print("This ID already belongs to another student!")
                    return


            pesel_number = input("Enter a PESEL number of the student: ").strip()


            for student in self.students:
                if student.pesel_number == pesel_number:
                    print("This PESEL already belongs to another student!")
                    return

            gender = input("Enter the gender of the student: ").strip()
            field_of_study = input("Enter the field of study: ").strip()

            if gender not in ["Man", "Woman"]:
                print("Invalid gender. Try again.")
                return

            new_student = Student(
                first_name,
                last_name,
                address,
                id_student,
                pesel_number,
                gender,
                field_of_study
            )

            if not new_student.ValidatePESEL():
                print("The PESEL number is wrong! Try again.")
                return

            self.students.append(new_student)

            print("The student has been added successfully!")


    def add_student_grade(self):
        student_id = input("Enter an ID of the student: ")

        for student in self.students:
            if str(student.id_student) == student_id:
                 try:
                     grade = float(input("Enter grade(2-5):  "))
                 except ValueError:
                     print("Invalid grade!! Enter a number!!")
                     return
                 student.add_grade(grade)
                 return
            
        print("Student has not been found!!")


    def enroll_student_to_course(self):
        student_id = input("Enter an ID of the student:")

        for student in self.students:
            if str(student.id_student) == student_id:
                course = input("Enter course name:  ").strip()

                if not course:
                    print("Course name cannot be empty!!")
                    return
                student.enroll_course(course)
                return
            
        print("Student has not been found!!")


    def SearchForAStudent(self):
        search = input("Enter the last name or PESEL number you want to find a student with: ")

        found = False

        for student in self.students:
            if (student.last_name.lower() == search.lower() or student.pesel_number == search):

                student.display_students()
                found = True
                
     
        if not found:
             print("The student has not been found!")
            



    def RemoveStudentFromTheDataBase(self):
        remove_student = (input("Enter an ID number of the student you want to remove: "))

        for student in self.students:

            if str(student.id_student) == remove_student:
                self.students.remove(student)
                print("Student has been removed successfully!!")
                return
            
            
        print("Student has not been found :-(")


   
   