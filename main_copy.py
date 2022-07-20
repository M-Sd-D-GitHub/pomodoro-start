from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20













window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=("Courier", 24, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=204, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, width=8, height=1)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, width=8, height=1)
reset_button.grid(row=2, column=2)

check_symbol = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_symbol.grid(column=1, row=3)











window.mainloop()