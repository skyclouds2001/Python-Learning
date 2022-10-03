from tkinter import *


class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")

        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text="Programming is fun")
        self.lbl.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter text:")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)
        bt_change_text = Button(frame2, text="Change Text", command=self.process_button)
        self.v1 = StringVar()
        rb_red = Radiobutton(frame2, text="Red", bg="red", variable=self.v1, value='R',
                             command=self.process_radio_button)
        rb_yellow = Radiobutton(frame2, text="Yellow", bg="yellow", variable=self.v1, value='Y',
                                command=self.process_radio_button)

        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        bt_change_text.grid(row=1, column=3)
        rb_red.grid(row=1, column=4)
        rb_yellow.grid(row=1, column=5)

        window.mainloop()

    def process_radio_button(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "yellow"

    def process_button(self):
        self.lbl["text"] = self.msg.get()


ChangeLabelDemo()
