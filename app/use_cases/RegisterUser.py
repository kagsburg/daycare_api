# The Usecases are the application specific business rules. They are the glue between the core entities and the repositories. 
# They are the entry point to the domain layer.
from app.core.User import User

class RegisterUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user):
        email = user.email
        if self.user_repo.get_user_by_email(email):
            raise Exception("User already exists")
        user.password = self.user_repo.hash_password(user.password)
        new_user = User(user.name, user.email, user.password)

        return self.user_repo.create(new_user)