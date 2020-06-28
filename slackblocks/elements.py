from enum import Enum


class BlockElement(object):
    def __init__(self, element_type):
        self.type = element_type


class ButtonElement(BlockElement):
    class StyleType(Enum):
        DANGER = 'danger'
        PRIMARY = 'primary'

    def __init__(self):
        super(ButtonElement, self).__init__('button')
        self.text = None
        self.action_id = None
        self.url = None
        self.value = None
        self.style = None
        self.confirm = None
