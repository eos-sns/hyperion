# !/usr/bin/python3

""" Hyperion EOS creator """

from models.mongo import MongoRunner
from utils.files import find_files


class Creator(MongoRunner):
    def _run(self):
        files = self._get_files()
        for file in files:
            self._add_file(file)

    def _get_files(self):
        folder = self.configuration.get_src_folder()
        file_re = '\w+.h5'
        return find_files(folder, file_re, recurse=True)  # todo recurse ???
