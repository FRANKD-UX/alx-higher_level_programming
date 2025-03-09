-- List all genres not linked to Dexter
SELECT name
FROM genres
WHERE id NOT IN (
	    SELECT genre_id
	    FROM tv_show_genres
	    JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id
	    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;

