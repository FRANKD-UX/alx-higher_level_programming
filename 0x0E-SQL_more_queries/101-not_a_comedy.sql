-- List all shows that are not linked to Comedy
SELECT title
FROM tv_shows
WHERE id NOT IN (
	    SELECT tv_show_id
	    FROM tv_show_genres
	    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;

