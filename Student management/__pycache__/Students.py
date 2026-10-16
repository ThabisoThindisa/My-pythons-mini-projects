class StudentClass:
    Student_list = []

    def Save_Students(self, list):
        pass

    # Save marks of each student
    def Save_Marks(self, subjectName, mark):
        Subject = {"name": subjectName,
                   "mark": mark}
        return Subject

   # Add each student
    def add_Student(self, name, surname, student_iD):
        my_student = {"Name": name,
                      "Surname": surname,
                      "ID": student_iD,
                      "Subjects": {}}

        self.Student_list.append(my_student)

    # Get student base on the full name
    def get_Student(self, name, surname):

        for current_Student in self.Student_list:
            if current_Student.get("Name") == name and current_Student.get("Surname"):
                return current_Student

    def get_List(self):
        return self.Student_list
