import datetime
import uuid
from typing import Any, Sequence

import arrow
from flask import Flask
from flask_mongoengine import MongoEngine

from common.config import read_config


def create_dummy_app() -> Flask:
    config = read_config()
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = config.get('MONGO', {})
    return app


def create_db() -> MongoEngine:
    db = MongoEngine()
    dummy_app = create_dummy_app()

    db.init_app(dummy_app)
    del dummy_app

    return db


def now() -> datetime:
    """ Returns the current time """

    return datetime.datetime.utcnow()


def new_uuid() -> str:
    """ Created a new UUID string """

    return str(uuid.uuid4()).replace('-', '')


def first(collection: Sequence) -> Any:
    """ Retrieves the first element of a collection """

    if len(collection) == 0:
        return None

    return collection[0]


def to_humanized_date(date: datetime) -> str:
    """ Converts a date to a human readable format """

    return arrow.get(date).humanize()


def concat_url_path(url: str, path: str) -> str:
    """ Safely concatenating the start of a url string and a path """

    if url.endswith('/'):
        url = url[:-1]

    if path.startswith('/'):
        path = path[1:]

    return url + '/' + path
