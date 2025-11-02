# code/kaggle.py

import kagglehub
import shutil
from pathlib import Path


def descargar_bd(dataset: str, carpeta_destino: str) -> str:
    """
    Descarga un dataset desde Kaggle usando kagglehub y mueve los archivos
    a la carpeta destino especificada por el usuario

    Parámetros:
    - dataset (str): Nombre del dataset en formato 'autor/nombre_dataset'
        Ejemplo: 'ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset'
    - carpeta_destino (str): Ruta donde se copiarán los archivos del dataset

    Retorno:
    - str: Confirmación y ruta donde se guardaron los archivos del dataset
    """
    # Descarga del dataset:
    print(f"Descargando dataset '{dataset}' desde KaggleHub...")
    ruta_origen = Path(kagglehub.dataset_download(dataset))

    # Preparación de la carpeta destino:
    ruta_destino = Path(carpeta_destino).expanduser().resolve()
    # Crea la carpeta si no existe:
    ruta_destino.mkdir(parents=True, exist_ok=True)

    # Copia los archivos:
    print(f"Copiando archivos a: {carpeta_destino}")
    for archivo in ruta_origen.rglob("*"):
        if archivo.is_file():
            destino_archivo = ruta_destino/archivo.name
            shutil.copy2(archivo, destino_archivo)

    # Indica dónde se ha guardado:
    print(f"Dataset descargado en: {carpeta_destino}")
