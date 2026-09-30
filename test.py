import tkinter as tk
import math

# Create the window
root = tk. Tk()
root.title("For Lisa ❤ ")
root.geometry("800x800")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
        width=800,
        height=800,
        bg="black",
        highlightthickness=0
)
canvas.pack()

# Heart shape
def heart