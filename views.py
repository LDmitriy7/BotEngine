import os

from flask import url_for, redirect

from api import tags
from loader import app

BOT_PATH = 'bot'


@app.route('/')
def index():
    return tags.a('Bot', url_for('bot'))


@app.route('/bot/')
def bot():
    return bot_file(req_path='')


@app.route('/test')
def test():
    return tags.textarea('Bebra')


@app.route('/bot/<path:req_path>')
def bot_file(req_path: str):
    file_path = f'{BOT_PATH}/{req_path}'

    if not os.path.exists(file_path):
        return 'File not found'

    if os.path.isdir(file_path):
        walker = os.walk(file_path)
        items = next(walker)
        strings = []

        for i in items[1] + items[2]:
            i_path = f'{req_path}/{i}'.lstrip('/')
            i_url = tags.a(i, url_for('bot_file', req_path=i_path))
            strings.append(i_url)

        return tags.pre('\n'.join(strings))

    with open(file_path) as file:
        return tags.textarea(file.read(), cols=100, rows=30)
