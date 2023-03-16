-- Active: 1678888257555@@127.0.0.1@3306@hbtn_0d_tvshows
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT 
    tv_genres.name
FROM
    tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
WHERE show_id = 8;