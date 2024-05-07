from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Entry
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

# Cargar el CSV
data = pd.read_csv('Heart.csv')

# Separar las características (X) y la variable objetivo (y)
X = data.drop('Disease', axis=1)
y = data['Disease']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = round((accuracy_score(y_test, y_pred)) * 100 , 2)

def grafica():
    plt.figure(figsize=(15,10))
    plot_tree(model, feature_names=X.columns, class_names=['No Disease', 'Disease'], filled=True)
    plt.show()


def predecir():  
    canvas.delete("prediccion_texto")
    # Obtener los valores ingresados en las entradas de texto y convertirlos a float
    edad = float(entry_1.get())
    genero = float(entry_2.get())
    ritmo_cardiaco = float(entry_3.get())
    colesterol = float(entry_4.get())
    presion_sangre = float(entry_5.get())
    tipo_dolor_pecho = float(entry_6.get())
    angina_pecho = float(entry_7.get())
    vasos_sanguineos = float(entry_8.get())
    thallium = float(entry_9.get())

    # Formar un nuevo registro con estos valores
    nuevo_registro = [[edad, genero, ritmo_cardiaco, colesterol, presion_sangre, tipo_dolor_pecho, angina_pecho, vasos_sanguineos, thallium]]
    
    # Predecir si el nuevo registro tiene o no una enfermedad cardíaca
    prediccion = model.predict(nuevo_registro)

    canvas.create_text(
    1000.0,
    329.0,
    anchor="nw",
    text=("Presence" if prediccion[0] == "Presence" else "Absence"),  
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1),
    tags="prediccion_texto"
    )
    

######################################################################
window = Tk()

window.geometry("1366x768")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1036.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    321.0,
    69.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1065.0,
    69.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    695.0,
    384.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=grafica,
    relief="flat"
)
button_1.place(
    x=924.0,
    y=681.0,
    width=282.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=predecir,
    relief="flat"
)
button_2.place(
    x=233.0,
    y=681.0,
    width=200.0,
    height=50.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    173.0,
    186.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=73.0,
    y=161.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    72.0,
    135.0,
    anchor="nw",
    text="Edad\n",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    173.0,
    270.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=73.0,
    y=245.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    71.0,
    217.0,
    anchor="nw",
    text="Género (1 - 0)",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    175.0,
    606.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=75.0,
    y=581.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    72.0,
    553.0,
    anchor="nw",
    text="Ritmo Cardíaco",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    173.0,
    522.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=73.0,
    y=497.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    69.0,
    469.0,
    anchor="nw",
    text="Colesterol",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    174.0,
    438.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=74.0,
    y=413.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    72.0,
    385.0,
    anchor="nw",
    text="Presión en sangre",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    173.0,
    354.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=73.0,
    y=329.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    72.0,
    304.0,
    anchor="nw",
    text="Tipo de dolor de pecho",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    489.0,
    186.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=389.0,
    y=161.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    386.0,
    135.0,
    anchor="nw",
    text="Angina de pecho",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    489.0,
    304.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=389.0,
    y=279.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    387.0,
    226.0,
    anchor="nw",
    text="Número de vasos sanguíneos",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    489.0,
    400.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=389.0,
    y=375.0,
    width=200.0,
    height=48.0
)

canvas.create_text(
    385.0,
    347.0,
    anchor="nw",
    text="Thallium",
    fill="#000000",
    font=("InriaSerif Bold", 20 * -1)
)

canvas.create_text(
    894.0,
    146.0,
    anchor="nw",
    text="Predicción de Paciente: ",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)

canvas.create_text(
    816.0,
    239.0,
    anchor="nw",
    text="Diagnóstico:  ",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)


canvas.create_text(
    1000.0,
    513.0,
    anchor="nw",
    text=str(accuracy) + "%",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)

canvas.create_text(
    816.0,
    413.0,
    anchor="nw",
    text="Eficiencia:",
    fill="#FFFFFF",
    font=("InriaSerif Bold", 30 * -1)
)
window.resizable(False, False)
window.mainloop()
