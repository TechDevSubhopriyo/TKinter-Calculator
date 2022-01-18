from tkinter import *
import conversion

root = Tk()
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=30)

list_of_numbers = []
def number_input(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(0, str(current_value) + str(number))
def clear_values():
    list_of_numbers.clear()
    e.delete(0, END)
def sum():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    list_of_numbers.append('+')
    e.delete(0, END)
def sub():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    list_of_numbers.append('-')
    e.delete(0, END)
def mul():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    list_of_numbers.append('*')
    e.delete(0, END)
def div():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    list_of_numbers.append('/')
    e.delete(0, END)
def equals():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    e.delete(0, END)

    stack = list()
    postfix = conversion.infix_to_postfix(list_of_numbers)

    for values in postfix:
        if values == '+':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 + v2)
        elif values == '-':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v2 - v1)
        elif values == '*':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 * v2)
        elif values == '/':
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v2 / v1)
        else:
            stack.append(int(values))

    SUM = stack.pop()
    list_of_numbers.clear()
    e.insert(0, str(SUM))


button9 = Button(root, text="9", pady=20, padx=40, command=lambda: number_input(9)).grid(row=1, column=0)
button8 = Button(root, text="8", pady=20, padx=40, command=lambda: number_input(8)).grid(row=1, column=1)
button7 = Button(root, text="7", pady=20, padx=40, command=lambda: number_input(7)).grid(row=1, column=2)
button6 = Button(root, text="6", pady=20, padx=40, command=lambda: number_input(6)).grid(row=2, column=0)
button5 = Button(root, text="5", pady=20, padx=40, command=lambda: number_input(5)).grid(row=2, column=1)
button4 = Button(root, text="4", pady=20, padx=40, command=lambda: number_input(4)).grid(row=2, column=2)
button3 = Button(root, text="3", pady=20, padx=40, command=lambda: number_input(3)).grid(row=3, column=0)
button2 = Button(root, text="2", pady=20, padx=40, command=lambda: number_input(2)).grid(row=3, column=1)
button1 = Button(root, text="1", pady=20, padx=40, command=lambda: number_input(1)).grid(row=3, column=2)
button0 = Button(root, text="0", pady=20, padx=40, command=lambda: number_input(0)).grid(row=4, column=1)

button_add = Button(root, text="+", pady=20, padx=40, command=lambda: sum()).grid(row=1, column=3)
button_sub = Button(root, text="-", pady=20, padx=40, command=lambda: sub()).grid(row=2, column=3)
button_mul = Button(root, text="*", pady=20, padx=40, command=lambda: mul()).grid(row=3, column=3)
button_div = Button(root, text="/", pady=20, padx=40, command=lambda: div()).grid(row=4, column=3)
button_clear = Button(root, text="CLS", pady=20, padx=30, command=lambda: clear_values()).grid(row=4, column=0)
button_equals = Button(root, text="=", pady=20, padx=40, command=lambda: equals()).grid(row=4, column=2)

root.mainloop()
