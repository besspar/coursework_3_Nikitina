from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_user_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def create(self, data_in):
        obj = User(**data_in)
        self._db_session.add(obj)
        self._db_session.commit()
        return obj

    def get_limit(self, limit, offset):
        return self._db_session.query(User).limit(limit).offset(offset).all()

    def update(self, data_in):
        obj = self.get_user_by_id(data_in.get('id'))
        if obj:
            if data_in.get('password'):
                obj.password = data_in.get('password')
            if data_in.get('role'):
                obj.role = data_in.get('role')
            if data_in.get('name'):
                obj.name = data_in.get('name')
            if data_in.get('surname'):
                obj.surname = data_in.get('surname')
            if data_in.get('favorite_genre'):
                obj.surname = data_in.get('favorite_genre')
            if data_in.get('role'):
                obj.surname = data_in.get('role')
            self._db_session.add(obj)
            self._db_session.commit()
            return obj