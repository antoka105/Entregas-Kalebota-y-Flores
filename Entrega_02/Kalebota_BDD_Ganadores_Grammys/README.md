## Documentación

**Proceso de limpieza de datos**

1. Tomé la base de datos inicial, que estaba en formato CSV, y la convertí en una tabla en excel para facilitar su visualización. Esto porque el formato inicial se me hacía dificil de navegar, sobretodo por la gran cantidad de datos con los que se estaba trabajando. 
1. De esta tabla eliminé todos los datos que eran irrelevante para el análisis como: El número de ceremonia (Ya que solo nos importa el año en el que se realizó), los productores que trabajaron en un determinado disco/canción (Para simplificar la visualización de la información nos enfocamos solo en el artista principal) y el url que llevaba a la fuente de la información.
1. Luego, para facilitar la visualización de cada una de las categorías/años, hice que fuera posible filtrar cada una de las variables. O sea, poder filtrar por año de la ceremonia, por categoría, por ganadores o solo nominados y, hasta, por artista.
1. El primer filtro que apliqué fue el del año, dejando solo aquellos datos que van desde el 2000 hasta el 2024. Acá es importante considerar que si estamos trabajando con datos de la ceremonia más reciente, 2025, pero está catalogada como 2024 porque se premia la música de ese año. 
1. Luego, comencé a filtrar por categoría, separando cada una de ellas en una hoja distinta para poder cambiar información sin afectar la base de datos madre. Decidí enfocarme en las categorías principales (Álbum del Año, Canción del Año, Grabación del Año y Mejor Artista Nuevo) y elegí los géneros musicales que me parecían más relevantes en la categoría de mejor disco (Alternativo, Pop, Rock y Rap/Hip-Hop). Esto para no solo tener una visión de las categorías más importantes, sino también saber si existen distintos parametros de votación dependiendo del género muscial que esté en juego.
1. En cada categoría, me preocupé de que cada uno de los nominados y ganadores fuera correcto, además de simplificar la información eliminando datos como quienes escribieron las canciones, dejando solo al artista principal. Este paso lo tuve que realizar a mano, ya que en categorías como Mejor Artista Nuevo no hay ningún valor en la columna de disco y canción lo que hizo que algunas filas tuvieran información que no era correcta (Como que el nombre del disco y del artista no coincidieran).
1. Una vez los datos de la base de datos principal estuvieran en orden, agregué dos nuevas columnas: "Género del artista o banda" y "Género del disco/canción", esta última solo en las categorías generales. Con esto, agregar variables que van más allá de si el artista ganó o perdió y con que disco o canción. Considerp que estas nuevas columnas pueden significar descubrimientos importantes para la investigación. Este paso lo realicé a mano y con datos de múltiples sitios de internet, aunque algunos, como el género de artistas populares, los pude hacer sin necesidad de consultar.
1. Con estas nuevas columnas creadas, agregué la  nueva información a cada una de las hojas que había separado de la base de datos inicial. Cabe decir que la columna de "Género del disco/canción", obviamente, no fue incorporada en las categorías que son de un género específico, ya que el mismo nombre de la categoría resuelve esa incógnita. Particularmente cuando se trató de definir a un disco/canción con un género traté de ser bastante general, para así facilitar el contraste de información.



**Fuentes de datos utilizadas**

Para la mayor parte de esta información, la fuente utilizada fue [El sitio web de los Grammys](https://www.grammy.com/awards) donde está toda la información de todas las ceremonias. O sea, categorias, ganadores y nominados por año. 

El resto de la información, o sea el género de los artistas y la música, fue recopilada a través de búsquedas de internet para cada una de los artistas/canción/disco. Mucha de la información, como el género de un disco/canción viene de Wikipedia.

**Tres preguntas que se pueden responder con la base de datos**

1. ¿Cuántas mujeres han sido nominadas en la categoría de Grabación del Año en los últimos 25 años?
1. ¿Qué genero musical ha sido más premiado en la categoría de Álbum del Año en los últimos 25 años?
1.  ¿Qué artistas se repiten más en las categorías principales en los últimos 25 años?
