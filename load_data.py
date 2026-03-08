import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

# Cargar los datos directamente desde la API
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"
response = requests.get(url)
data = response.json()

# Extraer datos manualmente antes de crear DataFrame
records = []
for item in data:
    record = {
        'customerID': item.get('customerID'),
        'Churn': item.get('Churn'),
        # customer
        'gender': item['customer'].get('gender'),
        'SeniorCitizen': item['customer'].get('SeniorCitizen'),
        'Partner': item['customer'].get('Partner'),
        'Dependents': item['customer'].get('Dependents'),
        'tenure': item['customer'].get('tenure'),
        # phone
        'PhoneService': item['phone'].get('PhoneService'),
        'MultipleLines': item['phone'].get('MultipleLines'),
        # internet
        'InternetService': item['internet'].get('InternetService'),
        'OnlineSecurity': item['internet'].get('OnlineSecurity'),
        'OnlineBackup': item['internet'].get('OnlineBackup'),
        'DeviceProtection': item['internet'].get('DeviceProtection'),
        'TechSupport': item['internet'].get('TechSupport'),
        'StreamingTV': item['internet'].get('StreamingTV'),
        'StreamingMovies': item['internet'].get('StreamingMovies'),
        # account
        'Contract': item['account'].get('Contract'),
        'PaperlessBilling': item['account'].get('PaperlessBilling'),
        'PaymentMethod': item['account'].get('PaymentMethod'),
        # charges
        'Monthly': item['account']['Charges'].get('Monthly'),
        'Total': item['account']['Charges'].get('Total'),
    }
    records.append(record)

# Convertir a DataFrame
df = pd.DataFrame(records)

# Información inicial
print("Columnas del DataFrame después de extracción:")
print(df.columns.tolist())
print(f"\nForma: {df.shape}")
print(f"\nTipos de datos:")
print(df.dtypes)

# LIMPIAR Y PROCESAR DATOS
# Eliminar duplicados por customerID
df = df.drop_duplicates(subset=['customerID'])

# Llenar valores faltantes
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('desconocido')
    elif df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].median())

# Normalizar strings: minúsculas y sin espacios
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(lambda x: x.lower().strip() if isinstance(x, str) else x)

# CONVERSIONES A NUMÉRICAS
df['Monthly'] = pd.to_numeric(df['Monthly'], errors='coerce')
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')
df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
df['SeniorCitizen'] = pd.to_numeric(df['SeniorCitizen'], errors='coerce')

# CREAR CUENTAS_DIARIAS
df['cuentas_diarias'] = df['Monthly'] / 30

# RENOMBRAR COLUMNAS
rename_map = {
    'customerID': 'id_cliente',
    'Churn': 'evasi_n',
    'gender': 'genero',
    'SeniorCitizen': 'adulto_mayor',
    'Partner': 'pareja',
    'Dependents': 'dependientes',
    'tenure': 'antiguedad',
    'PhoneService': 'servicio_telefonica',
    'MultipleLines': 'multiples_lineas',
    'InternetService': 'servicio_internet',
    'OnlineSecurity': 'seguridad_en_linea',
    'OnlineBackup': 'copia_seguridad',
    'DeviceProtection': 'proteccion_dispositivos',
    'TechSupport': 'soporte_tecnico',
    'StreamingTV': 'tv_streaming',
    'StreamingMovies': 'peliculas_streaming',
    'Contract': 'tipo_contrato',
    'PaperlessBilling': 'facturacion_digital',
    'PaymentMethod': 'metodo_pago',
    'Monthly': 'facturacion_mensual',
    'Total': 'facturacion_total'
}
df = df.rename(columns=rename_map)

# RESUMEN DE DATOS LIMPIOS
print("\n" + "="*70)
print("DATOS LIMPIOS Y TRANSFORMADOS")
print("="*70)
print(f"Dimensiones finales: {df.shape}")
print(f"\nColumnas: {list(df.columns)}")
print(f"\nMuestra de datos:")
print(df.head(3))

# ANÁLISIS DESCRIPTIVO
print("\n" + "="*70)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("="*70)
numeric_cols = df.select_dtypes(include=['number']).columns
print(df[numeric_cols].describe())

# ANÁLISIS DE CHURN (EVASIÓN)
print("\n" + "="*70)
print("ANÁLISIS DE EVASIÓN (CHURN)")
print("="*70)
print("\nDistribución de Churn:")
print(df['evasi_n'].value_counts())
print("\nProporción (%):")
print(df['evasi_n'].value_counts(normalize=True) * 100)


# VISUALIZACIONES
print("\n" + "="*70)
print("CREANDO VISUALIZACIONES")
print("="*70)

# Gráfico de distribución de churn
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico de barras
churn_counts = df['evasi_n'].value_counts()
axes[0].bar(churn_counts.index, churn_counts.values, color=['#2ecc71', '#e74c3c'])
axes[0].set_title('Distribución de Evasión (Churn)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Evasión', fontsize=12)
axes[0].set_ylabel('Cantidad de Clientes', fontsize=12)
axes[0].grid(axis='y', alpha=0.3)

# Gráfico de pastel
churn_prop = df['evasi_n'].value_counts()
colors = ['#2ecc71', '#e74c3c']
axes[1].pie(churn_prop.values, labels=churn_prop.index, autopct='%1.1f%%', 
            colors=colors, startangle=90)
axes[1].set_title('Proporción de Evasión (Churn)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('analisis_churn.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfico guardado como 'analisis_churn.png'")
print("\n" + "="*70)
print("PROCESO COMPLETADO EXITOSAMENTE")
print("="*70)
