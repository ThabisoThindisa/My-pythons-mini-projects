
# Student class
class StudentClass:
    Student_list = []  # list of all students saved

    # Save marks of each student
    def Save_Marks(self, english_marks, science_marks, maths_marks):
        Subjects = {"english": english_marks,
                    "science": science_marks,
                    "mathematics": maths_marks
                    }
        return Subjects

   # Add each student
    def add_Student(self, name, surname, student_iD, student_subjects):
        my_student = {"Name": name,
                      "Surname": surname,
                      "ID": student_iD,
                      "Subjects": student_subjects}

        self.Student_list.append(my_student)

    # Get student base on the full name
    def get_Student(self, name, surname):

        for current_Student in self.Student_list:
            if current_Student.get("Name") == name and current_Student.get("Surname"):
                return current_Student

    def get_List(self):
        return self.Student_list
