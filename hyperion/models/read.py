# !/usr/bin/python3

""" Hyperion EOS db reader """

from models.meta import MetaRunner


class Reader(MetaRunner):
    def run(self):
        self.log_message('read')
        raise NotImplementedError

    def __init__(self):
        super().__init__('READER')
