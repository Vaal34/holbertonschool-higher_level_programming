-- Active: 1678888257555@@127.0.0.1@3306@hbtn_0d_usa
-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linkedSELECT tv_shows.title, tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;