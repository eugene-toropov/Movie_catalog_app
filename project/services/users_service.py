from project.dao.user import UsersDAO
from project.exceptions import ItemNotFound
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def get_all(self):
        users = self.dao.get_all()
        return users

    def update(self, user_d):
        user_d['password'] = generate_password_hash(user_d['password'])
        return self.dao.update(user_d)

    def delete(self, pk):
        self.dao.delete(pk)

    def create(self, user_d):
        user_d['password'] = generate_password_hash(user_d['password'])
        return self.dao.create(user_d)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def update_password(self, email, new_password):
        self.dao.update_password(email, new_password)
