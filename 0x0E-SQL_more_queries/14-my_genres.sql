-- List all genres for the show Dexter
SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;

