from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

window2 = Tk()
window2.title("ESTADÍSTICAS")
window2.geometry("1366x768")
window2.configure(bg="#FFFFFF")

canvas = Canvas(
    window2,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(82.0, 80.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(751.0, 79.0, image=image_image_2)

canvas.create_text(
    243.0,
    50.0,
    anchor="nw",
    text="ESTADÍSTICAS DE LOS REGISTROS ALMACENADOS",
    fill="#000000",
    font=("InriaSerif Bold", 31)
)

# Supongamos que ya has cargado los datos del archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv("Heart.csv")

# Convertir 'Presence' a 1 y 'Absence' a 0 en la columna 'Disease'
df['Disease'] = df['Disease'].map({'Presence': 1, 'Absence': 0})

# Crear una nueva figura para el gráfico de pastel
fig1, ax1 = plt.subplots(figsize=(4, 4))
sex_counts = df['Sex'].value_counts()
ax1.pie(sex_counts, labels=['Male', 'Female'], autopct='%1.1f%%', startangle=140)
ax1.set_title('Distribución de Géneros')

# Guardar el gráfico de pastel como una imagen PNG
fig1.savefig("pie_chart.png")

# Cargar la imagen del gráfico de pastel como un PhotoImage
fig1_photo = PhotoImage(file="pie_chart.png")

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(333.0, 459.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(1027.0, 459.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(333.0, 229.0, image=image_image_5)

canvas.create_text(
    199.0,
    205.0,
    anchor="nw",
    text="Gráfico De Géneros",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(1036.0, 229.0, image=image_image_6)

# Mostrar la imagen del gráfico de pastel en el canvas
canvas.create_image(333.0, 490.0, image=fig1_photo)

canvas.create_text(
    910.0,
    205.0,
    anchor="nw",
    text="Gráfico De Edades",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)

# Crear una nueva figura para el gráfico de barras
fig2, ax2 = plt.subplots(figsize=(4, 4))

# Utilizar pivot_table para asegurarse de tener valores para ambas condiciones en todas las edades
age_disease_counts = df.pivot_table(index='Age', columns='Disease', aggfunc='size', fill_value=0)

ages = age_disease_counts.index
bar_width = 0.35
bar1 = ax2.bar(ages - bar_width/2, age_disease_counts[1], bar_width, label='Con enfermedad')
bar2 = ax2.bar(ages + bar_width/2, age_disease_counts[0], bar_width, label='Sin enfermedad')

ax2.set_xlabel('Edad')
ax2.set_ylabel('Cantidad')
ax2.set_title('Personas con Enfermedad / Edad')
ax2.legend()

# Guardar el gráfico de barras como una imagen PNG
fig2.savefig("bar_chart.png")

# Cargar la imagen del gráfico de barras como un PhotoImage
fig2_photo = PhotoImage(file="bar_chart.png")

# Mostrar la imagen del gráfico de barras en el canvas
canvas.create_image(1025.0, 490.0, image=fig2_photo)

window2.resizable(False, False)
window2.mainloop()
