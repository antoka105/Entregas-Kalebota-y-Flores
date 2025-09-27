import pandas as pd

# Cargar CSV
df = pd.read_csv("BDD_Billboard_copia.csv", low_memory=False)

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# === 1. Rellenar valores faltantes con "#" ===
df[col] = pd.to_numeric(df[col], errors="coerce")
df[col] = df[col].fillna("#")

df.drop(columns=["url"], errors="ignore"

# === 2. Eliminar duplicados ===
df = df.drop_duplicates()

# === 3. Convertir columna 'date' a tipo fecha ===
try:
    df["date"] = pd.to_datetime(df["date"], errors="raise")
except:
    pass

# === 4. Convertir columnas numéricas ===
num_cols = ["rank", "last_week", "peak_position", "weeks_in_charts"]
for col in num_cols:
    if col in df.columns:  # solo si la columna existe
        df[col] = pd.to_numeric(df[col], errors="ignore")

# === 5. Filtrar registros desde el año 2000 en adelante ===
if pd.api.types.is_datetime64_any_dtype(df["date"]):
    df = df[df["date"].dt.year >= 2000]

# Guardar CSV limpio
df.to_csv("BDD_Billboard_copia_Limpia_2000.csv", index=False)

print("Limpieza completa. CSV guardado como BDD_Billboard_copia_Limpia_2000.csv")
