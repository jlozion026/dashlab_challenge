from pathlib import Path

from tkinter import Toplevel
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from utils.generate_csv_files import generate_csv_files


def show_insert_data(window):

    script_dir = Path(__file__).resolve().parent

    # Define relative paths from the script directory
    OUTPUT_PATH = script_dir
    ASSETS_PATH = script_dir.parent / "tkinterdesign" / "build" / "assets" / "frame3"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    top_window = Toplevel(window)
    top_window.title("Medical Form Analyzer")
    top_window.geometry("700x550")
    top_window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        top_window,
        bg = "#FFFFFF",
        height = 550,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        78.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        629.0,
        41.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        172.0,
        42.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        354.0,
        305.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        355.0,
        306.5,
        image=entry_image_1
    )
    entry_1 = Text(
        top_window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )

    entry_1.config(state=tk.DISABLED)

    entry_1.place(
        x=64.0,
        y=115.0,
        width=582.0,
        height=381.0
    )
    
    generate_csv_files(entry_1)
    
    top_window.resizable(False, False)
    top_window.mainloop()
