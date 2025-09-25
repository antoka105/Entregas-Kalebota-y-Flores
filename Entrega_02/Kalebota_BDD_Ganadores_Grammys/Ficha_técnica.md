**Fuente de los datos**

La base de datps inicial fue publicada en el sitio Kaggle por John Pendenque, un especialista en Python que colecciona data [(Link BDD)](https://www.kaggle.com/datasets/johnpendenque/grammy-winners-and-nominees-from-1965-to-2024). La información está sacada directamente del sitio web de los Grammys.

En cuanto a las nuevas bases de datos limpias, a la base original agregamos información que será valiosa para nuestra investigación como el género del artista o banda (Mujer, Hombre o Mixto) y el género de la canción o álbum nominado en el caso de las categorías generales. Esta información tiene múltiples orígenes como Wikipedia, sitios especializados de música y otras publicaciones, para así tener un consenso en torno a cosas como el género de una canción/disco.



**Metodología de la construcción de la base**

La base de datos principal se realizó a partir del sitio web de los Grammys, donde se encuentran todos los ganadores de todas las categorías de cada una de las ceremonias. A partir de este sitio, el autor de la base de datos creo un robot con Selenuim llamado Kryptone que se utiliza para sacar data compleja de sitios web.

La información extra que agregamos a esta base de datos se hizo a mano, buscando cada uno de los datos necesarios.

**Alcance de los datos**

El alcance de los datos es desde el 2000 hasta el 2025. Las categorías es particular que fueron seleccionadas son:
- Álbum del Año
- Canción del Año
- Grabación del Año
- Mejor Artista Nuevo
- Mejor Álbum Pop
- Mejor Álbum Rock
- Mejor Álbum Rap
- Mejor Álbum Alternativo


**Característica de los datos**

Según su obtención: De investigación de campo.

Según su estado: Procesados

Según su fuente: Abierta.

Según su categoría: Estructurados.

Según su naturaleza: Cualitativos.



**Variables incorporadas: variable | descripción**

Las variables incorporadas en esta base de datos son:
- Año: De que año es cierto ganador/nominado.
- Categoría: La categoría en la que se encuentra cada ganador/nominado.
- Artista: Quién es el artista nominado, considerando solo el artista principal. O sea, dejando de lado escritores y productores.
- Disco o canción: El proyecto que se encuentra nominado en la categoría.
- Ganador: Si el artista/proyecto señalado ganó o no en la categoría determinada. Señalado por "True" si es el ganador y "False" si no lo es.
- Género del artista o banda: El género de la artista o banda nominada, señalado por M (mujer), H (hombre) o MIXTO.
- Género de la canción/disco: El tipo de música en el que se enmarca el proyecto nominado, muchas veces simplificado para facilitar el contraste de la información.

**Otras observaciones que tengan sobre la base**

La variable de "Genero de la canción/disco" solo se encuentra en las categorías generales, ya que estas no se enmarcan en un solo género.

Para que el género de una banda se considere mixto debe haber por lo menos una persona de cada sexo en el grupo. Aunque la mayoría sean del sexo opuesto igual fue considerado como mixto.
