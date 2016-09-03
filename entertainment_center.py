# Importing other python files used in this file
import media
import fresh_tomatoes

# Example object:
# object = fileName.Class(parameter1, p2, p3, p4)
toystory = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar = media.Movie("Avatar", "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of rock", "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouielle = media.Movie("Ratatouielle", "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in paris", "While on a trip to Paris with his fiance's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger games", "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death", "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

# Array of movie Instances
movie_list = [toystory, avatar, school_of_rock, ratatouielle, midnight_in_paris, hunger_games]

# passing movie instances array to "open_movies_page" function provided by Udacity
# Here fresh_tomatoes is filename and open_movies_page is a function
fresh_tomatoes.open_movies_page(movie_list)