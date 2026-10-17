
# Student class
class StudentClass:
    Student_list = []  # list of all students saved

    # Save marks of each student
    def Save_Marks(self, english_marks, science_marks, maths_marks):

        temp_english = english_marks
        temp_science = science_marks
        temp_maths = maths_marks

        # Check if its in range of 0 <x< 100
        if temp_english < 0 or temp_english > 100:
            temp_english = 0
        if temp_science < 0 or temp_science > 100:
            temp_science = 0
        if temp_maths < 0 or temp_maths > 100:
            temp_maths = 0

        Subjects = {"english": temp_english,
                    "science": temp_science,
                    "mathematics": temp_maths
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
