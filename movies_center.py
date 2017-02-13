import movie
import fresh_tomatoes
import webbrowser

the_godfather = movie.Movie("The Godfather",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Godfather_ver1.jpg/220px-Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

fight_club = movie.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_green_mile = movie.Movie("The Green Mile",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Green_mile.jpg/220px-Green_mile.jpg",
                             "https://www.youtube.com/watch?v=ctRK-4Vt7dA")

the_shawshank_redemption = movie.Movie("The Shawshank Redemption",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
                                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

three_idiots = movie.Movie("3 Idiots",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",
                           "https://www.youtube.com/watch?v=K0eDlFX9GMc")


the_lion_king = movie.Movie("The Lion King",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/The_Lion_King_poster.jpg/220px-The_Lion_King_poster.jpg",
                            "https://www.youtube.com/watch?v=4sj1MT05lAA")

seven = movie.Movie("Se7en",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Seven_%28movie%29_poster.jpg/220px-Seven_%28movie%29_poster.jpg",
                    "https://www.youtube.com/watch?v=znmZoVkCjpI")

saving_private_ryan = movie.Movie("Saving Private Ryan",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",
                                  "https://www.youtube.com/watch?v=zwhP5b4tD6g")


movies_list = [the_godfather, fight_club,the_green_mile,the_shawshank_redemption,three_idiots,the_lion_king,seven,saving_private_ryan]


fresh_tomatoes.open_movies_page(movies_list)