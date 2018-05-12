class Movie(object):
    def __init__(self, name, rating):
        self.name=name
        self.rating=rating
        
class Action(Movie):
    def content(self):
        return "fight"
    
class Comedy(Movie):
    def content(self):
        return "fun"
    
class Drama(Movie):
    def content(self):
        return "life"

movies=[Action("Batman",4),Comedy("Look",6),Drama("Dream",3)]

for movie in movies:
    print("Movie is",movie.name+".")
    print("It is rated", movie.rating, movie.content())
    
