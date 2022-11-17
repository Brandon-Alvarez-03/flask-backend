from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from model import Song

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/song/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Song.get(Song.id == id)))
    else:
        song_list = []
        for song in Song.select():
            song_list.append(model_to_dict(song))
        return jsonify(song_list)

  if request.method =='PUT':
    body = request.get_json()
    Song.update(body).where(Song.id == id).execute()
    return "Song " + str(id) + " has been updated."

  if request.method == 'POST':
    new_song = dict_to_model(Song, request.get_json())
    new_song.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Song.delete().where(Song.id == id).execute()
    return "Song " + str(id) + " deleted."

app.run(debug=True, port=9000)
