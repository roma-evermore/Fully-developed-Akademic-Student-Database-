import json
from student import Student

class FileManager:
    def saveToFIle(self, students):
        data = []


        for student in students:
            data.append({
                "first_name" : student.first_name,
                "last_name" : student.last_name,
                "address" : student.address,
                "id_student" : student.id_student,
                "pesel_number" : student.pesel_number,
                "gender" : student.gender,
                "field_of_study" : student.field_of_study,
                "grades" : student.grades,
                "courses" : student.courses
            })

        with open("students.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Database has been saved succesfully!!")


    def loadFromFile(self):
        try:

            with open("students.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            students = []

            for item in data:
                student = Student(
                    item["first_name"],
                    item["last_name"],
                    item["address"],
                    item["id_student"],
                    item["pesel_number"],
                    item["gender"],
                    item.get("field_of_study", "Not Specified"),
                    item.get("grades", []),
                    item.get("courses", [])

                )

                students.append(student)

            
           


            print("Database loaded succesfully!!")
            return students

        except FileNotFoundError:
            print("No saved database found. Starting with an empty database.")
            return []
        except(json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Could not load the database:  {error}")
            return []
