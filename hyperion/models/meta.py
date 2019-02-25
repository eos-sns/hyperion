# !/usr/bin/python3

""" Running modes of Hyperion """

import abc

from logs.logger import get_custom_logger


class MetaRunner:
    def __init__(self, run_mode):
        self.run_mode = run_mode
        self.logger = get_custom_logger(self.run_mode.upper())

    def log_message(self, *message):
        self.logger.log_message(message)

    def log_error(self, *error, cause):
        self.logger.log_error(error, cause)

    @abc.abstractmethod
    def run(self):
        pass
