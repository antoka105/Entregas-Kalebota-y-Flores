## Documentación

**Proceso de limpieza de datos**
1. Visualicé cuales eran las categorías existentes dentro de la base de datos: nombres de canciones, artistas, posiciones semanales, fechas, semanas en el chart.
1. Tome la base de datos e hice una copia dentro de Visual Studio Code para no dañar la base de datos original. 
1. Normalicé el nombre de las columnas, esto más que nada, por temas estéticos más que por temas técnicos a futuro. Esto a traves de Visual Studio Code mediante el script. Esto facilita la manipulación de datos en Python y evita errores al escribir código con nombres inconsistentes.
1. De esta base de datos original cambie los datos de la columna "date" y la cambie a tipo fecha. Esto permite hacer análisis temporales, gráficos de evolución y filtros por año o mes.
1. Convertí las columnas, "rank"; "last_week"; "peak_position"; "week_in_charts" a columnas númericas, ya que los datos dentro de estas columnas deben ser analizados como datos cuantitativos, no cualitativos como en el trabajo de mi compañera y en las otras columnas dentro de la base de datos. 
1. Luego elimine los datos que estuvieran duplicados, ya que podrían generar complicaciones en la utilización de datos, luego cuando diseñemos la página web.
1. Además, de rellenar los valores faltantes, que sí existían en esta base de datos a diferencia de otras, con un "#". Al momento de analizar los datos se nos falicitará hacerlo, ya que existirá este signo diferenciador. Si es que habría reemplazado con 0, por ejemplo, creo que se podría ver alterada la base de datos y nos confudiría más a futuro. 
1. También, decidimos filtrar los datos en una determinada época, ya que la base de datos original era de un tamaño mucho mayor, lo cual dificultaba nuestro trabajo. Decidimos reducirla a solo los años 2000 a 2025, ya que esto disminuye también la carga computacional y facilita el análisis visual. A pesar de esto contamos con una gran cantidad de datos en esta base (133.900 entries, según Google Collab)
1. Por último, procuré verificar que los datos se encontraban correctamente ordenados a través de Google Collab.
1. Esta documentación facilita, además, que otro integrante del grupo pueda trabajar con esta base de datos y adaptarla a otro tipo de análisis. 


**Fuentes de datos utilizados**

Toda la información de esta base de datos proviene de la página oficial de la lista Billboard Hot 100, ya que la base de datos solo se limita a mostrar datos específicos de ese ranking. Incluso, la base de datos original se actualiza constantemente para seguir recolectando datos actuales.
Nosotras por un tema de practicidad decidimos dejar los datos hasta el momento que enviamos la Entrega_01. 

**Tres preguntas que se pueden hacer responder con la base de datos**
1. ¿Cuántas veces ha estado X artista en la lista Billboard Hot 100? ¿Por cuánto tiempo?
2. ¿Cuál ha sido la tendencia musical que ha estado mejor posicionada en la lista Billboard Hot 100? ¿Ha ido cambiando a lo largo de los años?
3. ¿Cuál ha sido el máximo puesto que ha tenido X artista/canción en la lista Billboard Hot 100? ¿Se ha repetido?
   
