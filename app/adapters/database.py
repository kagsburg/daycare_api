

class DatabaseAdapter:
    def __init__(self, db_url: str):
        self.db_url = db_url

    def connect(self):
        print(f"Connecting to {self.db_url}")

    def disconnect(self):
        print(f"Disconnecting from {self.db_url}")


class DatabsePort:
    def save(self, data):
        pass
    def get(self, id):
        pass
    def update(self, id, data):
        pass
    def delete(self, id):
        pass
    