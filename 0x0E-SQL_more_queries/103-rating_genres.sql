-- List all genres and their total ratings, sorted by the rating sum in descending order
SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.tv_genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;

