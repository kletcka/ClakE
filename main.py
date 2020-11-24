import time
import threading
import tkinter as tk
import objects
import json

with open('settings.json', 'r', encoding='utf-8') as read_file:
    settings = json.load(read_file)

WINDOW_HEIGHT = settings["WINDOW_HEIGHT"]
WINDOW_WIDTH = settings["WINDOW_WIDTH"]
BUTTON_SIDE = settings["BUTTON_SIDE"]
SPEED_X = settings["SPEED_X"]
SPEED_Y = settings["SPEED_Y"]
TITLE = settings["TITLE"]

app = objects.App(
    TITLE, WINDOW_WIDTH, WINDOW_HEIGHT,
    BUTTON_SIDE, SPEED_X, SPEED_Y)
if __name__ == "__main__":
    app.mainloop()