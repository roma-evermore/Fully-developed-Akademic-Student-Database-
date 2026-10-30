
from student import Student


class UpdateStudent:

    def __init__(self, students):
        self.students = students

    def find_student(self):

        student_id = input(
            "Enter ID of the student you want to update: "
        )

        for student in self.students:
            if str(student.id_student) == student_id:
                return student

        print("Student has not been found!")
        return None

    def update_first_name(self, student):

        new_name = input("Enter new first name: ").strip()

        if not new_name:
            print("First name unchanged!")

        elif new_name == student.first_name:
            print("This is already the current name!")

        else:
            student.first_name = new_name
            print("First name updated!")

    def update_last_name(self, student):

        new_name = input("Enter new last name: ").strip()

        if not new_name:
            print("Last name unchanged!")

        elif new_name == student.last_name:
            print("This is already the current surname!")

        else:
            student.last_name = new_name
            print("Last name updated!")

    def update_address(self, student):

        new_address = input("Enter new address: ").strip()

        if not new_address:
            print("Address unchanged!")

        elif new_address == student.address:
            print("Address is the same as before!")

        else:
            student.address = new_address
            print("Address updated!")

    def update_id(self, student):

        new_id = input("Enter new ID: ").strip()

        if not new_id:
            print("ID unchanged!")

        elif new_id == str(student.id_student):
            print("ID is the same as before!")

        elif not new_id.isdigit() or len(new_id) != 5:
            print("ID must contain exactly 5 digits!")

        elif any(
            str(s.id_student) == new_id and s is not student
            for s in self.students
        ):
            print("This ID already belongs to another student!")

        else:
            student.id_student = int(new_id)
            print("ID updated!")

    def update_pesel(self, student):

        new_pesel = input("Enter new PESEL: ").strip()

        if not new_pesel:
            print("PESEL unchanged!")

        elif new_pesel == student.pesel_number:
            print("PESEL is the same as before!")

        else:
            temporary_student = Student(
                student.first_name,
                student.last_name,
                student.address,
                student.id_student,
                new_pesel,
                student.gender,
                student.field_of_study,
                student.grades,
                student.courses
            )

            if not temporary_student.ValidatePESEL():
                print("Invalid PESEL!")

            elif any(
                s.pesel_number == new_pesel and s is not student
                for s in self.students
            ):
                print("This PESEL already belongs to another student!")

            else:
                student.pesel_number = new_pesel
                print("PESEL updated!")

    def update_gender(self, student):

        new_gender = input("Enter gender (Man/Woman): ").strip()

        if not new_gender:
            print("Gender unchanged!")

        elif new_gender == student.gender:
            print("Gender is the same as before!")

        elif new_gender not in ["Man", "Woman"]:
            print("Invalid gender!")

        else:
            student.gender = new_gender
            print("Gender updated!")

    def update_field(self, student):

        new_field = input("Enter new field of study: ").strip()

        if not new_field:
            print("Field of study unchanged!")

        elif new_field == student.field_of_study:
            print("Field of study is the same as before!")

        else:
            student.field_of_study = new_field
            print("Field of study updated!")

    def UpdateGrades(self, student):

        while True:

            print("\n===== UPDATE GRADES =====")
            print("Current grades:", student.grades)
            print("1. Add a grade")
            print("2. Replace all grades")
            print("3. Remove all grades")
            print("0. Return")

            choice = input("Choose an option: ")

            if choice == "1":

                try:
                    grade = float(input("Enter grade (2-5): "))

                    if 2 <= grade <= 5:
                        student.add_grade(grade)
                    else:
                        print("Grade must be between 2 and 5!")

                except ValueError:
                    print("Invalid grade!")

            elif choice == "2":

                try:
                    grades_input = input(
                        "Enter grades separated by commas: "
                    ).strip()

                    if not grades_input:
                        print("Grades unchanged!")
                        continue

                    grades = [
                        float(g.strip())
                        for g in grades_input.split(",")
                    ]

                    if not all(2 <= g <= 5 for g in grades):
                        print("Grades must be between 2 and 5!")

                    elif grades == student.grades:
                        print("Grades are the same!")

                    else:
                        student.grades = grades
                        print("Grades updated!")

                except ValueError:
                    print("Invalid grades!")

            elif choice == "3":

                if not student.grades:
                    print("There are no grades to remove!")
                else:
                    student.grades = []
                    print("Grades removed!")

            elif choice == "0":
                break

            else:
                print("Invalid option!")

    def UpdateCourses(self, student):

        while True:

            print("\n===== UPDATE COURSES =====")
            print("Current courses:", student.courses)
            print("1. Add a course")
            print("2. Replace all courses")
            print("3. Remove all courses")
            print("0. Return")

            choice = input("Choose an option: ")

            if choice == "1":

                course = input("Enter course name: ").strip()

                if not course:
                    print("Course name cannot be empty!")

                elif course.lower() in [
                    c.lower() for c in student.courses
                ]:
                    print("Already enrolled in this course!")

                else:
                    student.enroll_course(course)

            elif choice == "2":

                courses_input = input(
                    "Enter courses separated by commas: "
                ).strip()

                if not courses_input:
                    print("Courses unchanged!")
                    continue

                courses = list(dict.fromkeys(
                    c.strip()
                    for c in courses_input.split(",")
                    if c.strip()
                ))

                if [c.lower() for c in courses] == [
                    c.lower() for c in student.courses
                ]:
                    print("Courses are the same!")

                else:
                    student.courses = courses
                    print("Courses updated!")

            elif choice == "3":

                if not student.courses:
                    print("There are no courses to remove!")
                else:
                    student.courses = []
                    print("Courses removed!")

            elif choice == "0":
                break

            else:
                print("Invalid option!")

    def UpdateStudent(self):

        student = self.find_student()

        if student is None:
            return

        print("\nStudent found!")
        student.display_students()

        while True:

            print("\n========== UPDATE STUDENT ==========")
            print("1. Update first name")
            print("2. Update last name")
            print("3. Update address")
            print("4. Update student ID")
            print("5. Update PESEL")
            print("6. Update gender")
            print("7. Update field of study")
            print("8. Update grades")
            print("9. Update courses")
            print("10. Display student information")
            print("0. Finish updating")

            choice = input("What would you like to change? ")

            if choice == "1":
                self.update_first_name(student)

            elif choice == "2":
                self.update_last_name(student)

            elif choice == "3":
                self.update_address(student)

            elif choice == "4":
                self.update_id(student)

            elif choice == "5":
                self.update_pesel(student)

            elif choice == "6":
                self.update_gender(student)

            elif choice == "7":
                self.update_field(student)

            elif choice == "8":
                self.UpdateGrades(student)

            elif choice == "9":
                self.UpdateCourses(student)

            elif choice == "10":
                student.display_students()

            elif choice == "0":
                print("Finished updating student!")
                student.display_students()
                break

            else:
                print("Invalid choice!")

