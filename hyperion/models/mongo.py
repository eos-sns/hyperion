# !/usr/bin/python3

""" Hyperion runner using MongoDB """

import abc

import h5py
from pymongo import MongoClient

from models.meta import MetaRunner


class MongoRunner(MetaRunner):
    def run(self):
        self._on_start_run()
        self._run()
        self._on_end_run()

    def __init__(self):
        super().__init__('CREATOR')

        self.mongo_client = None
        self.mongo_db = None  # will be created once there is a configuration

    def _open_mongo(self):
        if not self.mongo_client:
            self.mongo_client = MongoClient(
                self.configuration.get_db_server(),
                self.configuration.get_db_port()
            )

        if not self.mongo_db:
            self.mongo_db = self.mongo_client[self.configuration.get_db_name()][self.configuration.get_coll_name()]

    def _close_mongo(self):
        self.mongo_client.close()

    def _on_start_run(self):
        self._open_mongo()

    def _on_end_run(self):
        self._close_mongo()

    @staticmethod
    def _get_file_model(file_path, discard_keys=['external_table_path']):
        file_reader = h5py.File(file_path, 'r')

        model = {
            str(key): float(file_reader.attrs.get(key))  # todo parse key, val
            for key in file_reader.attrs.keys()
            if key not in discard_keys
        }
        model['path'] = file_path  # build model

        file_reader.close()
        return model

    def _add_file(self, file_path):
        model = self._get_file_model(file_path)
        self.mongo_db.insert_one(model)

    def _upsert_file(self, file_path):
        model = self._get_file_model(file_path)
        update_model = {'$set': model}  # set exact
        search_params = {'path': model['path']}
        file_in_db = self.mongo_db.find_one(search_params)

        if file_in_db:
            self.mongo_db.update_one(search_params, update_model)
        else:
            self._add_file(file_path)

    @abc.abstractmethod
    def _run(self):
        pass
