Metodología del proyecto

Para este proyecto he seleccionado cinco variantes del gen CFTR relacionadas con la fibrosis quística: F508del, G542X, G551D, W1282X y N1303K. La información se ha obtenido de ClinVar, una base de datos pública del NCBI que recoge variantes genéticas y sus interpretaciones clínicas.

He consultado individualmente los registros de las cinco variantes para identificar sus cambios en el ADN, las alteraciones que producen en la proteína y su clasificación clínica para fibrosis quística. Los datos seleccionados se han organizado en el archivo variantes_cftr.csv, situado en la carpeta datos del repositorio.

Para procesar esta información he preparado un programa en Python que permite leer el archivo CSV y contar las variantes según su consecuencia molecular y clasificación clínica. He utilizado las bibliotecas csv y collections, que forman parte de la biblioteca estándar de Python.

La lectura de los datos y el recuento de las consecuencias moleculares se han comprobado en Google Colab. Entre las cinco variantes seleccionadas se ha identificado una deleción dentro del marco de lectura, dos variantes sin sentido y dos de cambio de sentido. Este recuento se ha incorporado al archivo resumen_variantes.csv.

Los resultados corresponden únicamente a las cinco variantes seleccionadas y no representan la frecuencia de estas alteraciones en la población con fibrosis quística.

Fuentes consultadas:

ClinVar, National Center for Biotechnology Information (NCBI). https://www.ncbi.nlm.nih.gov/clinvar/

Registros de las variantes:

F508del: https://www.ncbi.nlm.nih.gov/clinvar/variation/7105/

G542X: https://www.ncbi.nlm.nih.gov/clinvar/variation/7115/

G551D: https://www.ncbi.nlm.nih.gov/clinvar/variation/7120/

W1282X: https://www.ncbi.nlm.nih.gov/clinvar/variation/7129/

N1303K: https://www.ncbi.nlm.nih.gov/clinvar/variation/7136/

Fecha de consulta: 7 de noviembre de 2026.
