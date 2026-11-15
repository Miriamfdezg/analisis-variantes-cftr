# Estructuras experimentales de CFTR (PDB)

## Qué es el PDB
El Protein Data Bank (PDB, rcsb.org) es la base de datos que reúne las estructuras tridimensionales de proteínas determinadas experimentalmente, principalmente por cristalografía de rayos X, microscopía electrónica criogénica (cryo-EM) y resonancia magnética nuclear (RMN).

## Cómo se seleccionaron
La ficha de UniProt de CFTR (P13569) enlaza 58 estructuras del PDB: unas 35 de rayos X, 22 de cryo-EM y 1 de RMN. Se han seleccionado cuatro que permiten situar las cinco variantes del proyecto:

- Dos estructuras de la proteína completa (residuos 1-1480), para ver las variantes en el contexto de toda la proteína.
- Una estructura del dominio NBD1 (residuos 387-646), que contiene las posiciones 508, 542 y 551.
- Una estructura del dominio NBD2 (residuos 1193-1427), que contiene las posiciones 1282 y 1303.

Para cada tipo se eligió la de mejor resolución disponible entre las listadas por UniProt.

## Estructuras seleccionadas
| Código PDB | Método | Resolución | Residuos | Título | Año | Ligandos |
|---|---|---|---|---|---|---|
| 9MXL | cryo-EM | 2.10 Å | 1-1480 | [título] | [año] | [ligandos] |
| 7SVD | cryo-EM | 2.70 Å | 1-1480 | [título] | [año] | [ligandos] |
| 2PZE | Rayos X | 1.70 Å | 387-646 | [título] | [año] | [ligandos] |
| 3GD7 | Rayos X | 2.70 Å | 1193-1427 | [título] | [año] | [ligandos] |

Método, resolución y residuos proceden de UniProt; título, año y ligandos, de la ficha de cada estructura en RCSB.

## Qué estructura cubre cada variante
| Variante | Posición | Dominio | Estructuras que la incluyen |
|---|---|---|---|
| F508del | 508 | NBD1 | 9MXL, 7SVD, 2PZE |
| G542X | 542 | NBD1 | 9MXL, 7SVD, 2PZE |
| G551D | 551 | NBD1 | 9MXL, 7SVD, 2PZE |
| W1282X | 1282 | NBD2 | 9MXL, 7SVD, 3GD7 |
| N1303K | 1303 | NBD2 | 9MXL, 7SVD, 3GD7 |

La cobertura se ha deducido comparando la posición de cada variante con el rango de residuos de cada estructura. Que una estructura incluya una posición no significa que contenga la variante: ver apartado de limitaciones.

## Figuras
![Dominio NBD1 de CFTR (PDB 2PZE)](../resultados/figuras/2pze_nbd1.png)

*Figura 1. Dominio NBD1 de CFTR, estructura 2PZE del PDB (rayos X, 1.70 Å). [Qué se resalta en la imagen, si algo]. Captura realizada con el visor Mol* de RCSB el DD/MM/AAAA.*

![Dominio NBD2 de CFTR (PDB 3GD7)](../resultados/figuras/3gd7_nbd2.png)

*Figura 2. Dominio NBD2 de CFTR, estructura 3GD7 del PDB (rayos X, 2.70 Å). [Qué se resalta]. Captura realizada con el visor Mol* de RCSB el DD/MM/AAAA.*

![CFTR completa (PDB 9MXL)](../resultados/figuras/9mxl_completa.png)

*Figura 3. Proteína CFTR completa, estructura 9MXL del PDB (cryo-EM, 2.10 Å). Captura realizada con el visor Mol* de RCSB el DD/MM/AAAA.*

## Observaciones
- Las cinco posiciones afectadas por las variantes están cubiertas por estructuras experimentales, por lo que pueden localizarse sobre la proteína real y no solo sobre un modelo.
- En esta selección, las estructuras de dominios aislados (2PZE, 3GD7) son de rayos X, y las de la proteína completa, de cryo-EM.
- La estructura 3GD7 termina en el residuo 1427, mientras que el dominio NBD2 llega hasta el 1443 según UniProt. Aun así, incluye las posiciones 1282 y 1303.
- [Una observación propia: por ejemplo, qué diferencias ves entre el dominio solo y dentro de la proteína completa.]

## Limitaciones
- Cada estructura representa la proteína en un estado concreto (con o sin ATP, con o sin fármaco, con una construcción determinada). [Comprobar y anotar para cada una cuál es.]
- [Comprobar en RCSB si alguna de las estructuras contiene una de las variantes del proyecto (por ejemplo, un NBD1 con la deleción F508). Si no, indicar que las estructuras corresponden a la proteína sin la variante y que solo se ha situado la posición.]
- Las figuras son capturas del visor y no un análisis estructural cuantitativo.

## Fuentes
- UniProtKB P13569, versión 287 (04-nov-2026). Consultada el DD/MM/AAAA.
- RCSB PDB (rcsb.org), consultado el DD/MM/AAAA. Estructuras: 9MXL, 7SVD, 2PZE, 3GD7.
- [Referencia del artículo de cada estructura: autores, revista, año.]
