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
