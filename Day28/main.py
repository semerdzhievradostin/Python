from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5D9C59"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
window = Tk()
window.title("Pomodoro")
window.config(width=600, height=600, padx=100, pady=50, bg=YELLOW)
clock = None


# ---------------------------- UI SETUP ------------------------------- #


tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
break_time = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global break_time
    global clock
    mins, secs = divmod(count, 60)
    time = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer, text=time)
    if count > 0:
        clock = window.after(1000, countdown, count - 1)
    if count < 1:
        start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global break_time
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if break_time:
        countdown(short_break)
        timer_text.config(text="Break", fg=PINK)
        break_time = False
    elif not break_time and reps <= 4:
        countdown(work_time)
        timer_text.config(text="Timer", fg=GREEN)
        reps += 1
        break_time = True
    elif reps > 4:
        countdown(long_break)
        timer_text.config(text="Break", fg=RED)
        checkmark.config(text=CHECKMARK)


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global break_time
    window.after_cancel(clock)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer")
    checkmark.config(text="")
    break_time = False


timer_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35,))
timer_text.grid(column=1, row=0)

canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

reset = Button(text="Reset", command=reset)
reset.grid(column=2, row=2)

window.mainloop()
