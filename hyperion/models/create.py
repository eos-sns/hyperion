# !/usr/bin/python3

""" Hyperion EOS creator """

from pymongo import MongoClient

from models.meta import MetaRunner
from utils.files import find_files


class Creator(MetaRunner):
    def run(self):
        self.log_message('run')
        self._create()

        for category in self.configuration.categories():
            self._create_category(category)

    def _create_category(self, category):
        files = self._get_files_of(category)
        coll_name = self.configuration.get_collection_name_of(category)

        for file in files:
            simulation_data = self.configuration.get_simulation_data(file)
            simulation_data['path'] = file
            self.mongo_db[coll_name].insert_one(simulation_data)

    def __init__(self):
        super().__init__('CREATOR')

        self.mongo_client = MongoClient()
        self.mongo_db = None  # will be created once there is a configuration

    def _create(self):
        db_name = self.configuration.get_db_name()
        self.mongo_db = self.mongo_client[db_name]

    def _get_files_of(self, category):
        file_regex = self.configuration.get_file_regex_of(category)
        source_folder = self.configuration.get_folder_of(category)
        return find_files(source_folder, file_regex, False)  # todo recurse ?
