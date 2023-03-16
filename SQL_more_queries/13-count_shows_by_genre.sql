-- Active: 1678888257555@@127.0.0.1@3306@hbtn_0d_tvshows
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
ALTER TABLE tv_genres ADD number_of_shows INT DEFAULT 1;
SELECT tv_genres.name, SUM(number_of_shows)
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name, number_of_shows
ORDER BY SUM(number_of_shows) DESC;