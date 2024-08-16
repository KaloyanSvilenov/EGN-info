import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import egn_logic as el

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.inputted_egn = ""
        self.obj_egn = el.Logic

        # window
        self.geometry("420x250")
        self.resizable(False, False)
        self.title("ЕГН - информация")

        # 2x3 grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # label for the textbox
        self.label_textbox_egn = ctk.CTkLabel(master=self, text="Въведете ЕГН: ",
                                              fg_color="transparent",
                                              text_color="lightgrey",
                                              font=("Segoe UI", 15),
                                              width=90,
                                              height=20
                                              )
        self.label_textbox_egn.grid(row=0, column=0, padx=0, pady=30, sticky="e")

        # egn input
        self.entry_egn_input = ctk.CTkEntry(master=self,
                                            fg_color="gray",
                                            text_color="black",
                                            font=("Segoe UI", 15),
                                            state="normal",
                                            width=98,
                                            height=18,
                                            placeholder_text="0000000000",
                                            placeholder_text_color="silver"
                                            )
        self.entry_egn_input.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        # analyze egn button
        self.button = ctk.CTkButton(master=self, command=self.output,
                                    fg_color="gray",
                                    hover_color="lightgray",
                                    border_width=2,
                                    border_color="black",
                                    text="давай",
                                    text_color="black",
                                    font=("Segoe UI", 15),
                                    width=100,
                                    height=30
                                    )
        self.button.grid(row=0, column=2, padx=15, pady=10, sticky="sw")
        # self.button.bind('<Return>', self.output)

        # clear button
        self.button_clear = ctk.CTkButton(master=self, command=self.clear_output_label,
                                          fg_color="gray",
                                          hover_color="lightgray",
                                          border_width=2,
                                          border_color="black",
                                          text="изчисти",
                                          text_color="black",
                                          font=("Segoe UI", 15),
                                          width=100,
                                          height=30
                                          )
        self.button_clear.grid(row=1, column=2, padx=15, pady=10, sticky="nw")

        # frame for the output label
        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid(row=1, column=0, columnspan=2, padx=15, pady=15, sticky="nsew")

        # just a line
        line = ""
        while len(line) < 37:
            line += "-"
        # label for the output
        self.result = "\nЕГН: {0}\nРожден ден: {1}\nРоден в област: {2}\nПол: {3}\n{4} родено за деня №{5}\n"
        self.result = line + self.result + line
        self.label_output = ctk.CTkLabel(master=self.frame, text=self.result.format("", "", "", "", "Бебе", ""),
                                         fg_color="transparent",
                                         text_color="lightgrey",
                                         font=("Segoe UI", 15),
                                         justify=tk.LEFT
                                         )
        self.label_output.grid(padx=15, pady=0, sticky="w")

    def throw_error(self):
        tk.messagebox.showerror(title="Грешка", message="Моля въведете правилно ЕГН")
        self.entry_egn_input.delete(0, "end")

    def get_formatted_info(self):
        birthday = self.obj_egn.date() + self.obj_egn.year()
        region = self.obj_egn.city()
        bnum = self.obj_egn.baby()
        sex = self.obj_egn.gender()
        if sex == "М":
            baby = "Момче"
        else:
            baby = "Момиче"

        return self.result.format(self.inputted_egn, birthday, region, sex, baby, bnum)

    def output(self, event=None):
        while 1:
            # gets egn from input
            self.inputted_egn = self.entry_egn_input.get()
            self.obj_egn = el.Logic(self.inputted_egn.split()[0])
            # checks egn
            if not self.obj_egn.check():
                self.throw_error()
                continue
            break

        # output
        self.label_output.configure(text=self.get_formatted_info())
        # delete contents of input textbox
        self.entry_egn_input.delete(0, "end")

    def clear_output_label(self):
        # delete contents of input textbox
        self.entry_egn_input.delete(0, "end")
        # delete contents of output label
        self.label_output.configure(text=self.result.format("", "", "", "", "Бебе", ""))
