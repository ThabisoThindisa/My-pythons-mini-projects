import customtkinter


class Display(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    def createButton(self, name, command):  # Create UI button
        return customtkinter.CTkButton(self, text=name, command=command)

    def createTextBox(self, width, height):  # Create UI text box

        text_box = customtkinter.CTkTextbox(
            master=self, width=width, height=height)
        text_box.insert("0.0", "new text to insert")
        text = text_box.get("0.0", "end")
        text_box.delete("0.0", "end")  # delete all text
        text_box.configure(state="normal")  # configure textbox to be read-only
        return text_box

    def createLabel(self, name):  # Create UI Label
        label_name = customtkinter.CTkLabel(
            self, text=name, fg_color="transparent")
        return label_name

    def get_input(self, textbox):
        return textbox.get("1.0", "end-1c")
