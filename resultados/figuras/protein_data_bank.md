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
| Código PDB | Método | Resolución | Residuos |
|---|---|---|---|---|---|---|
| 9MXL | cryo-EM | 2.10 Å | 1-1480 |
| 7SVD | cryo-EM | 2.70 Å | 1-1480 |
| 2PZE | Rayos X | 1.70 Å | 387-646 |
| 3GD7 | Rayos X | 2.70 Å | 1193-1427 |

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

## Observaciones
- Las cinco posiciones afectadas por las variantes están cubiertas por estructuras experimentales, por lo que pueden localizarse sobre la proteína real y no solo sobre un modelo.
- En esta selección, las estructuras de dominios aislados (2PZE, 3GD7) son de rayos X, y las de la proteína completa, de cryo-EM.
- La estructura 3GD7 termina en el residuo 1427, mientras que el dominio NBD2 llega hasta el 1443 según UniProt. Aun así, incluye las posiciones 1282 y 1303.

## Fuentes
- UniProtKB P13569, versión 287 (04-nov-2026). Consultada el 14/11/2026.
- RCSB PDB (rcsb.org), consultado el 14/11/2026. Estructuras: 9MXL, 7SVD, 2PZE, 3GD7.
