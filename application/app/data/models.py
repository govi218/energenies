

class User(object):

    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return "< User: {} >".format(self.username)


