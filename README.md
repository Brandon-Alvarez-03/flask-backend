# Songs DB using Flask and Peewee

## Model/Schema

- Running model.py connects to the PostgreSQL database and updates the schema for entering new songs

Ex.

```python

class BaseModel(Model):
  class Meta:
    database = db

class Song(BaseModel):
  title = CharField()
  artist = CharField()

```

## Seeding

- Running seed.py connects to the PostgreSQL database and seeds several example songs for the user to view


## Using the browser to view notes as json files

- Flask was implemented using peewee and playhouse shortcuts to enable the user to view their favorite songs in the browser
- By running backend.py the user will have all song titles and their respective artist presented by default and can view individual songs using endpoint ```'/song/<id>'```

### Example Result in Browser

```JSON

[
  {
    "artist": "Backstreet Boys",
    "id": 1,
    "title": "Tearin Up My Heart"
  },
  {
    "artist": "Taylor Swift",
    "id": 2,
    "title": "Love Story"
  },
  {
    "artist": "Frank Sinatra",
    "id": 3,
    "title": "Jingle Bells"
  }
]

```
