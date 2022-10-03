from tkinter import *


class ProcessButtonEvent:
    def process_ok(self):
        print("OK button")

    def process_cancel(self):
        print("Cancel button")

    def __init__(self):
        window = Tk()
        bt_ok = Button(window, text="OK", fg="red", command=self.process_ok())
        bt_cancel = Button(window, text="Cancel", bg="yellow", command=self.process_cancel())

        bt_ok.pack()
        bt_cancel.pack()

        window.mainloop()


ProcessButtonEvent()
