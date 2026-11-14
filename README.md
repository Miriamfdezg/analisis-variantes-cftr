# Análisis bioinformático de variantes del gen CFTR asociadas a fibrosis quística

## Descripción del proyecto

La fibrosis quística es una enfermedad genética autosómica recesiva causada por variantes patogénicas en el gen CFTR (Cystic Fibrosis Transmembrane Conductance Regulator). Este gen codifica una proteína de membrana que interviene principalmente en el transporte de iones cloruro y bicarbonato a través de las células epiteliales. Las alteraciones en su funcionamiento pueden afectar a distintos órganos, especialmente a los sistemas respiratorio y digestivo.
Las cinco variantes analizadas afectan a un mismo gen, CFTR, que codifica para un regulador de conductancia transmembrana para fibrosis quística, una única proteína de 1480 aminoácidos.

Este proyecto tiene como finalidad desarrollar un análisis bioinformático básico de variantes del gen CFTR relacionadas con la fibrosis quística, así como relacionar cada variante con su posición en la proteína y con su efecto en la función de la misma, utilizando información procedente de diversas bases de datos públicas y herramientas de programación científica.

## Objetivos

Objetivo general:

Analizar y comparar variantes genéticas del gen CFTR asociadas a fibrosis quística mediante un procedimiento bioinformático reproducible.

Objetivos específicos:

1. Consultar información genética y clínica del gen CFTR en bases de datos públicas.
  - Caracterizar la proteína CFTR a partir de UniProt: tamaño, dominios y función.
2. Seleccionar un conjunto de variantes relevantes, incluyendo F508del.
  - Localizar cada variante en un dominio de la proteína.
  - Relacionar cada variante con su efecto sobre la proteína y con la enfermedad.
  - Consultar estructuras experimentales de la proteína CFTR en el PDB y situar en ellas las posiciones de las variantes.
3. Organizar la información obtenida en archivos CSV y TXT.
4. Desarrollar un script en Python para procesar y resumir los datos obtenidos.
5. Documentar la metodología y los resultados del análisis.

## Metodología

El proyecto se ha desarrollado siguiendo las siguientes fases:

1. Recopilación de información: consulta de ClinVar, una base de datos del NCBI, para obtener información genética y clínica de cinco variantes del gen CFTR asociadas a fibrosis quística.
2. Caracterización de la proteína: descarga de la ficha de CFTR en UniProt (P13569) y extracción de su tamaño, función, dominios y enfermedades asociadas. Después se situó cada variante en el dominio correspondiente.
3. Consulta de estructuras: selección en el PDB de cuatro estructuras de CFTR, a partir de las enlazadas en UniProt, y captura de su visualización 3D con el visor Mol* de RCSB.
4. Preparación de los datos: selección de las variantes F508del, G542X, G551D, W1282X y N1303K y organización de sus identificadores, cambios moleculares y clasificaciones clínicas en un archivo CSV.
5. Procesamiento mediante Python: elaboración de un script para leer los datos y realizar un recuento de las variantes según su consecuencia molecular y clasificación clínica. La lectura de los datos y el recuento de consecuencias moleculares se comprobaron en Google Colab.
6. Interpretación de resultados: identificación de una deleción dentro del marco de lectura, dos variantes sin sentido y dos variantes de cambio de sentido. Los resultados obtenidos se incorporaron a la carpeta resultados del repositorio.

Las clasificaciones clínicas utilizadas proceden de ClinVar y no constituyen una validación experimental propia. El análisis se limita a las cinco variantes seleccionadas.

## Estructura del repositorio

- datos/: archivos con la información de las variantes genéticas
- scripts/: código utilizado para procesar los datos.
- resultados/: archivos generados durante el análisis y capturas de las estructuras proteicas.
- documentacion/: descripción detallada de la metodología y las fuentes consultadas.
- información adicional/: resumen de la proteína y relación con las variantes
- README.md: presentación general del proyecto.
- LICENSE: licencia del repositorio.

## Herramientas y recursos

- Python: procesamiento y análisis básico de los datos.
- Google Colab: ejecución y comprobación del análisis en Python. (Debido a que en momentos no he contado con mi ordenador portatil)
- Git y GitHub: organización del repositorio y control de versiones.
- NCBI: acceso a recursos de información genética.
- ClinVar: consulta de variantes genéticas y sus interpretaciones clínicas.
- UniProt: información de la proteína CFTR (P13569).
- RCSB PDB: consulta y visualización de estructuras 3D de la proteína.

## Estado del proyecto

El repositorio contiene los datos de cinco variantes del gen CFTR obtenidos de ClinVar, organizados en un archivo CSV, junto con un script de Python para procesarlos y un resumen de los resultados. Se ha comprobado la lectura de los datos y el recuento de las consecuencias moleculares. También se ha documentado la metodología empleada y las fuentes consultadas. Se ha documentado la ficha de la proteína CFTR (UniProt) y se han seleccionado cuatro estructuras experimentales del PDB que cubren las posiciones de las cinco variantes.

## Licencia

Este proyecto se distribuye bajo la licencia MIT, incluida en el archivo LICENSE.

## Instrucciones de uso

Para utilizar los archivos del proyecto, se puede descargar el repositorio desde GitHub mediante la opción Code y Download ZIP. En la carpeta datos se encuentra el archivo variantes_cftr.csv, que contiene la información de las cinco variantes del gen CFTR seleccionadas a partir de ClinVar.

El archivo analizar_variantes.py, situado en la carpeta scripts, permite leer los datos y realizar un recuento de las variantes según su consecuencia molecular y clasificación clínica. Para ejecutarlo es necesario disponer de Python 3 y mantener la estructura original de carpetas del repositorio.

El programa está preparado para generar un archivo CSV con el resumen de las consecuencias moleculares en la carpeta resultados.

## Comprobación del funcionamiento

Se ha comprobado el funcionamiento del repositorio utilizando comandos de Git desde el entorno de Google Colab. Mediante `git clone` se ha descargado el proyecto, con `git status` se ha verificado el estado de la rama principal y con `git log` se ha consultado el historial de commits.

También se ha ejecutado el script `analizar_variantes.py` con Python, obteniendo un total de cinco variantes del gen CFTR: una deleción en marco, dos variantes sin sentido y dos de cambio de sentido. Las cinco presentan clasificación patógena según los datos recopilados de ClinVar.

La ejecución ha finalizado correctamente y ha permitido comprobar el funcionamiento del análisis.
