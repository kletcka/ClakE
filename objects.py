import time
import threading
import tkinter as tk
from random import randint as rnd


class App(tk.Tk):
    def __init__(self, title, size_x, size_y, b_size, spped_x, speed_y):
        super().__init__()
        self.title(title)
        self.window_x = int(size_x)
        self.window_y = int(size_y)
        self.geometry(f'{self.window_x}x{self.window_y}')
        self.vx = spped_x
        self.vy = speed_y
        self.w = int(b_size)
        self.h = (self.w)*6/10
        self.cliks = 0
        self.x = rnd(5, (self.window_x-(self.w*11))-5)
        self.y = rnd(5, (self.window_y-(self.h*18))-5)
        self.button = tk.Button(
            self, command=self.start_action,
            text=self.cliks,  height=int(self.h), width=int(self.w))
        self.button.place(x=self.x, y=self.y)

    def start_action(self):
        self.button.destroy()
        self.button = tk.Button(
            self, command=self.add,
            text=self.cliks,  height=int(self.h), width=int(self.w))
        self.button.place(x=self.x, y=self.y)
        thread = threading.Thread(target=self.run_action)
        thread.start()

    def add(self):
        self.cliks += 1
        self.button['text'] = str(self.cliks)
        self.button.place(x=int(self.x), y=int(self.y))

    def run_action(self):
        while True:
            self.x += self.vx / 100
            self.y += self.vy / 100
            if self.x >= (self.window_x-(self.w * 11)):
                self.vx = -self.vx
            if self.y >= (self.window_y-(self.h * 18)):
                self.vy = -self.vy
            if self.x <= 0:
                self.vx = -self.vx
            if self.y <= 0:
                self.vy = -self.vy
            try:
                self.button.place(x=self.x, y=self.y)
            except Exception:
                pass
