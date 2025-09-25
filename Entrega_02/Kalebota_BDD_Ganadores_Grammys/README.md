## Documentación

**Proceso de limpieza de datos**

1. Tomé la base de datos inicial y la convertí en una tabla para facilitar su visualización.
1. De esta tabla eliminé todos los datos que eran irrelevante para el análisis como: El número de ceremonia, los productores que trabajaron en un determinado disco/canción y el url que llevaba a la fuente de la información.
1. Luego, para facilitar la visualización de cada una de las categorías/años, hice que fuera posible filtrar cada una de las variables.
1. El primer filtro que apliqué fue el del año, dejando solo aquellos datos que van desde el 2000 hasta el 2024.
1. Luego, comencé a filtrar por categoría, separando cada una de ellas en una hoja distinta para poder cambiar información sin afectar la base de datos madre.
1. En cada categoría, me preocupé de que cada uno de los nominados y ganadores fuera correcto, además de simplificar la información eliminando datos como quienes escribieron las canciones, dejando solo al artista principal.
1. Una vez los datos de la base de datos principal estuvieran en orden, agregué dos nuevas columnas: "Género del artista o banda" y "Género del disco/canción", esta última solo en las categorías generales.
1. Ahí, agregué la información en cada una de las categorías que separé de la base de datos principal.



**Fuentes de datos utilizadas**

Para la mayor parte de esta información, la fuente utilizada fue [El sitio web de los Grammys](https://www.grammy.com/awards) donde está toda la información de todas las ceremonias. O sea, categorias, ganadores y nominados por año. 

El resto de la información, o sea el género de los artistas y la música, fue recopilada a través de búsquedas de internet para cada una de los artistas/canción/disco. Mucha de la información, como el género de un disco/canción viene de Wikipedia.

**Tres preguntas que se pueden responder con la base de datos**

1. ¿Cuántas mujeres han sido nominadas en la categoría de Grabación del Año en los últimos 25 años?
1. ¿Qué genero musical ha sido más premiado en la categoría de Álbum del Año en los últimos 25 años?
1.  ¿Qué artistas se repiten más en las categorías principales en los últimos 25 años?
