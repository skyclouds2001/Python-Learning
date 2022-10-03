from tkinter import *


def process_ok():
    print("OK button")


def process_cancel():
    print("Cancel button")


window = Tk()
btOK = Button(window, text="OK", fg="red", command=process_ok())
btCancel = Button(window, text="Cancel", bg="yellow", command=process_cancel())

btOK.pack()
btCancel.pack()

window.mainloop()
