CREATE TABLE director (
	id_director INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_director TEXT
);


CREATE TABLE direccion (
	id_director INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_pelicula INTEGER NOT NULL
);


CREATE TABLE pelicula (
	Column1 INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	anio TEXT NOT NULL
);

CREATE TABLE produccion (
	id_productor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_pelicula INTEGER NOT NULL
);


CREATE TABLE productor (
	id_productor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_productor TEXT NOT NULL
);


CREATE TABLE protagonista (
	id_actor INTEGER NOT NULL,
	id_pelicula INTEGER NOT NULL
);


CREATE TABLE actor (
	id_actor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre_actor TEXT NOT NULL
);
