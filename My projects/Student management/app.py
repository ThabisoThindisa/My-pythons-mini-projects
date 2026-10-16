from GUI import Display
from MathCalculations import Calculator
from Students import StudentClass

app = Display()
app.title("Student Portal")
app.geometry("570x450")
students = StudentClass()


def button_Save_Marks():

    # Get information from textbox
    maths_info = app.get_input(textBox_maths)
    science_info = app.get_input(textBox_science)
    english_info = app.get_input(textBox_english)

    # save Student marks
    subjects_info = students.Save_Marks(english_info, science_info, maths_info)

    # Get user personal information
    temp_name = app.get_input(textBox_name)
    temp_Surname = app.get_input(textBox_surname)
    temp_ID = app.get_input(textBox_ID)

    students.add_Student(temp_name, temp_Surname, temp_ID, subjects_info)


label_name = app.createLabel("Student name: ")
label_Surname = app.createLabel("Student surname: ")
label_ID = app.createLabel("Student ID: ")
label_Marks = app.createLabel(
    "------------------Student Marsk------------------")
label_Marks_Science = app.createLabel("Physical science marks:")
label_Marks_English = app.createLabel("English marks:")
label_Marks_Maths = app.createLabel("Mathematics marks:")

textBox_name = app.createTextBox(300, 30)  # width=300, height=30)
textBox_surname = app.createTextBox(300, 30)  # width=300, height=30)
textBox_ID = app.createTextBox(300, 30)  # width=300, height=30)
textBox_maths = app.createTextBox(100, 30)  # width=300, height=30)
textBox_science = app.createTextBox(100, 30)  # width=300, height=30)
textBox_english = app.createTextBox(100, 30)  # width=300, height=30)

button_Enter = app.createButton("Add Student", button_Save_Marks)

label_name.grid(row=1, column=0, padx=20, pady=7)
textBox_name.grid(row=1, column=1, padx=20, pady=7)
label_Surname.grid(row=2, column=0, padx=20, pady=7)
textBox_surname.grid(row=2, column=1, padx=20, pady=7)
label_ID.grid(row=3, column=0, padx=20, pady=7)
textBox_ID.grid(row=3, column=1, padx=20, pady=0)

label_Marks.grid(row=4, column=1, padx=20, pady=0)

label_Marks_English.grid(row=5, column=0, padx=5, pady=0)
textBox_english.grid(row=5, column=1, padx=0, pady=5)

label_Marks_Maths.grid(row=6, column=0, padx=5, pady=0)
textBox_maths.grid(row=6, column=1, padx=0, pady=5)

label_Marks_Science.grid(row=7, column=0, padx=5, pady=10)
textBox_science.grid(row=7, column=1, padx=0, pady=10)

button_Enter.grid(row=8, column=1, padx=20, pady=20)

app.grid_columnconfigure(0, weight=1)

app.mainloop()
