import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar dataset delimitado por punto y coma
df = pd.read_csv("cda-export.csv", delimiter=";")

# Elegimos columnas útiles como características para predecir 'nitrogen'
# Puedes cambiar 'nitrogen' por otra variable objetivo de tu dataset
features = [
    "phosphorus", "potassium", "electricconductivity", "ph",
    "organiccontent", "sandcontent", "siltcontent", "claycontent", "density"
]

target = "nitrogen"

# Quitar filas con valores nulos
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

# Entrenar
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# Evaluar
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.3f}")
print(f"R2: {r2:.3f}")

# Ejemplo de predicción con una muestra nueva
ejemplo = pd.DataFrame({
    "phosphorus": [50],
    "potassium": [40],
    "electricconductivity": [0.5],
    "ph": [6.8],
    "organiccontent": [3.2],
    "sandcontent": [30],
    "siltcontent": [50],
    "claycontent": [20],
    "density": [1.3]
})

prediccion_nitrogen = model.predict(ejemplo)
print(f"Predicción Nitrogen: {prediccion_nitrogen[0]:.2f}")
