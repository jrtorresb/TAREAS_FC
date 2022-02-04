
select nombre_actor 
from actor A
left join protagonista P
on A.id_actor = P.id_actor
left join pelicula PE
on PE.id_pelicula = P.id_pelicula
where PE.titulo = "Iron Man"


select A.id_actor, A.nombre_actor 
from actor A
left join protagonista P
on A.id_actor = P.id_actor
left join pelicula PE
on PE.id_pelicula = P.id_pelicula
where PE.titulo = "Joss Whedon"


select P.titulo, PROD.nombre_productor
from actor A
left join protagonista P
on A.id_actor = P.id_actor
left join pelicula PE
on PE.id_pelicula = P.id_pelicula
left join produccion PR
on PR.id_pelicula = PE.id_pelicula
left join productor PROD
on PROD.id_prodcutor=PR.id_prodcutor
where A.nombre_actor = "Downey Jr" and A.nombre_actor = "Tom Holland"