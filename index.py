import tkinter as tk
#formspace project
#==form init window1==
window1 = tk.Tk()
window1.geometry("500x500")
window1.title("Window")
#==form init window1==

Title = tk.Label(window1,text="Title")
Title.place(x="0",y="0")

Input1 = tk.Entry(window1)
Input1.pack()

#~script source~ START
print("Form started")
#~script source~ END

#<looping forms>
window1.mainloop()
#formspace end