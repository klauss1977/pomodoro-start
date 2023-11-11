from tkinter import *

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
work_session = 0
keep_counting = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    global work_session
    work_session=0
    reps=0
    window.after_cancel(keep_counting)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Let's work!")
    check_marks_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global work_session
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Long break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    else:
        work_session += 1
        timer_label.config(text=f"Work session {work_session}", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global keep_counting
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        keep_counting = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps%2==0:
            checks=int(reps/2)*"✔"
            check_marks_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Let's work!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer_label.grid(column=1, row=0)
check_marks_label = Label(fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=3)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
