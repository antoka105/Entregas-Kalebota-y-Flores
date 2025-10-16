**Explicación proceso de visualización**

1. Para comenzar el proceso de crear la visualización, subí la base de datos, ya limpia y ordenada, de la categoría de Álbum del Año a Google Colab. 
1. Luego de subirla, cargué los datos y renombré algunas columnas que tenían caracteres borrados, ya que se reemplazaron las letras con tílde por un signo de interrogación. También tuve que cambiar un valor dentro de la columna de "Género disco", ya que en el género de Reggaetón también se había reemplazado la letra con tilde por un signo de interrogación. Todo esto por una cosa de estética más que nada, ya que no afecta los datos en sí. 
1. Luego, pensé que quería visualizar. En este caso, me interesaba visualizar la variación en los géneros de los discos nominados por año, ya que sabía que en la actualidad la mayoría de los nominados son Pop, y quería ver cuándo esto había empezado a ser así y si en años anteriores era otro género el que dominaba o si era más parejo.
1. Para comenzar con la visualización, agrupé los datos por año y género musical, para que así se pudiera contar cuántos discos hay en cada combinación de año y género.
1. Luego, con Altair armé un gráfico de barras horizontales, dónde en el eje X están la cantidad de discos nominados y en el eje Y están los años, yendo del 2000 al 2024. En cuanto a las barras, cada color representa un género musical.
1. Una vez visualicé este código, me di cuenta de dos cosas: Los años estaban desordenados y, por alguna razón, los números en el eje X contemplaba medios números, cosa que no me sirve porque los números representan discos nominados, y no se puede nominar medio disco, por lo que solo entorpece el gráfico.
1. Por esto, arreglé la forma en que se ordenaba el eje Y eliminando la parte del código que decía "sort='-x'", ya que esto ordenaba el eje Y en función de los datos del eje X, y a mi me importaba que estuviera ordenado del 2000 al 2024. 
1. Luego, busqué un código que me ayudara a solucionar los números del eje X y que fueran solamente números enteros.
1. Visualicé una vez más y el gráfico estaba tal como lo quería, pero decidí cambiar los colores. Para esto, agregué un código que me permitiera definir un color por cada uno de los géneros. No utilicé una paleta predeterminada de Altair porque quería más libertad y por la gran cantidad de géneros a los que había que definirle un color.
1. Una vez elegidos todos los colores, visualicé nuevamente y ya estaba mi gráfico final.


**Base de datos utilizada y proceso**

La base de datos utilizada para esta visualización fue la de Álbum de Año, esta fue sacada directamente desde la base de datos de los ganadores de los premios Grammys que fue descrita en la entrega anterior. La base de datos no necesitó mucho más procesamiento que lo que ya estaba hecho desde el principio, ya que me preocupé de que estuviera ordenada, lo único que tuve que arreglar fueron algunos títulos de discos que tenían comas, lo que desordenaba el formato de CSV y hacía parecer que habían columnas extras en algunas filas. También tuve que cambiar los nombres de algunas columnas en Google Colab, como expliqué más arriba.

Seleccioné esta base de datos porque corresponde a una de las categorías más importantes de los premios Grammy, está considerada dentro de las "cuatro grandes", que serían: Canción del Año, Grabación del Año, Mejor Artista Nuevo y Disco del Año. Además, siendo que es una de las categorías con la mayor cantidad de nominados, muchos de los nominados en esta categoría se repiten en las otras, por lo que me pareció que sería bastante representativa para esta entrega, considerando que es solo 1 visualización.

**Preguntas que se pueden responder con la visualización**

¿Cuál es el género con mayor cantidad de nominados en X año?
¿Cómo han variado los géneros de los discos nominados desde el año 2000 hasta la actualidad?
¿Cuál es el género que ha tenido más nominaciones desde el año 2000 hasta la actualidad?
¿Cuál es el género que ha predominado en la categoría en el siglo XXI, hasta el momento?
