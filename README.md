# 📊 Análisis de Evasión de Clientes (Churn) - TelecomX Data

## Descripción del Proyecto

Este proyecto realiza un **análisis descriptivo completo** de los datos de clientes de TelecomX, enfocándose en entender y cuantificar el fenómeno de **evasión de clientes (Churn)**. Se incluyen estadísticas descriptivas, visualizaciones, análisis de patrones categóricos y numéricos, así como recomendaciones estratégicas para reducir la tasa de abandono.

## 📋 Contenido del Análisis

1. **Estadísticas Descriptivas**: Media, mediana, desviación estándar, cuartiles, asimetría y curtosis
2. **Distribución de Churn**: Proporción de clientes que se dieron de baja vs. permanecieron
3. **Análisis Categórico**: Tasas de evasión por género, contrato, tipo de internet, método de pago, etc.
4. **Análisis Numérico**: Comparación de variables numéricas entre clientes que cancelaron y retuvieron
5. **Visualizaciones**: 7 gráficos de alta calidad (histogramas, pie charts, heatmap, boxplots, violin plots, matriz de impacto)
6. **Recomendaciones Estratégicas**: Acciones priorizadas para reducir el churn

## 🔧 Instalación y Configuración

### Requisitos Previos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
pip install requests pandas numpy matplotlib seaborn jupyter
```

### Librerías Necesarias

| Librería | Versión | Uso |
|----------|---------|-----|
| requests | 2.32.5+ | Descargar datos desde API |
| pandas | 3.0.1+ | Manipulación y análisis de datos |
| numpy | 2.4.2+ | Operaciones numéricas |
| matplotlib | 3.10.8+ | Visualizaciones estáticas |
| seaborn | 0.13.0+ | Gráficos estadísticos avanzados |
| jupyter | 1.0.0+ | Entorno de notebook interactivo |

## 🚀 Cómo Ejecutar el Proyecto

### Opción 1: Ejecutar el Notebook Completo

```bash
jupyter notebook analisis_churn_completo.ipynb
```

Luego abre el archivo en el navegador y ejecuta todas las celdas con:
- Menú: `Cell` → `Run All`
- O atajo: `Ctrl+Shift+Enter`

### Opción 2: Ejecutar desde Terminal con nbconvert

```bash
jupyter nbconvert --to notebook --execute analisis_churn_completo.ipynb
```

### Opción 3: Ejecutar Script de Carga de Datos

```bash
python load_data.py
```

## 📁 Estructura del Proyecto

```
challenge2-data-science/
├── analisis_churn_completo.ipynb          # Notebook principal con análisis completo
├── load_data.py                           # Script de carga y preparación de datos
├── README.md                              # Este archivo
└── output/                                # Carpeta de visualizaciones generadas (creada automáticamente)
    ├── 01_distribucion_numericas.png      # Histogramas de variables numéricas
    ├── 02_distribucion_churn.png          # Gráficos de distribución de churn
    ├── 03_churn_categoricas.png           # Tasas de churn por variables categóricas
    ├── 04_heatmap_evasion.png             # Heatmap de top 20 categorías
    ├── 05_boxplot_numericas.png           # Box plots comparativos
    ├── 06_violin_numericas.png            # Violin plots por estado de churn
    └── 07_matriz_impacto_esfuerzo.png    # Matriz de impacto vs. esfuerzo
```

## 📊 Datos Utilizados

**Fuente:** GitHub API  
**URL:** `https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json`

**Dimensiones:** 7,267 clientes × 22 variables

**Variables Clave:**
- Demográficas: Género, Antigüedad (meses), Adulto Mayor
- Servicios: Tipo Internet, Telefonía, Facturación Digital
- Económicas: Facturación Mensual, Facturación Total
- Contractuales: Tipo de Contrato, Método de Pago
- Objetivo: Churn (sí/no)

## 🔍 Resultados Clave

- **Tasa de Churn Total:** 25.7%
- **Clientes Retenidos:** 71.2%
- **Datos Desconocidos:** 3.1%

### Factores de Riesgo (Mayor Evasión):
1. Contrato mes a mes (41.3%)
2. Internet Fibra Óptica (40.6%)
3. Pago Electrónico (43.8%)

### Factores Protectores (Menor Evasión):
1. Contrato de 2 años (2.8%)
2. Sin Internet (7.1%)
3. Clientes con dependientes (14.9%)

## ⚠️ Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'seaborn'`
```bash
pip install seaborn
```

### Error: `NameError: name 'requests' is not defined`
Asegúrate de que la celda de importaciones se ejecutó primero:
```python
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Error: Conexión a API fallida
- Verifica tu conexión a internet
- Confirma que GitHub no está bloqueado
- Intenta acceder a la URL directamente en el navegador

### Las visualizaciones no se muestran
- Asegúrate de estar en un Jupyter Notebook o JupyterLab
- Ejecuta: `%matplotlib inline` en una celda antes de los gráficos

### Archivo JSON vacío
El archivo se carga correctamente si la respuesta HTTP es 200. Verifica:
```python
response = requests.get(url)
print(response.status_code)  # Debe ser 200
print(len(response.json()))  # Debe ser 7267
```

## 📈 Interpretación de Gráficos

### 01_distribucion_numericas.png
Muestra la distribución de 5 variables numéricas. La mayoría son asimétricas (sesgadas a la derecha).

### 02_distribucion_churn.png
Incluye: gráfico de barras (cantidad), pie chart (proporción) y barras horizontales con porcentajes.

### 03_churn_categoricas.png
8 paneles mostrando tasas de evasión por variable. Colores indican riesgo: rojo (>30%), naranja (>20%), verde (<20%).

### 04_heatmap_evasion.png
Top 20 categorías ordenadas por tasa de evasión de mayor a menor.

### 05_boxplot_numericas.png
Comparación de distribuciones entre clientes que cancelaron (rojo) vs. retuvieron (verde).

### 06_violin_numericas.png
Distribuciones de probabilidad más detalladas por estado de churn.

### 07_matriz_impacto_esfuerzo.png
7 iniciativas de retención posicionadas por impacto (eje Y) vs. esfuerzo (eje X). Los cuadrantes indican prioridad.

## 💡 Recomendaciones Principales

1. **🔴 CRÍTICA - Período de Onboarding (Primeros 6 meses)**
   - Implementar programa intensivo de onboarding
   - Impacto esperado: 8-12% reducción en churn

2. **🟠 ALTA - Promover Contratos Largos**
   - Incentivar migración de mes-a-mes a contratos de 1-2 años
   - Impacto esperado: 15-20% reducción

3. **🟡 MEDIA - Mejorar Soporte Fibra Óptica**
   - Aumentar calidad de servicio para clientes de fibra
   - Impacto esperado: 5-8% reducción

## 📝 Notas Técnicas

- **Lenguaje:** Python 3.14
- **Ambiente:** Jupyter Notebook
- **Manejo de Datos:** JSON anidado extraído manualmente para preservar integridad
- **Valores Faltantes:** Tratados con "desconocido" (categóricos) o mediana (numéricos)
- **Normalización:** Strings convertidos a minúsculas y sin espacios extras

## 👤 Autor

Análisis realizado como parte del desafío "Challenge 2 - Data Science" de LATAM

## 📄 Licencia

Datos públicos de TelecomX - Uso educativo

---

**Última actualización:** Marzo 2026  
**Estado:** ✅ Completado y validado
