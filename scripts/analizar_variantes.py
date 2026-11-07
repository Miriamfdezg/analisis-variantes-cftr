
import csv
from pathlib import Path
from collections import Counter

# Rutas de los archivos
carpeta_proyecto = Path(__file__).resolve().parent.parent
archivo_datos = carpeta_proyecto / "datos" / "variantes_cftr.csv"
archivo_resultados = carpeta_proyecto / "resultados" / "resumen_variantes.csv"

# Leer los datos del gen CFTR
with open(archivo_datos, "r", encoding="utf-8-sig", newline="") as archivo:
    lector = csv.DictReader(archivo)
    variantes = list(lector)

if not variantes:
    raise ValueError("El archivo no contiene variantes.")

# Contar los tipos de variantes
tipos = Counter(
    variante["consecuencia_molecular"] for variante in variantes
)

# Contar las clasificaciones clínicas
clasificaciones = Counter(
    variante["clasificacion_clinica"] for variante in variantes
)

# Mostrar los resultados
print("Análisis de variantes del gen CFTR")
print("Total de variantes:", len(variantes))

print("\nConsecuencias moleculares:")
for tipo, cantidad in tipos.items():
    print(tipo.replace("_", " "), ":", cantidad)

print("\nClasificación clínica:")
for clasificacion, cantidad in clasificaciones.items():
    print(clasificacion, ":", cantidad)

# Guardar los resultados
archivo_resultados.parent.mkdir(parents=True, exist_ok=True)

with open(archivo_resultados, "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["consecuencia_molecular", "numero_variantes"])

    for tipo, cantidad in tipos.items():
        escritor.writerow([tipo, cantidad])

print("\nAnálisis finalizado.")

