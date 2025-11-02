# PEC 2 - Visualización de Datos

**Autor:** Jesús F García Gavilán  
**Fecha:** 31 de octubre de 2025  
**Asignatura:** M2.859 Visualización de Datos - Máster en Ciencia de Datos (UOC)

## 📋 Descripción del Proyecto

Este proyecto corresponde a la segunda Prueba de Evaluación Continua (PEC2) de la asignatura de Visualización de Datos. El objetivo es crear tres visualizaciones diferentes utilizando técnicas específicas asignadas:

1. **Histograma** - Para visualizar distribuciones de datos
2. **Diagrama de Red (Network Diagram)** - Para mostrar interconexiones entre variables
3. **Gráfico en Espiral (Spiral Plot/Condogram)** - Para representar series temporales

## 📊 Datasets Utilizados

### 1. Life Style Data
- **Fuente:** [Kaggle - Life Style Data](https://www.kaggle.com/datasets/jockeroika/life-style-data)
- **Registros:** 20,000
- **Variables:** 54
- **Descripción:** Datos sobre estilo de vida y actividad física de individuos activos
- **Uso:** Histograma y Diagrama de Red

### 2. Daily Delhi Climate
- **Fuente:** [Kaggle - Daily Climate Time Series Data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data)
- **Registros:** 1,462 (2013-2016)
- **Variables:** 5
- **Descripción:** Datos climáticos diarios de Delhi
- **Uso:** Gráfico en Espiral

## 🎨 Visualizaciones

### 1. Histograma
**Variable analizada:** Balance calórico (`cal_balance`)  
**Descripción:** Muestra la distribución del balance calórico (diferencia entre calorías ingeridas y gastadas) en 20,000 personas activas.

### 2. Diagrama de Red
**Variables analizadas:** Todas las variables numéricas con correlación |r| ≥ 0.7  
**Método:** Correlación de Spearman  
**Descripción:** Red de correlaciones entre 21 variables de estilo de vida, mostrando conexiones positivas (azul) y negativas (rojo).

### 3. Gráfico en Espiral (Condogram)
**Variables analizadas:** Humedad media mensual (2013-2016)  
**Descripción:** Visualización circular tipo heat map que muestra la distribución de humedad media por mes a lo largo de 4 años.

## 📁 Estructura del Proyecto

```
PEC_2_VdD/
├── code.qmd              # Documento principal Quarto con todo el análisis
├── code.html             # Versión HTML renderizada del análisis
├── style.css             # Estilos personalizados para el documento
├── preambulo.tex         # Configuración LaTeX para PDF
├── README.md             
├── .gitignore            # Configuración de Git
│
├── database/             # Datos del proyecto
│   ├── raw/             # Datos originales descargados
│   └── clean/           # Datos procesados
│
├── figuras/             # Visualizaciones generadas
│   ├── PEC2_vdd_histograma.png
│   ├── PEC2_vdd_red_v2.png
│   └── PEC2_vdd_congram_v3.png
│
└── py/                  # Módulos Python
    ├── __init__.py
    └── kaggle.py        # Función para descargar datasets de Kaggle
```

## 🛠️ Tecnologías y Librerías

### Python
- `kagglehub` - Descarga de datasets
- `reticulate` (desde R) - Integración Python-R

### R
**Manipulación de datos:**
- `readr`, `janitor`, `dplyr`, `tidyr`, `stringr`, `lubridate`, `rio`

**Visualización:**
- `ggplot2` - Gráficos base
- `ggraph`, `tidygraph` - Diagramas de red
- `visNetwork`, `igraph` - Redes interactivas
- `gridExtra`, `grid` - Composición de gráficos
- `kableExtra` - Tablas
- `viridis` - Paletas de color

## 🚀 Instalación y Uso

### Requisitos Previos
- R (≥ 4.0)
- RStudio
- Quarto CLI
- Python 3.x
- Cuenta de Kaggle con API configurada

### Configuración del Entorno

1. **Clonar el repositorio:**
```bash
git clone <url-del-repositorio>
cd PEC_2_VdD
```

2. **Configurar credenciales de Kaggle:**
   - Obtener API token de Kaggle (kaggle.json)
   - Colocar en `~/.kaggle/kaggle.json` (Linux/Mac) o `C:\Users\<usuario>\.kaggle\kaggle.json` (Windows)

3. **Instalar paquetes de R:**
```r
# El código se encarga de instalar automáticamente el entorno virtual de Python
# Los paquetes de R se pueden instalar con:
install.packages(c("reticulate", "readr", "janitor", "dplyr", "tidyr", "stringr", "lubridate", "ggplot2", "kableExtra", "gridExtra", "grid", "ggraph", "tidygraph", "visNetwork", "igraph", "rio"))
```

4. **Renderizar el documento:**
```bash
quarto render code.qmd
```

O desde RStudio: Abrir `code.qmd` y hacer clic en "Render"

## 📈 Resultados

Las visualizaciones generadas demuestran:

- **Histograma:** El balance calórico en personas activas sigue una distribución aproximadamente normal con una media ligeramente positiva.

- **Diagrama de Red:** Variables relacionadas con el peso, IMC, y composición corporal muestran fuertes correlaciones positivas. Variables de gasto calórico se agrupan en clusters separados.

- **Gráfico en Espiral:** La humedad en Delhi muestra patrones estacionales claros, con mayor humedad en los meses de monzón (julio-septiembre).

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver más detalles a continuación:

```
MIT License

Copyright (c) 2025 Jesús F García Gavilán

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Nota:** Este proyecto utiliza datasets de Kaggle que están sujetos a sus propias licencias. Por favor, consulta las licencias de los datasets en sus respectivas páginas de Kaggle.

## 📧 Contacto

**Autor:** gavilanbiost@gmail.com

---

*Última actualización: 31 de octubre de 2025*
