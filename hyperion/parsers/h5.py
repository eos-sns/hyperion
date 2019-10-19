# !/usr/bin/python3

""" Parses H5PY file """

# given that f is a h5py.File
# f.attrs contains all the parameters of the data file
# f.keys() contains all the fields


import h5py


class H5PyParser:
    def __init__(self, file_path, opener=h5py.File):
        self.file_path = file_path
        self.opener = opener
        self.data = self._read_data()

    def _read_data(self):
        return self.opener(self.file_path, 'r')  # todo bufferize

    def get_attrs(self):
        return {
            key: self.data.attrs.get(key)
            for key in self.data.attrs.keys()
        }

    def get_fields(self):
        return {
            key: self.data.get(key)
            for key in self.data.keys()
        }

    def get_field(self, key):
        return self.data.get(key)
