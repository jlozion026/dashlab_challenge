from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Toplevel
from utils.generate_csv_files import generate_csv_files
import subprocess
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog, filedialog
import pyzipper
import os
import shutil



def show_generated_csv(window):
    generate_csv_files()
    # Get the directory of the script
    script_dir = Path(__file__).resolve().parent

    # Define relative paths from the script directory
    OUTPUT_PATH = script_dir
    ASSETS_PATH = script_dir.parent / "tkinterdesign" / "build" / "assets" / "frame1"
    file_paths = [
        "output_csv_folder\combined_data_hiv_cert_json.csv",
        "output_csv_folder\combined_data_med_landbase_cert_json.csv",
        "output_csv_folder\combined_data_med_seafarers_cert_json.csv",
        "output_csv_folder\combined_data_med_landbase_exam_json.csv",
        "output_csv_folder\combined_data_med_seafarers_exam_json.csv",
        "output_csv_folder\combined_data_psycho_eval_json.csv"
    ]
    
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    
    def open_file(index):
        try:
            file_path = file_paths[index]
            file_path = Path(file_path)
            
            if file_path.exists():
                # Ask for confirmation
                confirmation = messagebox.askyesno("Confirmation", f"Do you want to open {file_path} in Excel?")
                
                if confirmation:
                    subprocess.Popen(['start', 'excel', str(file_path)], shell=True)
                else:
                    print("File opening canceled.")
            else:
                messagebox.showerror("Error", f"The file '{file_path}' does not exist.")
        except IndexError:
            print("Invalid button index")
            

    def zip_and_encrypt_output_folder(output_csv_folder):
        root = tk.Tk()
        root.withdraw()

        # Prompt user for a zip file name
        zip_file_name = simpledialog.askstring("Input", "Enter the name of your zip file:", initialvalue="default")
        
        if zip_file_name:
            # Prompt user for a password
            password = simpledialog.askstring("Input", "Enter a password for encryption:", show='*')

            if password:
                zip_file_path = f"{zip_file_name}.zip"

                try:
                    with pyzipper.AESZipFile(zip_file_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
                        zf.setpassword(password.encode())
                        for csv_filename in os.listdir(output_csv_folder):
                            csv_file_path = os.path.join(output_csv_folder, csv_filename)
                            zf.write(csv_file_path, csv_filename)

                    # Use the same name for both the zip file and the download
                    download_path = filedialog.asksaveasfilename(
                        initialfile=zip_file_name + '.zip',
                        defaultextension=".zip",
                        filetypes=[("Zip Files", "*.zip")]
                    )

                    if download_path:
                        shutil.move(zip_file_path, download_path)
                        print(f"File downloaded to {download_path}")

                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Password input canceled.")
        else:
            print("Zip file name input canceled")

        root.destroy()

# Usage:
# zip_and_encrypt_output_folder(output_csv_folder)

        
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
        303.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        365.0,
        111.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        top_window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(0),
        relief="flat"
    )
    button_1.place(
        x=184.0,
        y=134.0,
        width=360.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        top_window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(1),
        relief="flat"
    )
    button_2.place(
        x=184.0,
        y=191.64122009277344,
        width=360.0,
        height=47.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        top_window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(2),
        relief="flat"
    )
    button_3.place(
        x=184.0,
        y=251.0,
        width=360.0,
        height=47.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        top_window,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(3),
        relief="flat"
    )
    button_4.place(
        x=184.0,
        y=309.0,
        width=360.0,
        height=47.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        top_window,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(4),
        relief="flat"
    )
    button_5.place(
        x=184.0,
        y=367.0,
        width=360.0,
        height=47.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        top_window,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_file(5),
        relief="flat"
    )
    button_6.place(
        x=184.0,
        y=426.0,
        width=360.0,
        height=47.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        top_window,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: zip_and_encrypt_output_folder("output_csv_folder"),
        relief="flat"
    )
    button_7.place(
        x=456.0,
        y=483.0,
        width=232.0,
        height=53.0
    )
    top_window.resizable(False, False)
    top_window.mainloop()
