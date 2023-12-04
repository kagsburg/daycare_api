# the Core User class that will be used to create a user object

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password