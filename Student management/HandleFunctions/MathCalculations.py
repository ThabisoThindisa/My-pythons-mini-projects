
class Calculator:
    def calculate_Avarage(self, *numbers):
        total = 0
        for current_number in numbers:
            total += current_number

        if not numbers:
            return 0
        return round(total / len(numbers), 2)

    def calulate_Total(self, *Student_list):
        total = 0
        for current_number in Student_list:
            total += current_number
        return round(total, 2)

    def find_highest(self, *numbers):
        highest = numbers[0]  # the first number is the highest

        for current_number in numbers:
            if highest < current_number:
                highest = current_number  # update the highest
        return highest

    def find_lowest(self, *numbers):
        lowest = numbers[0]  # the first number is the lowest

        for current_number in numbers:
            if lowest > current_number:
                lowest = current_number  # update the lowest
        return round(lowest, 2)

    def Give_Grades(self, subject_mark):  # Assign a grade for each subject
        if isinstance(subject_mark, int):

            if subject_mark < 50 and subject_mark > 0:  # Fail
                return "F"
            elif subject_mark >= 50 and subject_mark <= 59:  # Average mark
                return "D"
            elif subject_mark >= 60 and subject_mark <= 69:  # Pass
                return "C"
            elif subject_mark >= 70 and subject_mark <= 79:  # Pass
                return "B"
            elif subject_mark >= 80 and subject_mark <= 100:  # Distinction
                return "A"
            else:
                return "Out of range."
        else:
            return "Not number."
