# !/usr/bin/python3

""" Hyperion EOS creator """

import os
import re
import ntpath


def find_files(folder, file_name_regex, recurse):
    """
    :param folder: folder to search
    :param file_name_regex: regex of filename
    :param recurse: True iff you want to search inner folders too
    :return: [] of files, whose name match regex
    """

    lst = []

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if os.path.isfile(full_path):
            file_name = ntpath.basename(full_path)  # get file name
            if re.match(file_name_regex, file_name):  # check if it matches
                lst.append(full_path)
        elif os.path.isdir(full_path) and recurse:
            lst += find_files(
                full_path,
                file_name_regex,
                recurse
            )  # get list of files in directory

    return lst

