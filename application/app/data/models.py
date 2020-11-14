

class User(object):

    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return "< User: {} >".format(self.username)


class Device(object):

    def __init__(self, name, energy_usage, points, image):
        self.name = name
        self.energy_usage = energy_usage
        self.points = points
        self.image = image