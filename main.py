from tkinter import *

window = Tk()

def calculate():
    total_bill = int(total_amount_input.get())
    total_person = int(no_person_input.get())
    total_tip = int(tip_input.get())

    tip_calculate = round((total_bill+total_tip)/total_person)
    result.config(text=f"{tip_calculate}$")


# grapical user interface

window.title("Bill divider")
window.minsize(width=500, height=220)

# window.grid_rowconfigure(0, weight=0)
# window.grid_columnconfigure(0, weight=1)

result = Label(text="/person$", font=("arial", 24, "bold"))
result.grid(row=0, column=1)

result.place(x=210, y=5)

total_amount_label = Label(text="Enter the total amound of bill",)
total_amount_label.place(x=80, y=50)

total_amount_input = Entry(width=8)
total_amount_input.place(x=280, y=50)

no_person_label = Label(text="Enter number of person")
no_person_label.place(x=110, y=90)

no_person_input = Entry(width=8)
no_person_input.place(x=280, y=90)

tip_label = Label(text="Enter amount of tip")
tip_label.place(x=135, y=130)

tip_input = Entry(width=8)
tip_input.place(x=280, y=130)

button = Button(text="Submit", command=calculate)
button.place(x=210, y=170)



window.mainloop()