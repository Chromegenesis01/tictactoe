from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("tic tac toe")
root.geometry('1000x1000')

clicked = True
count = 0
o_winner = 0
x_winner = 0


def checkwon():
    global winner, o_winner, x_winner
    winner = False

    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")

    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        winner = True
        x_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")



    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        winner = True
        reset()
        o_winner += 1
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")

    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        winner = True
        o_winner += 1
        reset()
        messagebox.showinfo("tic tac toe", "Winner!")
    label_three = Label(root, text=o_winner, font='Times 15')
    label_three.place(x=900, y=100)
    label_three = Label(root, text=x_winner, font='Times 15')
    label_three.place(x=900, y=300)


def b_click(b):
    global clicked, count
    if b["text"] == ' ' and clicked == True:
        b["text"] = 'X'
        clicked = False
        count += 1
        checkwon()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        checkwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Choose a different box!")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=('Times', 20), height=3, width=6, bg="pink", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def resetscore():
    global x_winner, o_winner
    x_winner = 0
    o_winner = 0
    label_three = Label(root, text=o_winner, font='Times 15')
    label_three.place(x=900, y=100)
    label_three = Label(root, text=x_winner, font='Times 15')
    label_three.place(x=900, y=300)


Button(root, bg="red", text="reset board", width=10, command=reset).grid(row=21, sticky=W)
Button(root, bg="red", text="reset score", width=10, command=resetscore).grid(row=20, sticky=W)

label_one = Label(root, text='o_wins: ', font='Times 15')
label_one.place(x=700, y=100)

label_two = Label(root, text='x_wins: ', font='Times 15')
label_two.place(x=700, y=300)

label_three = Label(root, text=o_winner, font='Times 15')
label_three.place(x=900, y=100)

label_three = Label(root, text=x_winner, font='Times 15')
label_three.place(x=900, y=300)
reset()
root.mainloop()