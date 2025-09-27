import pandas as pd

# ========================
# 1. Cargar CSV
# ========================
df = pd.read_csv("BDD_Billboard_copia.csv", low_memory=False)

# ========================
# 2. Normalizar nombres de columnas
# ========================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ========================
# 3. Eliminar columna 'image_url' si existe
# ========================
df.drop(columns=["image_url"], errors="ignore", inplace=True)

# ========================
# 4. Rellenar valores faltantes con "#"
# ========================
df = df.fillna("#")

# ========================
# 5. Eliminar duplicados
# ========================
df = df.drop_duplicates()

# ========================
# 6. Convertir columna 'date' a tipo fecha
# ========================
try:
    df["date"] = pd.to_datetime(df["date"], errors="raise")
except Exception as e:
    print(f"Error al convertir 'date': {e}")

# ========================
# 7. Convertir columnas numéricas
# ========================
num_cols = ["rank", "last_week", "peak_position", "weeks_in_charts"]
for col in num_cols:
    if col in df.columns:
        # Convierte a numérico, los valores no convertibles pasan a NaN
        df[col] = pd.to_numeric(df[col], errors="coerce")
        # Rellenar NaN con "#"
        df[col] = df[col].fillna("#")

# ========================
# 8. Filtrar registros desde el año 2000 en adelante
# ========================
if pd.api.types.is_datetime64_any_dtype(df["date"]):
    df = df[df["date"].dt.year >= 2000]

# ========================
# 9. Guardar CSV limpio
# ========================
df.to_csv("BDD_Billboard_copia_Limpia_2000.csv", index=False)

print("Limpieza completa. CSV guardado como BDD_Billboard_copia_Limpia_2000.csv")
