import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar el CSV
data = pd.read_csv('Heart.csv')

# Separar las características (X) y la variable objetivo (y)
X = data.drop('Disease', axis=1)
y = data['Disease']

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X, y)

# Función para ingresar un nuevo registro y predecir
def predict_new_record(model, data_columns):
    new_data = []
    for column in data_columns:
        value = input(f"Ingrese el valor para '{column}': ")
        new_data.append(value)
    prediction = model.predict([new_data])[0]
    if prediction == 1:
        print("Predicción: Enfermedad cardíaca")
    else:
        print("Predicción: Sin enfermedad cardíaca")

# Solicitar entrada para un nuevo registro
print("Ingrese los valores para el nuevo registro:")
predict_new_record(model, X.columns)

# Visualizar el árbol de decisión
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=X.columns, class_names=['No Disease', 'Disease'], filled=True)
plt.show()
