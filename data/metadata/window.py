from data.metadata.attr_dict import AttrDict

class Window:

    ATTRIBUTES = {
        'mouse_x_pos': 0,
        'mouse_y_pos': 0,
        'click': False
    }

    def __init__(self):
        self.attributes = AttrDict(self.ATTRIBUTES)