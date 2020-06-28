from exceptions import BlockValidationError
from objects import TextObject


class Block(object):
    def __init__(self, block_type):
        self.type = block_type

    def validate(self):
        raise NotImplementedError()


class SectionBlock(Block):
    def __init__(self):
        super(SectionBlock, self).__init__('section')
        self.text = None
        self.block_id = None
        self.fields = None
        self.accessory = None

    def add_text(self, text, format_type):
        self.text = (TextObject()
                     .add_text(text, format_type, 3000))
        return self

    def add_block_id(self, block_id):
        if len(block_id) > 255:
            raise ValueError('Maximum length for block_id is 255 characters, '
                             'got {} instead'.format(len(block_id)))
        self.block_id = block_id
        return self

    def add_field(self, text, format_type):
        if not self.fields:
            self.fields = []
        if len(self.fields) == 10:
            raise ValueError('Maximum number of fields allowed is 10')
        self.fields.append(TextObject()
                           .add_text(text, format_type, 2000))
        return self

    def validate(self):
        if not self.fields and len(self.fields) < 1 and not self.text:
            raise BlockValidationError(
                block_class=self.__class__,
                reason='Text must be defined when fields is empty')
        if self.fields and len(self.fields) > 10:
            raise BlockValidationError(
                block_class=self.__class__,
                reason='Fields cannot hold more than 10 items')
