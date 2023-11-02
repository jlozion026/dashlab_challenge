from tkinter import filedialog
import os
import shutil
from .show_process_docu import show_process_docu
from .generate_csv_files import generate_csv_files


def upload(option, window):
    upload_path = filedialog.askopenfilename() if option == "1" else filedialog.askdirectory()
    if upload_path:
        target_folder = "forms_uploaded"
        os.makedirs(target_folder, exist_ok=True)

        if os.path.isfile(upload_path):
            file_name = os.path.basename(upload_path)
            target_path = os.path.join(target_folder, file_name)
            shutil.copy(upload_path, target_path)
        elif os.path.isdir(upload_path):
            for file_name in os.listdir(upload_path):
                if file_name != ".env":
                    src_path = os.path.join(upload_path, file_name)
                    dest_path = os.path.join(target_folder, file_name)
                    shutil.copy(src_path, dest_path)
        show_process_docu(target_folder, window)