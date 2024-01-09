from eralchemy2 import render_er

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table, Date, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

# OPCION 1: con relaciones dentro de las tablas

# Crear tabla: user, posts, media, follower y comment.
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    lastname = Column(String(10))
    firstname = Column(String(10))
    email = Column(String(30), nullable=False)
    password = Column(String(10), nullable=False)
    subscription_date = Column(Date)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)      

   
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Column(Enum, nullable=False)
    url = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship(Post)

# Usar backref para varias to varios. 
class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user_from = relationship(User, foreign_keys=[user_from_id], backref="followers_from")
    user_to_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user_to = relationship(User, foreign_keys=[user_to_id], backref="followers_to")

render_er(Base, 'diagram.png')
