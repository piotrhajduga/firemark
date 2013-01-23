from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, Sequence('user_id_seq'),
            primary_key=True, autoincrement=True)
    login = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    roles = Column(String(500), default='')

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %s (%s)>' % (self.login, self.email)

    def get_roles(self):
        roles = set(filter(lambda role: role,
                map(lambda role: role.strip(),
                    self.roles.split(','))))
        return roles

    def add_role(self, role):
        roles = set(filter(lambda role: role,
                map(lambda role: role.strip(),
                    self.roles.split(','))))
        roles.add(role)
        self.roles = ','.join(roles)

    def remove_role(self, role):
        roles = set(filter(lambda role: role,
                map(lambda role: role.strip(),
                    self.roles.split(','))))
        roles.remove(role)
        self.roles = ','.join(roles)


class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    tags = Column(String(500), default='')

    def __init__(self, name, tags=None):
        self.name = name
        if tags:
            self.tags = ','.join(tags)

    def __repr__(self):
        return '<Location %s (%x)>' % (self.name, self.location_id)

    def get_tags(self):
        tags = set(filter(lambda tag: tag,
                map(lambda tag: tag.strip(),
                    self.tags.split(','))))
        return tags

    def add_tag(self, tag):
        tags = set(filter(lambda tag: tag,
                map(lambda tag: tag.strip(),
                    self.tags.split(','))))
        tags.add(tag)
        self.tags = ','.join(tags)

    def remove_tag(self, tag):
        tags = set(filter(lambda tag: tag,
                map(lambda tag: tag.strip(),
                    self.tags.split(','))))
        tags.remove(tag)
        self.tags = ','.join(tags)



class Player(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    user = relationship("User", backref=backref('users', order_by=user_id))
    location = relationship("Location", backref=backref('locations', order_by=location_id))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Player %x (%x)>' % (self.player_id, self.user_id)


class Exit(Base):
    __tablename__ = 'exits'

    exit_id = Column(Integer, Sequence('exit_id_seq'), primary_key=True)
    name = Column(String(100))
    location_id = Column(Integer, ForeignKey('locations.location_id'))
    dest_location_id = Column(Integer, ForeignKey('locations.location_id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Exit %s (%x)>' % (self.name, self.id)


class Brick(Base):
    __tablename__ = 'bricks'

    brick_id = Column(Integer, Sequence('brick_id_seq'), primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.location_id'))
    type = Column(String(50))
    data = Column(String(3000))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Brick %s (%h)>' % (self.type, self.id)
