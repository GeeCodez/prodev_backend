# app/user_service.py

class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, username, age):
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string")
        if age < 18:
            raise ValueError("User must be at least 18")
        self.users.append({"username": username, "age": age})
        return True

    def get_usernames(self):
        return [u["username"] for u in self.users]

    def find_user(self, name):
        for user in self.users:
            if user["name"].lower() == name.lower():
                return user
        return None
