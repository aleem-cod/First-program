from tkinter import *

first_number=second_number=operator=None


def get_digit(digit):
    current = result_label['text']

    if current == '0':
        result_label.config(text=str(digit))
    else:
        new = current + str(digit)
        result_label.config(text=new)

def clear():
    result_label.config(text='0')
    expression_label.config(text='')

def get_operator(op):
    global first_number, operator

    first_number = int(result_label['text'])
    operator = op

    expression_label.config(text=str(first_number) + op)

    result_label.config(text='')


def get_result():
    global first_number, second_number, operator

    second_number = int(result_label['text'])

    if operator == '+':
        answer = first_number + second_number

    elif operator == '-':
        answer = first_number - second_number

    elif operator == '*':
        answer = first_number * second_number

    else:
        if second_number == 0:
            expression_label.config(
                text=str(first_number) + operator + str(second_number)
            )
            result_label.config(text='Error')
            return
        else:
            answer = first_number / second_number

    expression_label.config(
        text=str(first_number) + operator + str(second_number)
    )

    result_label.config(text=str(answer))

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

expression_label = Label(
    root,
    text='',
    bg='black',
    fg='gray',
    anchor='e'
)
expression_label.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=(10, 0),
    padx=10,
    sticky='ew'
)
expression_label.config(font=('verdana', 15))

result_label = Label(
    root,
    text='0',
    bg='black',
    fg='white',
    anchor='e'
)
result_label.grid(
    row=1,
    column=0,
    columnspan=4,
    pady=(0, 20),
    padx=10,
    sticky='ew'
)
result_label.config(font=('verdana', 30, 'bold'))

btn7 = Button(root,text='7',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=2,column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=2,column=2)
btn9.config(font=('verdana',14))

btn_add = Button(root,text='+',bg='#FF9500',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=2,column=3)
btn_add.config(font=('verdana',14))



btn4 = Button(root,text='4',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=3,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=3,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=3,column=2)
btn6.config(font=('verdana',14))

btn_minus = Button(root,text='-',bg='#FF9500',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_minus.grid(row=3,column=3)
btn_minus.config(font=('verdana',14))


btn1 = Button(root,text='1',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=4,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=4,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=4,column=2)
btn3.config(font=('verdana',14))

btn_mult = Button(root,text='*',bg='#FF9500',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_mult.grid(row=4,column=3)
btn_mult.config(font=('verdana',14))


btn_Clear = Button(root,text='AC',bg='#333333',fg='white',width=5,height=2,command=lambda:clear())
btn_Clear.grid(row=5,column=0)
btn_Clear.config(font=('verdana',14))

btn_zero = Button(root,text='0',bg='#333333',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn_zero.grid(row=5,column=1)
btn_zero.config(font=('verdana',14))

btn_Equal = Button(root,text='=',bg='#333333',fg='white',width=5,height=2,command=get_result)
btn_Equal.grid(row=5,column=2)
btn_Equal.config(font=('verdana',14))

btn_div = Button(root,text='/',bg='#FF9500',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=5,column=3)
btn_div.config(font=('verdana',14))

root.mainloop()
