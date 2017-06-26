# 8 states
# no color
# full cross stitch
# |X
# ^-
# _
# X|
# \
# /
# X + others
from enum import Enum
class Stitch(Enum):
    NoColor = 0
    FullStitch = 1

def _empty_grid():
    return [[0 for x in range(6)] for y in range(6)]

def Character(object):

    def __init__(self):
        self.matrix = _empty_grid()
        self.back_stitch = _empty_grid()
        self.fill()
    def fill(self):
        # error
        pass

def AsciiA(Character):

    def fill(self):
        self.matrix[2][2] = Stitch.FullStitch
