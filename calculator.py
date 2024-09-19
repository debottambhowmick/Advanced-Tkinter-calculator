from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry('500x300')
        self.operator = None
        self.is_result = False

        #button styles
        self.configure_styles()

        # Display frame
        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack()
        
        self.display_text = StringVar()

        self.display = ttk.Label(self.frame1, textvariable=self.display_text, font=('helvetica', 24), justify='left', width=27, background="white")
        self.display.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        # Number pad frame
        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack()

        # number pad buttons
        self.create_num_pad_buttons()

        # operation buttons
        self.create_operation_buttons()

        # utility buttons
        self.create_utility_buttons()

        # Configure row weight
        self.root.grid_columnconfigure(0, weight=1)
        self.root.mainloop()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Style for number buttons
        self.style.configure('Number.TButton', background="#d1c4e9", foreground="black", font=('helvetica', 12))

        # Style for operation buttons
        self.style.configure('Operation.TButton', background="#ff7043", foreground="white", font=('helvetica', 12))

        # Style for utility buttons
        self.style.configure('Utility.TButton', background="#4caf50", foreground="white", font=('helvetica', 12))

    def create_num_pad_buttons(self):

        button_style = {'padx': 5, 'pady': 5, 'sticky': 'ew'}

        self.num_7 = ttk.Button(self.frame2, text='7', style='Number.TButton', command=lambda: self.num_pad_btn(7))
        self.num_7.grid(row=0, column=0, **button_style)

        self.num_8 = ttk.Button(self.frame2, text='8', style='Number.TButton', command=lambda: self.num_pad_btn(8))
        self.num_8.grid(row=0, column=1, **button_style)

        self.num_9 = ttk.Button(self.frame2, text='9', style='Number.TButton', command=lambda: self.num_pad_btn(9))
        self.num_9.grid(row=0, column=2, **button_style)

        self.num_4 = ttk.Button(self.frame2, text='4', style='Number.TButton', command=lambda: self.num_pad_btn(4))
        self.num_4.grid(row=1, column=0, **button_style)

        self.num_5 = ttk.Button(self.frame2, text='5', style='Number.TButton', command=lambda: self.num_pad_btn(5))
        self.num_5.grid(row=1, column=1, **button_style)

        self.num_6 = ttk.Button(self.frame2, text='6', style='Number.TButton', command=lambda: self.num_pad_btn(6))
        self.num_6.grid(row=1, column=2, **button_style)

        self.num_1 = ttk.Button(self.frame2, text='1', style='Number.TButton', command=lambda: self.num_pad_btn(1))
        self.num_1.grid(row=2, column=0, **button_style)

        self.num_2 = ttk.Button(self.frame2, text='2', style='Number.TButton', command=lambda: self.num_pad_btn(2))
        self.num_2.grid(row=2, column=1, **button_style)

        self.num_3 = ttk.Button(self.frame2, text='3', style='Number.TButton', command=lambda: self.num_pad_btn(3))
        self.num_3.grid(row=2, column=2, **button_style)

        self.num_0 = ttk.Button(self.frame2, text='0', style='Number.TButton', command=lambda: self.num_pad_btn(0))
        self.num_0.grid(row=3, column=0, **button_style)

        self.num_00 = ttk.Button(self.frame2, text='00', style='Number.TButton', command=lambda: self.num_pad_btn('00'))
        self.num_00.grid(row=3, column=1, **button_style)

        self.num_dot = ttk.Button(self.frame2, text='.', style='Number.TButton', command=lambda: self.num_pad_btn('.'))
        self.num_dot.grid(row=3, column=2, **button_style)

    def create_operation_buttons(self):

        button_style = {'padx': 5, 'pady': 5, 'sticky': 'ew'}

        self.plus_btn = ttk.Button(self.frame2, text='+', style='Operation.TButton', command=lambda: self.plus())
        self.plus_btn.grid(row=3, column=3, **button_style)

        self.minus_btn = ttk.Button(self.frame2, text='-', style='Operation.TButton', command=lambda: self.minus())
        self.minus_btn.grid(row=2, column=3, **button_style)

        self.multi = ttk.Button(self.frame2, text='x', style='Operation.TButton', command=lambda: self.multiply())
        self.multi.grid(row=1, column=3, **button_style)

        self.div = ttk.Button(self.frame2, text='/', style='Operation.TButton', command=lambda: self.division())
        self.div.grid(row=0, column=3, **button_style)

    def create_utility_buttons(self):

        button_style = {'padx': 5, 'pady': 5, 'sticky': 'ew'}

        self.clear_btn = ttk.Button(self.frame2, text='C', style='Utility.TButton', command=lambda: self.clear())
        self.clear_btn.grid(row=4, column=0, **button_style)

        self.back_btn = ttk.Button(self.frame2, text='←', style='Utility.TButton', command=lambda: self.back())
        self.back_btn.grid(row=4, column=1, **button_style)

        self.percent_btn = ttk.Button(self.frame2, text='%', style='Utility.TButton', command=lambda: self.percent())
        self.percent_btn.grid(row=4, column=2, **button_style)

        self.cal_btn = ttk.Button(self.frame2, text='=', style='Utility.TButton', command=lambda: self.cal())
        self.cal_btn.grid(row=4, column=3, **button_style)

    def num_pad_btn(self, number):
        if not self.is_result:
            old_text = self.display.cget('text')
            new_text = old_text + str(number)
            self.display_text.set(new_text)
    
    def clear(self):
        self.display_text.set("")
        self.is_result = False
    
    def back(self):
        if not self.is_result:
            current_value = self.display.cget('text')
            new_value = current_value[:-1]
            self.display_text.set(new_value)

    def plus(self):
        if self.operator is not None:
            self.cal()
        self.first_num = self.display.cget('text')
        self.operator = '+'
        self.clear()

    def minus(self):
        if self.operator is not None:
            self.cal()
        self.first_num = self.display.cget('text')
        self.operator = '-'
        self.clear()
    
    def multiply(self):
        if self.operator is not None:
            self.cal()
        self.first_num = self.display.cget('text')
        self.operator = 'x'
        self.clear()

    def division(self):
        if self.operator is not None:
            self.cal()
        self.first_num = self.display.cget('text')
        self.operator = '/'
        self.clear()
    
    def percent(self):
        if self.operator is not None:
            self.cal()
        self.first_num = self.display.cget('text')
        self.operator = '%'
        self.clear()

    def cal(self):
        self.second_num = self.display.cget('text')
        if self.operator == '+':
            self.result = float(self.first_num) + float(self.second_num)
            self.display_text.set(str(self.result))
            self.is_result = True
            self.operator = None

        elif self.operator == '-':
            self.result = float(self.first_num) - float(self.second_num)
            self.display_text.set(str(self.result))
            self.is_result = True
            self.operator = None
        
        elif self.operator == 'x':
            self.result = float(self.first_num) * float(self.second_num)
            self.display_text.set(str(self.result))
            self.is_result = True
            self.operator = None
        
        elif self.operator == '/':
            try:
                self.result = round((float(self.first_num)/float(self.second_num)), 4)
                self.display_text.set(str(self.result))
                self.is_result = True
                self.operator = None
            except ZeroDivisionError:
                self.display_text.set("Cannot divide by zero.")
                return
        
        elif self.operator == '%':
            self.result = (float(self.first_num) * float(self.second_num)) / 100
            self.display_text.set(str(self.result))
            self.is_result = True
            self.operator = None

if __name__ == "__main__":
    Calculator()
