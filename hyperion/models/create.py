# !/usr/bin/python3

""" Hyperion EOS creator """

from models.meta import MetaRunner


class Creator(MetaRunner):
    def run(self):
        self.log_message('run')
        raise NotImplementedError

    def __init__(self):
        super().__init__('CREATOR')
