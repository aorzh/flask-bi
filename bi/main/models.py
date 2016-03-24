from sqlalchemy import Column, Integer, String, Boolean
from bi.main.database import Base


class User(Base):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'users'

    password = Column(String)
    authenticated = Column(Boolean, default=False)
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

    @staticmethod
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @staticmethod
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
