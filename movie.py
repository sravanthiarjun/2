import media
import fresh_tomatoes

ranga = media.Movie("rangastalam",
                    "it is a family entertainment story and emotional",
                    "https://bit.ly/2s2lD70", "https://youtu.be/mhhb6JAJKbE")
ok = media.Movie("ok bangaram", "pure love story", "https://bit.ly/2J0YHiT",
                 "https://youtu.be/UcIL3qsd1-0")
love = media.Movie("lovers", "beautiful and amzing love story",
                   "https://bit.ly/2IJY2za", "https://youtu.be/CnbspuM3jxU")
nenu = media.Movie("nenulocal", "girl was afraid of her father",
                   "https://bit.ly/2ID6a8C", "https://youtu.be/lylc7eY6yRU")
gol = media.Movie("golmol", "friendship and honest movie",
                  "https://bit.ly/2sZe4hI", "https://youtu.be/LGm0LV0gbH4")
#list of movies we have taken and it is defined by movies
movies = [ranga, ok, love, nenu, gol]
fresh_tomatoes.open_page(movies)
