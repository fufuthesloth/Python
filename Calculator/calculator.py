import customtkinter

customtkinter.set_appearance_mode('dark')  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme('green')  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

        calculation = ''

        def __init__(self):
            super().__init__()

            # Configure window
            self.geometry(f'{320}x{400}')
            self.title('Calculator')
            self.minsize(320, 400)

            # Configure grid layout
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure((0, 1, 2, 3), weight=1)

            # Configure buttons

            # Row 0
            self.text_result = customtkinter.CTkTextbox(master=self, height=2, width=16, font=('UbuntuMono NF', 28))
            self.text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 0), sticky='nsew')

            # Row 1
            self.button_1 = customtkinter.CTkButton(master=self, text='1', command=lambda: self.add_to_calculation('1'), font=('UbuntuMono NF', 14))
            self.button_1.grid(row=1, column=0, padx=(10, 5), pady=(10, 5), sticky='ew')

            self.button_2 = customtkinter.CTkButton(master=self, text='2', command=lambda: self.add_to_calculation('2'), font=('UbuntuMono NF', 14))
            self.button_2.grid(row=1, column=1, padx=5, pady=(10, 5), sticky='ew')

            self.button_3 = customtkinter.CTkButton(master=self, text='3', command=lambda: self.add_to_calculation('3'), font=('UbuntuMono NF', 14))
            self.button_3.grid(row=1, column=2, padx=5, pady=(10, 5), sticky='ew')

            self.button_add = customtkinter.CTkButton(master=self, text='+', command=lambda: self.add_to_calculation('+'), font=('UbuntuMono NF', 14))
            self.button_add.grid(row=1, column=3, padx=(5, 10), pady=(10, 5), sticky='ew')

            # Row 2
            self.button_4 = customtkinter.CTkButton(master=self, text='4', command=lambda: self.add_to_calculation('4'), font=('UbuntuMono NF', 14))
            self.button_4.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky='ew')

            self.button_5 = customtkinter.CTkButton(master=self, text='5', command=lambda: self.add_to_calculation('5'), font=('UbuntuMono NF', 14))
            self.button_5.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

            self.button_6 = customtkinter.CTkButton(master=self, text='6', command=lambda: self.add_to_calculation('6'), font=('UbuntuMono NF', 14))
            self.button_6.grid(row=2, column=2, padx=5, pady=5, sticky='ew')

            self.button_subtract = customtkinter.CTkButton(master=self, text='-', command=lambda: self.add_to_calculation('-'), font=('UbuntuMono NF', 14))
            self.button_subtract.grid(row=2, column=3, padx=(5, 10), pady=5, sticky='ew')

            # Row 3
            self.button_7 = customtkinter.CTkButton(master=self, text='7', command=lambda: self.add_to_calculation('7'), font=('UbuntuMono NF', 14))
            self.button_7.grid(row=3, column=0, padx=(10, 5), pady=5, sticky='ew')

            self.button_8 = customtkinter.CTkButton(master=self, text='8', command=lambda: self.add_to_calculation('8'), font=('UbuntuMono NF', 14))
            self.button_8.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

            self.button_9 = customtkinter.CTkButton(master=self, text='9', command=lambda: self.add_to_calculation('9'), font=('UbuntuMono NF', 14))
            self.button_9.grid(row=3, column=2, padx=5, pady=5, sticky='ew')

            self.button_multiply = customtkinter.CTkButton(master=self, text='*', command=lambda: self.add_to_calculation('*'), font=('UbuntuMono NF', 14))
            self.button_multiply.grid(row=3, column=3, padx=(5, 10), pady=5, sticky='ew')

            # Row 4
            self.button_bracket_left = customtkinter.CTkButton(master=self, text='(', command=lambda: self.add_to_calculation('('), font=('UbuntuMono NF', 14))
            self.button_bracket_left.grid(row=4, column=0, padx=(10, 5), pady=5, sticky='ew')

            self.button_0 = customtkinter.CTkButton(master=self, text='0', command=lambda: self.add_to_calculation('0'), font=('UbuntuMono NF', 14))
            self.button_0.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

            self.button_bracket_right = customtkinter.CTkButton(master=self, text=')', command=lambda: self.add_to_calculation(')'), font=('UbuntuMono NF', 14))
            self.button_bracket_right.grid(row=4, column=2, padx=5, pady=5, sticky='ew')

            self.button_divide = customtkinter.CTkButton(master=self, text='/', command=lambda: self.add_to_calculation('/'), font=('UbuntuMono NF', 14))
            self.button_divide.grid(row=4, column=3, padx=(5, 10), pady=5, sticky='ew')

            # Row 5
            self.button_clear = customtkinter.CTkButton(master=self, text='C', command=self.clear_field, font=('UbuntuMono NF', 14))
            self.button_clear.grid(row=5, column=0, columnspan=2, padx=(10, 5), pady=(5, 10), sticky='ew')

            self.button_equal = customtkinter.CTkButton(master=self, text='=', command=self.evaluate_calculation, font=('UbuntuMono NF', 14))
            self.button_equal.grid(row=5, column=2, columnspan=2, padx=(5, 10), pady=(5, 10), sticky='ew')

        def add_to_calculation(self, symbol : str):
            App.calculation += symbol
            self.text_result.delete(1.0, 'end')
            self.text_result.insert(1.0, App.calculation)

        def evaluate_calculation(self):
            try:
                App.calculation = str(eval(App.calculation))
                self.text_result.delete(1.0, 'end')
                self.text_result.insert(1.0, App.calculation)
            except:
                self.clear_field()
                self.text_result.insert(1.0, 'Error')

        def clear_field(self):
            App.calculation = ''
            self.text_result.delete(1.0, 'end')

if __name__ == '__main__':
    app = App()
    app.mainloop()
    
