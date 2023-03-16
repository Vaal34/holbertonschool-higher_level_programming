-- Active: 1678888257555@@127.0.0.1@3306@hbtn_0d_tvshows
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;