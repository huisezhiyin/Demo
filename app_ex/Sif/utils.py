import binascii
import os


class Mimir(object):

    @staticmethod
    def string(lens: int = 20):
        return binascii.hexlify(os.urandom(lens)).decode()
