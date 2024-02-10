from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_stoper():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_stoper():
    work_time_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    if reps == 7:
        stoper(long_break)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        stoper(work_time_sec)
        label.config(text="Work", fg=GREEN)
    else:
        stoper(short_break)
        label.config(text="Break", fg=PINK)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def stoper(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, stoper, count - 1)
    else:
        start_stoper()
        if reps == 2:
            check_mark.config(text="✔")
        elif reps == 4:
            check_mark.config(text="✔✔")
        elif reps == 6:
            check_mark.config(text="✔✔✔")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

button_start = Button(text="Start", command=start_stoper)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_stoper)
button_reset.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
check_mark.grid(column=1, row=3)

window.mainloop()