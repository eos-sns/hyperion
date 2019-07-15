# !/usr/bin/python3

""" Hyperion updater """

from models.mongo import MongoRunner
from utils.files import find_files


class Updater(MongoRunner):
    def _run(self):
        files = self._get_files()
        for file in files:
            self._upsert_file(file)

    def _get_files(self):
        folder = self.configuration.get_update_folder()
        file_re = '\w+.h5'
        return find_files(folder, file_re, recurse=True)  # todo recurse ???
