from model import db, Song
from peewee import *

db.connect()

db.drop_tables([Song])
db.create_tables([Song])

Song(title='Tearin Up My Heart', artist='Backstreet Boys').save()
Song(title='Love Story', artist='Taylor Swift').save()
Song(title='Jingle Bells', artist='Frank Sinatra').save()