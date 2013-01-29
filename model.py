from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy import ForeignKey, Sequence


Base = declarative_base()


loc2ns = Table('location2namespace', Base.metadata,
               Column('location_id', Integer, ForeignKey('location.id')),
               Column('namespace_id', Integer, ForeignKey('namespace.id'))
               )


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    login = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    roles = Column(String(500), default='')

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password
        self.roles = ''

    def __repr__(self):
        return '<User %s (id: %x)>' % (self.login, self.id)

    def get_roles(self):
        return set(filter(lambda role: role,
                          map(lambda role: role.strip(),
                              self.roles.split(','))))

    def add_role(self, role):
        roles = self.get_roles()
        roles.add(role)
        self.roles = ','.join(roles)

    def remove_role(self, role):
        roles = self.get_roles()
        roles.remove(role)
        self.roles = ','.join(roles)


class Namespace(Base):
    __tablename__ = 'namespace'

    id = Column(Integer, Sequence('namespace_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    starting = Column(Boolean, nullable=False, default=False)
    locations = relationship('Location', secondary=loc2ns)

    def __init__(self, name, starting=False):
        self.name = name
        self.starting = starting

    def __repr__(self):
        return '<Namespace %s (id: %x)>' % (self.name, self.id)


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    location_id = Column(Integer, ForeignKey('location.id'))

    user = relationship('User', backref=backref('user', uselist=False))
    location = relationship('Location',
                            backref=backref('location', uselist=False))

    def __repr__(self):
        return '<Player %x (for user %s (id: %x))>' % (self.id, self.user.login,
                                                       self.user_id)


class Exit(Base):
    __tablename__ = 'exit'

    id = Column(Integer, Sequence('exit_id_seq'), primary_key=True)
    brick_id = Column(Integer, ForeignKey('brick.id'))
    dest_location_id = Column(Integer, ForeignKey('location.id'))

    def __repr__(self):
        return '<Exit %x (id:%x)>' % (self.dest_location_id, self.id)


class Brick(Base):
    __tablename__ = 'brick'

    id = Column(Integer, Sequence('brick_id_seq'), primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    order = Column(Integer)
    type = Column(String(50), nullable=False)
    data = Column(String(3000))

    exits = relationship('Exit', backref=backref('exit'),
                         foreign_keys=[Exit.brick_id])

    def __init__(self, type):
        self.type = type
        self.data = '{}'

    def __repr__(self):
        return '<Brick %s (id: %x)>' % (self.type, self.id)


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    namespaces = relationship('Namespace', secondary=loc2ns)

    bricks = relationship('Brick', backref=backref('brick'),
                          foreign_keys=[Brick.location_id])

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Location %s (id: %x)>' % (self.name, self.id)
