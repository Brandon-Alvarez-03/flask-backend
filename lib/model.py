from peewee import *

db = PostgresqlDatabase('songs', user='brandonalvarez', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Song(BaseModel):
  title = CharField()
  artist = CharField()