from pathlib import Path 
import os
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

def abrir_estadisticas():
    os.system("python estadisticas.py")

def abrir_prediccion():
    os.system("python Prediccion.py")

window1 = tk.Tk()
window1.title("MENÚ INICIO")
window1.geometry("1366x768")
window1.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window1,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(683.0, 379.0, image=image_image_1)

image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(683.0, 615.0, image=image_image_2)

button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_prediccion,
    relief="flat"
)
button_1.place(x=941.0, y=582.0, width=250.0, height=67.0)

button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_inicio"),
    relief="flat"
)
button_2.place(x=558.0, y=582.0, width=250.0, height=67.0)

button_image_3 = tk.PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_estadisticas,
    relief="flat"
)
button_3.place(x=175.0, y=582.0, width=250.0, height=67.0)

canvas.create_rectangle(0.0, 0.0, 1366.0, 170.0, fill="#01043B", outline="")
canvas.create_text(
    524.0,
    0.0,
    anchor="nw",
    text="¡ Bienvenido !",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 50 * -1)
)

canvas.create_text(
    158.0,
    85.0,
    anchor="nw",
    text="Sistema Inteligente De Predicción Cardiovascular",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 50 * -1)
)

window1.resizable(False, False)
window1.mainloop()
