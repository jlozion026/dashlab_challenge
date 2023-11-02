from concurrent.futures import ThreadPoolExecutor
from dashlabs import DocumentProcessor
import os
import shutil
import tkinter as tk
from utils.generate_csv_files import generate_csv_files
from .time_it import time_it

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar
from tkinter import Toplevel


def show_process_docu(upload_file_folder, window):
    
    # Get the directory of the script
    script_dir = Path(__file__).resolve().parent

    # Define relative paths from the script directory
    OUTPUT_PATH = script_dir
    ASSETS_PATH = script_dir.parent / "tkinterdesign" / "build" / "assets" / "frame2"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    
    def update_diagnostics(message):
        entry_1.config(state=tk.NORMAL)  # Set state to normal to edit
        entry_1.insert(tk.END, message + "\n")
        entry_1.see(tk.END)
        entry_1.config(state=tk.DISABLED)  # Set state to disabled to make it uneditable
        entry_1.update_idletasks()  # Refresh the GUI
     
    # Function to process documents
    @time_it
    def process_documents():
        input_folder = "forms_uploaded"
        file_list = os.listdir(input_folder)
        
        for file_name in file_list:
            if os.path.isfile(os.path.join(input_folder, file_name)):
                doc_processor = DocumentProcessor(entry_1)
                file_path = os.path.join(input_folder, file_name)
                doc_processor.process_single_document(file_path, file_name)
        update_diagnostics("Processing Successful!")
        
        
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
        353.5,
        296.0,
        image=entry_image_1
    )
    entry_1 = Text(
        top_window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=60.0,
        y=103.0,
        width=587.0,
        height=384.0
    )

    entry_1.config(state=tk.DISABLED) 

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        top_window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: process_documents(),
        relief="flat"
    )
    button_1.place(
        x=218.0,
        y=489.0,
        width=272.0,
        height=48.0
    )
    top_window.resizable(False, False)
    top_window.mainloop()


