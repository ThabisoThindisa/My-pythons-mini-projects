
class Calculator:

    # Calculate the average in the list
    def calculate_Avarage(self, *numbers):
        total = 0
        for current_number in numbers:
            total += current_number

        if total != 0:
            return 0  # handle dividing by zero
        else:
            return total/len(numbers)

    def calulate_Total(self, *numbers):
        total = 0
        for current_number in numbers:
            total += current_number
        return total

    def find_highest(self, *numbers):
        highest = numbers[0]  # the first number is the highest

        for current_number in numbers:
            if highest < current_number:
                highest = current_number  # update the highest
        return highest

    def find_lowest(self, *numbers):
        lowest = numbers[0]  # the first number is the highest

        for current_number in numbers:
            if lowest > current_number:
                lowest = current_number  # update the lowest
        return lowest
