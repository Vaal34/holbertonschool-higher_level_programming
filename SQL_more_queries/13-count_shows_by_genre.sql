-- Active: 1678888257555@@127.0.0.1@3306@hbtn_0d_tvshows
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- Count permet de compter le nombre de fois que show_id est dans les genre_id
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
-- Join pour afficher que les genres pour lesquels il y a au moins une série associée dans la table tv_show_genres
GROUP BY tv_show_genres.genre_id 
-- regroupe les genre_id de la table tv_show_genres.
-- GROUP BY est nécessaire pour diviser les données en groupes et appliquer la fonction COUNT à chaque groupe individuellement.
ORDER BY number_of_shows DESC;  