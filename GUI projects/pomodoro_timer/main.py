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

#VARIABLES
reps = 0
checkmark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checkmark
    window.after_cancel(timer)
    reps = 0
    timer_label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(timer_text, text="00 : 00")
    checkmark = ""
    check_icon.config(text=checkmark)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global checkmark
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # SHORTER TIMES FOR DEBUGGING THE CLOCK
    # work_sec = 1
    # short_break_sec = 2
    # long_break_sec = 3

    #ADD A CHECK MARK TO TRACK USER REPS
    if reps % 2 == 0:
        checkmark += "✔"
        check_icon.config(text=checkmark)

        #If it's 1/3/5/7 rep:
    if reps == 0 or reps == 1 or reps == 3 or reps == 5 or reps == 7:
        print("work time")
        timer_label.config(fg=RED, text="WORK TIME!")
        count_down(work_sec)
    #If it's 2,4 or 6 rep:
    elif reps == 2 or reps ==4 or reps ==6:
        print("short break")
        timer_label.config(fg=PINK, text="Break time")
        count_down(short_break_sec)
    # #If it's the 8th rep:
    elif reps == 8:
        print("Long break")
        timer_label.config(fg=PINK, text="Long break")
        count_down(long_break_sec)
    else:
        timer_label.config(fg=GREEN, text="You're done!")
        canvas.itemconfig(timer_text, text="COMPLETE!")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO TIMER")
window.config(padx=100 ,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#PHOTO IMAGE IS REQUIRED TO READ PHOTOS IN.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

#TIMER LABEL
timer_label = Label(text="Timer")
timer_label.config(padx=10, pady=10, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

#START BUTTON
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#RESET BUTTON
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)

#CHECK ICON
check_icon = Label(bg=YELLOW ,fg=GREEN)
check_icon.grid(column=1, row=4)









window.mainloop()



#IMPORTANT NOTES AND LESSONS I LEARNED
"""If you want to edit a canvas element, you cannot simply call it.config.
For example, timer_text can't be edited timer_text.config(change). 
Since it's a canvas element you need to call canvas first, then itemconfig, then pass the element.
canvas.itemconfig(item_i_want_to_change, text="text i want"). 

"""