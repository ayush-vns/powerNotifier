from tkinter import *

root = Tk()
root.title("powerNotifier")
root.iconbitmap("../icon2.ico")

title_head = "Welcome to Power Notifier!"
Title = Label(root, text=title_head, width=40, bd=1, relief=RAISED)
Title.grid(row=0, column=0, pady=5, columnspan=2)

# Frame 1
frame1 = LabelFrame(root, text="PowerInfo...", padx=5, pady=5)
frame1.grid(row=1, column=0, padx=10, pady=10)

l11 = Label(frame1, text="Info about battary...", width=40, bd=1, relief=RIDGE) # releif = flat, groove, raised, ridge, solid, or sunken
l11.grid(row=0, column=0)

e11 = Entry(frame1, width=40, bd=1)
e11.grid(row=1, column=0, pady=10)

b11 = Button(frame1, text="Run", padx=10)
b11.grid(row=2, column=0)

## Frame 2
frame2 = LabelFrame(root, text="CPUInfo...", padx=5, pady=5)
frame2.grid(row=1, column=1,padx=10, pady=10)

Labelpi = Label(frame2, text="Info about CPU...", width=40, bd=1, relief=RIDGE)
Labelpi.grid(row=0, column=0)

e11 = Entry(frame2, width=40, bd=1)
e11.grid(row=1, column=0, pady=10)

b21 = Button(frame2, text="Run", padx=10)
b21.grid(row=2, column=0)

root.mainloop()