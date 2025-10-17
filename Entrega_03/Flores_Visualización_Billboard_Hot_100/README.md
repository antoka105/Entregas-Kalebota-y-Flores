**Explicación proceso de visualización**

Para comenzar el proceso de crear la visualización, subí la base de datos, ya limpia solamente desde el año 2000 a 2025 a Google Colab.
Luego de subirla, cargué los datos y renombré algunas columnas, porque los nombres anteriores estaban en inglés.
Luego, solo incluí los valores (posiciones) que se encontraban entre el 1 y el 10 en la lista Billboard en los años seleccionados (2000 - 2025), esto para acortar la cantidad de datos que iba a tener que manejar. 
Otro punto importante, es que me di cuenta que no me servía tener el día y el mes en que la canción de "X" artista había estado en esa posición, solo me servía el año. Por ende, dejé el denominado "date" y lo cambié a año. 
Además, dentro de las columnas con las que contaba al principio, solo decidí inlcuir las categorías de artista, año, canción y máxima posición, ya que creo que estos son los datos más relevantes para aportar a nuestra historia.
Luego, quise visualizar los datos, después de haberlos acortado. Algo que no se mostró en las visualizaciones fue que intenté con hartos tipos de gráfico o visualizaciones. Primero, lo intente con uno de lineas y con puntos referenciales del color de cada artista, pero el gráfico se veía confuso y era difícil interpretar y reconocer los datos. 
Por eso, preferí mostarlos a través de un mapa de calor, como el que vimos en clases. Mientras más veces canciones de un cierto artista estuvieran en el top 10 más oscuro se pondría el recuadro y si tenía pocas "apariciones" iba a ser más claro. Además, sabía que el gráfico que eligiera debía tener tres ejes, por lo cual, determiné que un heatmap era la mejor idea. 
Primero intenté hacer el mapa de calor con ambos años, pero me arrojaba un error, ya que eran demasiados datos, por ende, determine dividirlo en décadas. 
La primera década va desde el 2000 hasta el 2010 y la segunda del 2011 al 2025. 

La primera visualización a la que llegue, fue a una visualización estática. Me gustó como quedó, pero creía que no era muy atractivo visualmente ver la cantidad de veces que un artista ha tenido canciones en el top 10 del Billboard Hot 100. 
Por eso le di otra vuelta, quise hacerlo más atractivo visualmente y para poder interactuar con el gráfico. 

Luego, con Altair armé un gráfico/ mapa de calor, el cual me permitía ver los diferentes artistas y su posición en distintos años, pero interactuar con el gráfico en el caso de que necesitara saber cuantas veces había estado en el top 10. 
Primero hice el de los años 2000 - 2010 y el resultado fue bueno, pero al momento de hacer el segundo gráfico, los datos también reflejaban los resultados del gráfico anterior. Es por eso que tuve que delimitar el rango de 2011 - 2025. Este fue uno de los pasos más difíciles, ya que constantemente me arrojaba error. 

Al momento de lograr obtener ambos gráficos decidí diferenciarlos, con colores básicos, pero que se notara una diferencia en la intensidad, por ende, mayor cantidad de veces. 
Ya estaban mis gráficos, quedé contenta con el resultado. 

Base de datos utilizada y proceso

La base de datos utilizada para esta visualización fue la de Billboard Hot 100, esta es sacada directamente de la página de los Billboard Hot 100 y, de hecho, está constantemente actualizándose. La base no necesitó mucho más procesamiento que lo que ya estaba hecho desde el principio, ya que se encontraba ordenada, su complejidad era su extensión, ya que no solo estaba la categoría de artista, sino de canción, lo cual dificultaba la comprensión rápida de la base de datos. 

Seleccioné esta base de datos porque es un elemento fundamental para contrastar con la otra base de datos de mi grupo. Esto nos permite comparar que artistas son los que realmente se escuchan y cuales finalmente terminan nominados. A pesar de que creo que es una base de datos complementaria, nos ayudará a acercarnos a la hipótesis inicial de nuestro trabajo. 

Preguntas que se pueden responder con la visualización

¿Cuál es el artista más escuchado en el año "X" según Billboard Hot 100? ¿Qué año contó con una mayor cantidad de artistas escuchados? ¿Qué artista dentro del top 10 de Billboard Hot 100 ganó o fue nominado a un Grammy?
