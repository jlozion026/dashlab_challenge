from concurrent.futures import ThreadPoolExecutor
from dashlabs import DocumentProcessor
import os
import shutil
import tkinter as tk

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

    def move_processed_file(src_folder,file_name):
        
        processed_file_destination = "processed_forms" 
        src_path = os.path.join(src_folder, file_name)
        dest_path = os.path.join(processed_file_destination, file_name)
        shutil.move(src_path, dest_path)
    
    # Function to process documents
    def process_documents():
        input_folder = "forms_uploaded"
        file_list = os.listdir(input_folder)
        
        for file_name in file_list:
            if os.path.isfile(os.path.join(input_folder, file_name)):
                doc_processor = DocumentProcessor(entry_1)
                file_path = os.path.join(input_folder, file_name)
                doc_processor.process_single_document(file_path, file_name)
                move_processed_file(upload_file_folder,file_name)
        
    top_window = Toplevel(window)

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
        309.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        354.0,
        284.0,
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
        x=80.0,
        y=118.0,
        width=548.0,
        height=330.0
    )

    entry_1.config(state=tk.DISABLED) 

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        top_window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=process_documents,
        relief="flat"
    )
    button_1.place(
        x=174.0,
        y=466.0,
        width=360.0,
        height=47.0
    )
    window.resizable(False, False)
    window.mainloop()
