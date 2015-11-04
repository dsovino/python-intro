import fresh_tomatoes
import movie

# Movies instances setup
endless_summer = movie.Movie("Endless Summer 2",
                             "Documentarian Bruce Brown again "
                             "explores choice international surf "
                             "destinations, this time visiting "
                             "locations such as Alaska, Indonesia, "
                             "Fiji, France and South Africa.",
                             "1994", "Bruce Brown", "1h 49m",
                             "http://imgau3.surfstitch.com/product_images/"
                             "SF821-VAS-1600.JPG",
                             "https://www.youtube.com/watch?v=4hh4Mc7mtJE")

the_collaborators = movie.Movie("The Collaborators",
                                "Documentary with invited musicians on Daft "
                                "Punk's 'Random Access Memories' album",
                                "2013", "Ed Lachman", "1h 04m",
                                "http://www.interestingblends.com/wp-content/"
                                "uploads/2013/04/collabdp.png",
                                "https://www.youtube.com/watch?v=eYDvxo-M0OQ")

man_on_wire = movie.Movie("Man on Wire", "A look at "
                          "tightrope walker Philippe Petit's daring, but "
                          "illegal, high-wire routine performed between New "
                          "York City's World Trade Center's twin towers in "
                          "1974, what some consider, 'the artistic crime "
                          "of the century.'", "2008", "James Marsh", "1h 34m",
                          "http://ia.media-imdb.com/images/M/MV5BMTMxNTk3NDY"
                          "1NV5BMl5BanBnXkFtZTcwNDk0ODg3MQ@@"
                          "._V1_SX640_SY720_.jpg",
                          "https://www.youtube.com/watch?v=6ddpV1GvF7E")

the_matrix = movie.Movie("The Matrix", "Neo (Keanu Reeves) believes "
                         "that Morpheus (Laurence Fishburne), an elusive "
                         "figure considered to be the most dangerous man "
                         "alive, can answer his question -- What is the "
                         "Matrix? Neo is contacted by Trinity (Carrie-Anne"
                         " Moss), a beautiful stranger who leads him into an"
                         " underworld where he meets Morpheus...", "1999",
                         "Andy Wachowski, Lana Wachowski", "2h 16m",
                         "http://die2live.worthyofpraise.org/wp-content/"
                         "uploads/2015/02/matrix-movie.jpg",
                         "https://www.youtube.com/watch?v=2oHOv9p9dHQ")

riding_giants = movie.Movie("Bustin down the Door", "During the winter of "
                            "	1975 in Hawaii, surfing was shaken to "
                            "its core. A group of young surfers from "
                            "Australia and South Africa sacrificed everything"
                            " and put it all on the line to create a sport, "
                            "a culture, and an industry that today is worth "
                            "billions of dollars and has captured the "
                            "imagination of the world.", "2008",
                            "Jeremy Gosch", "1h 46m",
                            "http://ecx.images-amazon.com/images/I/"
                            "515WxApm5jL._SY445_.jpg",
                            "https://www.youtube.com/watch?v=GxvEyJuDjvI")

neighbor_totoro = movie.Movie("My Neighbor Totoro",
                              "Two sisters encounter a mythical forest sprite"
                              " and its woodland companions when they move to "
                              "rural Japan.", "1988",
                              "Hayao Miyazaki", "1h 28m",
                              "http://t1.gstatic.com/images?q="
                              "tbn:ANd9GcR8rbq35XeWZXz_KJV5B_nR3KippiLlu"
                              "W2OnFK4TcoZ8Ukn6jBP",
                              "https://www.youtube.com/watch?v=TuLX50_5UAI")

# Moview list
movies = [endless_summer, the_collaborators, man_on_wire,
          the_matrix, riding_giants, neighbor_totoro]

# Fresh_tomatoes module setup
fresh_tomatoes.open_movies_page(movies)
