#!/usr/bin/env python3
# coding: utf-8

""" Configuration module """

import json
import ntpath

from logs.logger import get_custom_logger


class Configuration:
    SIMULATION_ID_REGEX = "<ID>"  # used in file regex

    def __init__(self, config_file):
        self.config_file = config_file
        self.data = None  # will be a dictionary when parsed
        self.logger = get_custom_logger('CONFIGURATION')

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
        simulation_id_regex = self.get_simulation_id_regex()
        raw_file_regex = self.get_matrioska_config([key, 'file regex'])
        file_regex = raw_file_regex.replace(
            self.SIMULATION_ID_REGEX, simulation_id_regex
        )

        return file_regex

    def get_simulation_id_regex(self):
        return self.get_matrioska_config(['simulation', 'id regex'])

    def get_walker_collection_name(self):
        return self.get_matrioska_config(['Walker', 'collection name'])

    def get_tau_collection_name(self):
        return self.get_matrioska_config(['TauData', 'collection name'])

    def get_simulation_id(self, file_path):
        file_name = ntpath.basename(file_path)

        if file_name.startswith('Walker'):
            pass  # todo
        elif file_name.startswith('AveData'):
            pass  # todo
        elif file_name.startswith('Tau_e_'):
            pass  # todo
        elif file_name.endswith('_FLIPBOXES0_200_300Mpc_lighttravel'):
            pass  # todo
        elif file_name.startswith('_200_300Mpc_LightConeSlice'):
            pass  # todo
