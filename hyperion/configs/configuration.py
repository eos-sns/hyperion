#!/usr/bin/env python3
# coding: utf-8

""" Configuration module """

import json
import ntpath
import re

from logs.logger import get_custom_logger


class Configuration:
    def __init__(self, config_file):
        self.config_file = config_file
        self.data = None  # will be a dictionary when parsed
        self.logger = get_custom_logger('CONFIGURATION')

    def valid_categories(self):
        return self.get_matrioska_config(['meta', 'categories'])

    def _parse(self):
        self.logger.log_message('parse', self.config_file)
        raise NotImplementedError

    def get_config(self, key):
        if not self.data:  # cache
            with open(self.config_file) as reader:
                self.data = json.load(reader)

        return self.data[key]

    def get_matrioska_config(self, matrioska):
        """
        :param matrioska: list of inner configs, e.g ['db', 'coll', 'name']
        :return: None or value in config
        """

        current_matrioska = self.get_config(matrioska[0])

        for key in matrioska[1:]:  # first key already got
            try:
                current_matrioska = current_matrioska[key]
            except:
                return None

        return current_matrioska

    def get_db_name(self):
        return self.get_matrioska_config(['db', 'name'])

    def get_folder_of(self, key):
        return self.get_matrioska_config([key, 'folder'])

    def get_file_regex_of(self, key):
        return self.get_matrioska_config([key, 'file regex'])

    def get_simulation_id_regex(self):
        return self.get_matrioska_config(['simulation', 'id regex group'])

    def get_file_id_regex(self):
        return self.get_matrioska_config(['simulation', 'file id regex group'])

    def get_walker_collection_name_of(self, key):
        return self.get_matrioska_config([key, 'collection name'])

    def get_file_regex(self, file_name):
        if file_name.startswith('Walker'):
            return self.get_file_regex_of('Walker')
        elif file_name.startswith('AveData'):
            return self.get_file_regex_of('AveData')
        elif file_name.startswith('Tau_e_'):
            return self.get_file_regex_of('TauData')
        elif file_name.endswith('_FLIPBOXES0_200_300Mpc_lighttravel'):
            return self.get_file_regex_of('LightConeBoxes')
        elif file_name.startswith('_200_300Mpc_LightConeSlice'):
            return self.get_file_regex_of('LightConsSlices')

        return None

    def get_simulation_id(self, file_path):
        file_name = ntpath.basename(file_path)

        file_regex = self.get_file_regex(file_name)
        if file_regex:
            match = re.search(file_regex, file_name)
            out = {
                'id': match.group(self.get_simulation_id_regex())
            }

            if len(match.groups()) > 1:  # there are more groups
                out['file id'] = match.group(self.get_file_id_regex())

            return out

        return None
