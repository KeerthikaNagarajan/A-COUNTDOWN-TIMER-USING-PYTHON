# A COUNTDOWN TIMER USING PYTHON

## Description:
This is a simple countdown timer application built using Python's Tkinter library. It allows users to set a duration and displays a countdown until the timer reaches zero. The application provides options to start, pause, and reset the timer.

## Features:
- Set a custom duration for the countdown timer.
- Start, pause, and reset the timer as needed.
- Display the remaining time in minutes and seconds format.
- Notify users when the timer finishes.

## Usage:
1. Enter the duration of the timer in seconds when prompted.
2. Click the "Start" button to begin the countdown.
3. Click the "Pause" button to temporarily pause the timer. Click "Resume" to continue.
4. Click the "Reset" button to reset the timer to its initial duration.

## CODE:
```python
import tkinter as tk
from tkinter import messagebox

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining_time = duration
        self.is_paused = False

        # create GUI
        self.window = tk.Tk()
        self.window.title("Countdown Timer")
        self.label = tk.Label(self.window, text="")
        self.label.pack()
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.pause_button = tk.Button(self.window, text="Pause", state="disabled", command=self.pause_timer)
        self.pause_button.pack()
        self.reset_button = tk.Button(self.window, text="Reset", state="disabled", command=self.reset_timer)
        self.reset_button.pack()

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.update_timer()

    def pause_timer(self):
        if self.is_paused:
            self.pause_button.config(text="Pause")
            self.is_paused = False
            self.update_timer()
        else:
            self.pause_button.config(text="Resume")
            self.is_paused = True

    def reset_timer(self):
        self.remaining_time = self.duration
        self.is_paused = False
        self.label.config(text="")
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def update_timer(self):
        if self.remaining_time <= 0:
            self.pause_button.config(state="disabled")
            self.label.config(text="Time's up!")
            messagebox.showinfo("Time's up!", "The timer has finished.")
        elif not self.is_paused:
            minutes, seconds = divmod(self.remaining_time, 60)
            time_string = f"{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_string)
            self.remaining_time -= 1

        self.window.after(1000, self.update_timer)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    duration = int(input("Enter the duration of the timer in seconds: "))
    timer = Timer(duration)
    timer.run()
```

   
## INPUT: 
 <img width="285" alt="input" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/61a0363f-01a2-481e-a3bd-fe6e5ada0cc9">


## OUTPUT: 

•	Before starting the timer:

<img width="210" alt="before start" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/ddaa131a-b15f-4eb1-94aa-9a3f50593348">

•	While the timer is paused:

<img width="210" alt="while pause" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/1bb834b8-2a63-48e5-8ecd-63ecea86be79">

 
•	While the timer is resumed:

<img width="210" alt="while resume" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/b5cc7850-74a7-45e0-897b-5b12cb0cc9f5">


•	While the timer is up:

 <img width="210" alt="while pause" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/4ed696ca-3688-4d18-9bd9-4fd331fe2c4e">


•	After reset:

 <img width="210" alt="before start" src="https://github.com/KeerthikaNagarajan/A-COUNTDOWN-TIMER-USING-PYTHON/assets/93427089/847224c1-94d2-41e0-a723-a517982cc323">

## Conclusion
The countdown timer successfully ran for the specified duration, providing real-time updates on the remaining time. Users were able to start, pause, and reset the timer as needed, allowing for flexible time management. Upon completion of the timer, a notification was displayed, indicating that the time was up. Overall, the application functioned as intended, providing a convenient tool for countdown timing tasks.



