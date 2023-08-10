import tkinter
from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(display.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        display.update()

    elif text == "C":
        scvalue.set("")
        display.update()
    elif text == "AC":
        scvalue.set("")
        display.update()
    else:
        scvalue.set(scvalue.get() + text )
        display.update()




root= Tk()
root.geometry("400x600")
root.title("Calculator by Chirag")
root.maxsize(400,600)
root.minsize(400,600)

scvalue=StringVar()
scvalue.set("")
display=Entry(root, textvariable=scvalue, font="lucida 40 bold")
display.pack(fill=X, ipadx=1, pady=25, padx=2)

frame =  Frame(root, bg="grey")
button= Button(frame, text="C",bg="grey", padx=21, pady=15, font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="CE",bg="grey", padx=16 , pady=20, font="lucida 21 bold")
button.pack(side=LEFT)
button= Button(frame, text="%",bg="grey",  padx=22 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="/",bg="grey", padx=28 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame =  Frame(root, bg="grey")
button= Button(frame, text="7", padx=25 , pady=15, font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="8", padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="9",  padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="-",bg="grey", padx=27 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame =  Frame(root, bg="grey")
button= Button(frame, text="4", padx=25 , pady=15, font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="5", padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="6",  padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="*",bg="grey", padx=26 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame =  Frame(root, bg="grey")
button= Button(frame, text="1", padx=24 , pady=15, font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="2", padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="3",  padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="+",bg="grey", padx=23 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

frame =  Frame(root, bg="grey")
button= Button(frame, text="AC",bg="grey", padx=15 , pady=18, font="lucida 22 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text="0", padx=25 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame, text=".",bg="grey",  padx=29 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)

button= Button(frame,bg="orange" ,text="=", padx=22 , pady=15,  font="lucida 25 bold")
button.pack(side=LEFT)
button.bind("<Button-1>", click)
frame.pack()

root.mainloop()