import tkinter as tk
import math
import playsound


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BEEP = "./beep.mp3"
VUVUZELA = "./vuvuzela.mp3"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    check_mark_label["text"] = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_text_label['text'] = "Timer"
    timer_text_label['fg'] = GREEN
    global reps
    reps = 0
    start_button["state"]= "normal"
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 == 1 and reps < 8:
        playsound.playsound(BEEP)
        count_down(work_min)
        timer_text_label['text'] = "Work"
    elif reps % 2 == 0 and reps < 8:
        playsound.playsound(BEEP)
        count_down(short_break)
        timer_text_label['text'] = "Break"
        timer_text_label['fg'] = PINK

    elif reps == 8:
        playsound.playsound(BEEP)
        count_down(long_break)
        timer_text_label['text'] = "Break"
        timer_text_label['fg'] = RED

    elif reps == 9:
        playsound.playsound(VUVUZELA)
        reset()




def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    start_button["state"]= "disabled"
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        ckecks = int(reps / 2)
        if reps < 9:
            check_mark_label["text"] = "✔"* ckecks

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
window.iconphoto(False, image)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 124, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_text_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
timer_text_label.grid(column=1, row=0)
check_mark_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
check_mark_label.grid(column=1, row=3)

start_button = tk.Button(text="Start", highlightthickness=0, font=(FONT_NAME, 16, "bold"), borderwidth=10,
                         command=start_count)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="reset", highlightthickness=0, font=(FONT_NAME, 16, "bold"), borderwidth=10, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
