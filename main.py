from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from pathlib import Path


from utils import upload
from utils import show_generated_csv
from utils import show_insert_data

# Get the directory of the script
script_dir = Path(__file__).resolve().parent

# Define relative paths from the script directory
OUTPUT_PATH = script_dir
ASSETS_PATH = script_dir / "tkinterdesign" / "build" / "assets" / "frame0"



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.title("Medical Form Analyzer")

window.geometry("700x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
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
    350.0,
    292.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    542.0,
    381.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    535.0,
    292.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    123.0,
    156.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    172.0,
    42.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    229.0,
    350.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    460.0,
    188.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    535.0,
    320.0,
    image=image_image_9
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: upload("1", window),
    relief="flat"
)
button_1.place(
    x=265.0,
    y=111.0,
    width=134.0,
    height=134.35574340820312
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: upload("2", window),
    relief="flat"
)
button_2.place(
    x=518.0,
    y=109.0,
    width=136.0,
    height=133.080078125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_generated_csv(window),
    relief="flat"
)
button_3.place(
    x=447.0,
    y=467.0,
    width=237.0,
    height=53.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_insert_data(window),
    relief="flat"
)
button_4.place(
    x=208.0,
    y=471.0,
    width=234.0,
    height=57.0
)
window.resizable(False, False)
window.mainloop()
