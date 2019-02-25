# !/usr/bin/python3

""" Hyperion EOS creator """

from pymongo import MongoClient

from models.meta import MetaRunner


class Creator(MetaRunner):
    def run(self):
        self.log_message('run')
        raise NotImplementedError

    def __init__(self):
        super().__init__('CREATOR')

        self.mongo_client = MongoClient()
        self.mongo_db = None  # will be created once there is a configuration

    def _create(self):
        db_name = self.configuration.get_db_name()
        self.mongo_db = self.mongo_client[db_name]
