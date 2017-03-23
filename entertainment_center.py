import media
import fresh_tomatoes

#Toy Story Movie
toy_story = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Inception Movie
inception = media.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

#Pulp Fiction Movie
pulp_fiction = media.Movie("Pulp Fiction", "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

#Hackers Movie
hackers = media.Movie("Hackers", "Dade Murphy was a hacker even as a kid in Seattle. He got arrested for the computer virus that he planted and was banned from using any computer until the age of 18.Then he moves to New York to meet a group of hackers. He also falls in love with Kate Libby.", "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg", "https://www.youtube.com/watch?v=Ql1uLyuWra8")

#Lucy Movie
lucy = media.Movie("Lucy", "A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.", "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg", "https://www.youtube.com/watch?v=MVt32qoyhi0")

#Gravity Movie
gravity = media.Movie("Gravity", "Two astronauts work together to survive after an accident which leaves them alone in space.", "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg", "https://www.youtube.com/watch?v=OiTiKOy59o4")


movies = [toy_story, inception, pulp_fiction, hackers, lucy, gravity]

#A function to use fresh_tomatoes file to open in the browser
fresh_tomatoes.open_movies_page(movies)

