class Coordinate(object):
    def __init__(self, val):
        self._val = val

    @property
    def file(self):
        return self._val[0]

    @property
    def rank(self):
        return self._val[1]

    @property
    def file_idx(self):
        return {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
        }.get(self.file)

    @property
    def rank_idx(self):
        return range(8, -1, -1)[int(self.rank)]
