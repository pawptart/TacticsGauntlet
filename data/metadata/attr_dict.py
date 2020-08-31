class AttrDict(dict):
    # Helper class to access dict keys as attributes
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self