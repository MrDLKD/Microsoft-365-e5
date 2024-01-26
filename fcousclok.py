import tkinter as tk
from tkinter import messagebox
import time

class FocusClock:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x200")

        self.time_remaining = 25 * 60  # 默认25分钟专注时间（以秒为单位）
        self.is_running = False

        self.label = tk.Label(master, text=self.format_time(self.time_remaining), font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="开始专注", command=self.start_focus)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="停止专注", command=self.stop_focus, state=tk.DISABLED)
        self.stop_button.pack()

    def start_focus(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.countdown()

    def stop_focus(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def countdown(self):
        if self.is_running and self.time_remaining > 0:
            self.label.config(text=self.format_time(self.time_remaining))
            self.time_remaining -= 1
            self.master.after(1000, self.countdown)
        elif self.time_remaining == 0:
            messagebox.showinfo("专注结束", "专注时间已结束！")
            self.reset_clock()

    def reset_clock(self):
        self.is_running = False
        self.time_remaining = 25 * 60
        self.label.config(text=self.format_time(self.time_remaining))
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    @staticmethod
    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusClock(root)
    root.mainloop()
