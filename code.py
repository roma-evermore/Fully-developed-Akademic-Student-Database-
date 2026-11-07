from student import Student
from database import DataBase
from filemanager import FileManager
from update_student import UpdateStudent



database = DataBase()
filemanager = FileManager()
database.students = filemanager.loadFromFile()
updater = UpdateStudent(database.students)


while True:
    print("==================ACADEMIC STUDENT DATABASE==================")
    print("1. Add new student/s to the database. ")
    print("2. Display all the students. ")
    print("3. Add grade to a student. ")
    print("4. Enroll student to a course. ")
    print("5. Search for student(by Last name or PESEL number.)")
    print("6. Sort database by PESEL number or Last name. ")
    print("7. Delete student by ID number. ")
    print("8. Update student information. ")
    print("9. Save database to a file. ")
    print("10. Exit")


    choice = input("Enter the desired option : ")
    if choice == '1':
        database.addStudent()
    elif choice == '2':
        for student in database.students:
            student.display_students()
    elif choice == '3':
        database.add_student_grade()
    elif choice == '4':
        database.enroll_student_to_course()
    elif choice == '5':
        database.SearchForAStudent()
    elif choice == '6':
        database.SortDataBase()
    elif choice == '7':
        database.RemoveStudentFromTheDataBase()
    elif choice == '8':
        updater.UpdateStudent()
        filemanager.saveToFIle(database.students)
    elif choice == '9':
        filemanager.saveToFIle(database.students)
    elif choice == '10':
        filemanager.saveToFIle(database.students)
        print("Pls DONT LEAVe... Senpai.. mrrr")
        break
    else:
        print("Invalid option!! Please choose from 1 to 6")
