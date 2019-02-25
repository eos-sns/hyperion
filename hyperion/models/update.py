# !/usr/bin/python3

""" Hyperion updater """

from models.meta import MetaRunner


class Updater(MetaRunner):
    def run(self):
        self.log_message('running')
        raise NotImplementedError

    def __init__(self):
        super().__init__('UPDATER')
