#!/usr/bin/env python3
# coding: utf-8

""" Configuration module """

from logs.logger import get_custom_logger


class Configuration:
    def __init__(self, config_file):
        self.config_file = config_file
        self.data = None  # will be a dictionary when parsed
        self.logger = get_custom_logger('CONFIGURATION')

    def _parse(self):
        self.logger.log_message('parse', self.config_file)
        raise NotImplementedError

    def get_config(self, key):
        if not self.data:  # cache
            self._parse()

        return self.data[key]
