class Movie_Rating:
    def __init__(self, name, actors: int, music: int, story: int):
        self.name = name
        self.actors = actors
        self.music = music
        self.story = story
        self.avg = (self.music + self.actors + self.story) / 3
        
        self.ratings = {
            "name": self.name,
            "actor rating": self.actors,
            "music rating": self.music,
            "story rating": self.story,
            "average rating": self.avg
        }

def print_movies(movie_list):
    for i in movie_list:
        print("name: ", i.name, ", actor rating: ", i.actors, ", music rating: ", i.music, ", story rating: ", i.story, ", average rating: ", i.avg)

movies = []

while True:
    add_rating = input("add rating? (Y|N) ")

    if add_rating == "Y":
        name = input("Movie name: ")
        actors = int(input("actor rating: "))
        music = int(input("music rating: "))
        story = int(input("story rating: "))
        movies.append(Movie_Rating(name, actors, music, story))

    print_prompt = input("print list? (Y|N) ")

    if print_prompt == "Y":
        print_movies(movies)