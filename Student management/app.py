from HandleFunctions.GUI import Display
from HandleFunctions.MathCalculations import Calculator
from HandleFunctions.Students import StudentClass
from tkinter import messagebox

# How the user interface layout
app = Display()
app.title("Student Portal")
app.geometry("1700x990")
students = StudentClass()
calculator = Calculator()


def button_Save_Marks():
    try:
        maths_info = float(app.get_input(textBox_maths))
        science_info = float(app.get_input(textBox_science))
        english_info = float(app.get_input(textBox_english))
    except ValueError:
        messagebox.showerror("Invalid marks", "Enter a number for each mark.")
        return

    subjects_info = students.Save_Marks(english_info, science_info, maths_info)
    temp_name = app.get_input(textBox_name)
    temp_Surname = app.get_input(textBox_surname)
    temp_ID = app.get_input(textBox_ID)
    students.add_Student(temp_name, temp_Surname, temp_ID, subjects_info)
    clear_Box()
# ------------------ End function here--------------.


def calculate_for_latest_student(calculation, result_box):
    student_list = students.get_List()
    if not student_list:
        messagebox.showwarning(
            "No students", "Add a student before calculating marks.")
        return

    student_marks = student_list[-1]["Subjects"]
    result = calculation(*student_marks.values())
    result_box.delete("1.0", "end")
    result_box.insert("1.0", str(result))
# ------------------ End function here.-------------


def calculate_for_all_students(calculation, result_box):
    student_list = students.get_List()
    if not student_list:
        messagebox.showwarning(
            "No students", "Add a student before calculating marks.")
        return

    student_marks = [
        mark
        for current_student in student_list
        for mark in current_student["Subjects"].values()
    ]
    if not student_marks:
        messagebox.showwarning(
            "No marks", "Add student marks before calculating.")
        return

    result = calculation(*student_marks)
    result_box.delete("1.0", "end")
    result_box.insert("1.0", str(result))


def calculate_average():
    calculate_for_all_students(calculator.calculate_Avarage, textBox_Average)
# ------------------ End function here.-------------


def calculate_total():
    calculate_for_latest_student(calculator.calulate_Total, textBox_Total)
# ------------------ End function here.----------


def calculate_highest():
    calculate_for_all_students(calculator.find_highest, textBox_Highest)
# ------------------ End function here.------------


def Display_All_student():
    Student_List = students.get_List()
    textBox_Display_students.delete("1.0", "end")

    if not Student_List:
        textBox_Display_students.insert("1.0", "No students saved.")
    else:
        for currentStudent in Student_List:
            student_information = ""
            # Format how the student info is displayed
            student_information += "Name: " + currentStudent["Name"] + "\n"
            student_information += "Surname: " + \
                currentStudent["Surname"] + "\n"
            student_information += "ID: " + currentStudent["ID"] + "\n"

            # Add a newline after each student's information
            student_information += "Subjects: " + \
                str(currentStudent["Subjects"]) + "\n\n"

            # Insert at the end of the TextBox
            textBox_Display_students.insert("end", student_information)
# ------------------ End function here.------------


def clear_Box():  # clean textbox after submit
    textBox_name.delete("1.0", "end")
    textBox_ID.delete("1.0", "end")
    textBox_surname.delete("1.0", "end")


def assign_grade():

    # Get marks
    science_mark = app.get_input(textBox_science)
    english_mark = app.get_input(textBox_english)
    math_mark = app.get_input(textBox_maths)

    # Give grade
    science_grade = calculator.Give_Grades(int(science_mark))
    english_grade = calculator.Give_Grades(int(english_mark))
    math_grade = calculator.Give_Grades(int(math_mark))

    # english
    textBox_english_grade.delete("1.0", "end")
    textBox_english_grade.insert("1.0", english_grade)
    # Maths
    textBox_maths_grade.delete("1.0", "end")
    textBox_maths_grade.insert("1.0", math_grade)

    # Science
    textBox_science_grade.delete("1.0", "end")
    textBox_science_grade.insert("1.0", science_grade)
# ------------------ End function here.--------------


# ---------------- user personal information
textBox_name = app.createTextBox(260, 30)  # width=300, height=30)
textBox_surname = app.createTextBox(260, 30)  # width=300, height=30)
textBox_ID = app.createTextBox(260, 30)  # width=300, height=30)
label_name = app.createLabel("Student name: ")
label_Surname = app.createLabel("Student surname: ")
label_ID = app.createLabel("Student ID: ")

# Marks
label_Marks = app.createLabel(
    "------------------Student Marsk------------------")
label_Marks_Science = app.createLabel("Physical science marks (out of 100):")
label_Marks_English = app.createLabel("English marks (out of 100):")
label_Marks_Maths = app.createLabel("Mathematics marks (out of 100):")

textBox_maths = app.createTextBox(100, 30)  # width=300, height=30)
textBox_science = app.createTextBox(100, 30)  # width=300, height=30)
textBox_english = app.createTextBox(100, 30)  # width=300, height=30)


# The grades
label_Grade_Science = app.createLabel("Physical science Grade:")
label_Grade_English = app.createLabel("English Grade:")
label_Grade_Maths = app.createLabel("Mathematics Grade:")

textBox_science_grade = app.createTextBox(150, 30)  # width=300, height=30)

textBox_english_grade = app.createTextBox(150, 30)


textBox_maths_grade = app.createTextBox(150, 30)  # width=300, height=30)
button_Grades = app.createButton(
    "Give grades", assign_grade)


textBox_All = app.createTextBox(300, 300)  # width=300, height=30)
button_Enter = app.createButton("Add Student", button_Save_Marks)

# Do all the calculations
label_Average = app.createLabel("Average:")
label_Total = app.createLabel("total:")
label_high = app.createLabel("Highest marks:")

textBox_Average = app.createTextBox(100, 30)  # width=300, height=30)
textBox_Total = app.createTextBox(100, 30)  # width=300, height=30)
textBox_Highest = app.createTextBox(100, 30)  # width=300, height=30)
textBox_Display_students = app.createTextBox(300, 120)  # width=300, height=30)
Button_Display = app.createButton("Get all students.", Display_All_student)

# ------------------The display of the user interface----------
# row 1
label_name.grid(row=1, column=0, padx=5, pady=10)
textBox_name.grid(row=1, column=1, padx=5, pady=10)
label_Average.grid(row=1, column=2, padx=5, pady=20)
textBox_Average.grid(row=1, column=3, padx=5, pady=20)
button_Average = app.createButton(
    "Calculate average", calculate_average)
button_Average.grid(row=1, column=4, padx=5, pady=20)

# row 2
label_Surname.grid(row=2, column=0, padx=5, pady=10)
textBox_surname.grid(row=2, column=1, padx=5, pady=10)
label_Total.grid(row=2, column=2, padx=5, pady=20)
textBox_Total.grid(row=2, column=3, padx=5, pady=20)
button_Total = app.createButton(
    "Calculate total", calculate_total)
button_Total.grid(row=2, column=4, padx=5, pady=20)

# row 3
label_ID.grid(row=3, column=0, padx=5, pady=10)
textBox_ID.grid(row=3, column=1, padx=5, pady=0)
label_high.grid(row=3, column=2, padx=5, pady=20)
textBox_Highest.grid(row=3, column=3, padx=5, pady=20)
button_highest = app.createButton(
    "Find highest", calculate_highest)
button_highest.grid(row=3, column=4, padx=5, pady=20)

# row 4
label_Marks.grid(row=4, column=1, padx=0, pady=0)

# row 5
label_Marks_English.grid(row=5, column=0, padx=2.5, pady=0)
textBox_english.grid(row=5, column=1, padx=0, pady=5)
label_Grade_English.grid(row=5, column=2, padx=0, pady=20)
textBox_english_grade.grid(row=5, column=3, padx=0, pady=20)

# row 6
label_Marks_Maths.grid(row=6, column=0, padx=2.5, pady=0)
textBox_maths.grid(row=6, column=1, padx=0, pady=5)
label_Grade_Maths.grid(row=6, column=2, padx=0, pady=20)
textBox_maths_grade.grid(row=6, column=3, padx=0, pady=20)

# row 7
label_Marks_Science.grid(row=7, column=0, padx=2.5, pady=3)
textBox_science.grid(row=7, column=1, padx=0, pady=3)
label_Grade_Science.grid(row=7, column=2, padx=0, pady=20)
textBox_science_grade.grid(row=7, column=3, padx=0, pady=20)

# row 8
button_Enter.grid(row=8, column=1, padx=0, pady=3)
button_Grades.grid(row=8, column=3, padx=0, pady=20)

# row 9
textBox_Display_students.grid(row=9, column=0, padx=2.5, pady=5)
Button_Display.grid(row=9, column=1, padx=2.5, pady=5)

app.grid_columnconfigure(0, weight=1)

app.mainloop()
