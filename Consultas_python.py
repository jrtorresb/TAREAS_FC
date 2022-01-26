# Consultar datos
conexion = sqlite3.connect("MCU.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM director") 
personas=cursor.fetchall() # recoge todos los resultados de la ejecucion
for persona in personas:
  print(persona)

conexion.close()

# pero se necesita normlizar la table y se hace de manera manuel
# los INSERTS manuales se incluyen en el archivo: Querys_SQL



# CONSULTAS UNA VEZ QUE SE NORMALIZA LA BASE:

conexion = sqlite3.connect("MCU.db")
cursor = conexion.cursor()

l = ["SELECT * FROM pelicula WHERE anio IN ('2015','2016','2017','2018','2019','2020')",
	"""SELECT P.titulo, P.anio, D.id_director, DD.nombre_director from pelicula  P
	LEFT JOIN direccion D on P.id_pelicula = D.id_pelicula
	LEFT JOIN director DD on D.id_director = DD.id_director WHERE DD.nombre_director = 'Jon Watts'""",
	"""SELECT P.titulo, D.id_productor, DD.nombre_productor from pelicula  P
	LEFT JOIN produccion D on P.id_pelicula = D.id_pelicula
	LEFT JOIN productor DD on D.id_productor = DD.id_productor WHERE P.titulo LIKE '%Man%'""",
	"""SELECT P.titulo, P.anio, DD.nombre_director, A.nombre_actor from pelicula  P
	LEFT JOIN direccion D on P.id_pelicula = D.id_pelicula
	LEFT JOIN director DD on D.id_director = DD.id_director 
	LEFT JOIN protagonista PR on P.id_pelicula = PR.id_pelicula 
	LEFT JOIN actor A on PR.id_actor = A.nombre_actor 
	""",
	"""SELECT P.titulo, P.anio, DD.nombre_director, N.nombre_productor from pelicula  P
	LEFT JOIN direccion D on P.id_pelicula = D.id_pelicula
	LEFT JOIN director DD on D.id_director = DD.id_director
	LEFT JOIN produccion p2 on P.id_pelicula = p2.id_pelicula 
	LEFT JOIN productor N on p2.id_productor = N.id_productor WHERE N.nombre_productor = 'Kevin Feige'"""
]

for query in l:
	cursor.execute(query) 
	personas=cursor.fetchall() # recoge todos los resultados de la ejecucion
	# No se usa commit porque no se ha ejecutado ninguna actualizacion o insercion a la base de datos
	for persona in personas:
	  print(persona)

conexion.close()