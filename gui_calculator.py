from tkinter import *

# Mathematical expression entered by the user
expression = ""

def press(num):
    'Modify number on calculator screen whlile pressing the key'
    global expression
    expression = expression + str(num)
    equation.set(expression)
    

def clear():
    'Clear the screen of the calculator'
    global expression
    expression = ''
    equation.set(0)

def equal_press():
    'Process the calculation entered by the user'
    global expression
    if not expression:
        return 0 
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = str(total)
    except:
        equation.set('Error')
        expression = ''


window = Tk()                   # Creaete tkinter object
window.title('Calculator')      # Title of calculator window
window.geometry('330x375')      # Size of the window
window.configure(bg='#5c85d6')  # Set background colour of the window

# Set icon for the application
img = PhotoImage(file='calc.png')
window.iconphoto(False, img)

window.resizable(False, False)  # Lock resizing window


button_frame = Frame(window, bg="#5c85d6")
# pack organizes the control onto the parent widget
button_frame.pack()

# Value of equation is displayed on the screen
equation = StringVar()
equation.set('0')

# Screen design - Creating widgets
calculator_screen = Entry(button_frame, textvariable=equation, justify='right',
                         font=('arial', 20, 'bold'), bg='#000033', fg='#ffffff')

# Button row 1
button1 = Button(button_frame, text='1', font=('times new roman', 12),
                relief='ridge', borderwidth=1, width=8, height=3,
                command=lambda:press(1))
button2 = Button(button_frame, text='2', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(2))
button3 = Button(button_frame, text='3', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(3))
buttonAdd = Button(button_frame, text='+', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press('+'))

# Button row 2
button4 = Button(button_frame, text='4', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(4))
button5 = Button(button_frame, text='5', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(5))
button6 = Button(button_frame, text='6', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(6))
buttonSubtract = Button(button_frame, text='-', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press('-'))

# Button row 3
button7 = Button(button_frame, text='7', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(7))
button8 = Button(button_frame, text='8', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(8))
button9 = Button(button_frame, text='9', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(9))
buttonMultiply = Button(button_frame, text='*', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press('*'))

# Button row 4
button0 = Button(button_frame, text='0', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press(0))
buttonDecimal = Button(button_frame, text='.', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press('.'))
buttonClear = Button(button_frame, text='C', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:clear())

buttonDivide = Button(button_frame, text='/', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=8, height=3,
                command=lambda:press('/'))

# Button row 5
buttonEqual = Button(button_frame, text='=', font=('times new roman', 12),
                relief='ridge', borderwidth=1, bg="#fff7e6", width=35, height=3,
                command=lambda:equal_press())


# Screen design - Placing widgets on the window
calculator_screen.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15)

button1.grid(row=1, column=0, sticky='nsew')
button2.grid(row=1, column=1, sticky='nsew')
button3.grid(row=1, column=2, sticky='nsew')
buttonAdd.grid(row=1, column=3, sticky='nsew')

button4.grid(row=2, column=0, sticky='nsew')
button5.grid(row=2, column=1, sticky='nsew')
button6.grid(row=2, column=2, sticky='nsew')
buttonSubtract.grid(row=2, column=3, sticky='nsew')

button7.grid(row=3, column=0, sticky='nsew')
button8.grid(row=3, column=1, sticky='nsew')
button9.grid(row=3, column=2, sticky='nsew')
buttonMultiply.grid(row=3, column=3, sticky='nsew')

button0.grid(row=4, column=0, sticky='nsew')
buttonDecimal.grid(row=4, column=1, sticky='nsew')
buttonClear.grid(row=4, column=2, sticky='nsew')
buttonDivide.grid(row=4, column=3, sticky='nsew')

buttonEqual.grid(row=5, column=0, columnspan=4, sticky='nsew')

# End screen design

window.mainloop()
