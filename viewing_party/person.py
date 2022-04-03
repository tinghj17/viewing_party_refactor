class Person:
    def __init__(self, name, watched, friends, subscriptions):
        self.name = name
        self.watched = watched
        self.friends = friends
        self.subscriptions = subscriptions

    def add_watched(self, movie):
        self.watched.append(movie)
    
    def get_num_watched(self):
        return len(self.watched)