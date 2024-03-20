#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from models.engine.file_storage import FileStorage


# storage = FileStorage()
# storage.reload()
from os import getenv
from models.base_model import Base
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
