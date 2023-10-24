
# using ports and adapters architecture

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, id):
        return self.db.get_user(id)

    def get_all_users(self):
        return self.db.get_all_users()

    def add_user(self, user):
        return self.db.add_user(user)

    def delete_user(self, id):
        return self.db.delete_user(id)

    def update_user(self, user):
        return self.db.update_user(user)

    def get_user_by_email(self, email):
        return self.db.get_user_by_email(email)