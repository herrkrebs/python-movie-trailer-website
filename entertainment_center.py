# Initializes the movies and generates the html page

import fresh_tomatoes
import media


# Initialize the movie objects
what_we_do_in_the_shadows = media.Movie("What We Do in the Shadows",
                                        """Viago, Deacon, and Vladislav are
                                        vampires who are finding that
                                        modern life
                                        has them struggling with the mundane -
                                        like paying rent, keeping up with the
                                        chore wheel, trying to get into
                                        nightclubs, and overcoming flatmate
                                        conflicts.""",
                                        "https://upload.wikimedia.org/wikipedia/en/7/70/What_We_Do_in_the_Shadows_poster.jpg",  # noqa
                                        "https://www.youtube.com/watch?v=Cv568AzZ-i8",  # noqa
                                        "2014",
                                        "Jemaine Clement, Taika Waititi, "
                                        "Cori Gonzalez-Macuer",
                                        "http://www.imdb.com/title/tt3416742/?ref_=nv_sr_1")  # noqa

the_fountain = media.Movie("The Fountain",
                           """As a modern-day scientist, Tommy is struggling
                           with mortality, desperately searching for
                           the medical breakthrough that will save the life of
                           his cancer-stricken wife, Izzi.""",
                           "https://upload.wikimedia.org/wikipedia/en/e/ee/Fountain_poster_1.jpg",  # noqa
                           "https://www.youtube.com/watch?v=dAuxryJ6pv8",
                           "2007",
                           "Hugh Jackman, Rachel Weisz, Sean Patrick Thomas",
                           "http://www.imdb.com/title/tt0414993/")

berlin_blues = media.Movie("Berlin Blues",
                           """Frank Lehmann (Christian Ulmen) is a bartender
                           working in Kreuzberg, a borough of
                           West Berlin in October 1989, in the final weeks
                           before the fall of the Berlin Wall.
                           As he is approaching his 30th birthday, his friends
                           start teasing him by calling him
                           "Herr Lehmann" ("Mr. Lehmann").
                           He has little interest in anything outside of SO 36,
                           the eastern part of the borough of Kreuzberg.
                           He has a brief relationship with Katrin
                           (Katja Danowski (de)), a cook at a nearby bar.
                           His best friend, Karl (Detlev Buck) slowly goes mad,
                            and his parents show up for a visit,
                           disrupting his laid-back lifestyle.""",
                           "http://www.wagnerverein-jena.de/wp-content/uploads/2015/04/herr-lehmann.jpg",  # noqa
                           "https://www.youtube.com/watch?v=s8CjefK93ik",
                           "2003",
                           "Christian Ulmen, Katja Danowski, Detlev Buck",
                           "http://www.imdb.com/title/tt0322545/?ref_=fn_al_tt_1")  # noqa

# Add the movie objects to a list
movies = [what_we_do_in_the_shadows, the_fountain, berlin_blues]

# Generate the movies page with the movies
fresh_tomatoes.open_movies_page(movies)
