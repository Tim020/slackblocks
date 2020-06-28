from enum import Enum


class CompObject(object):
    def __init__(self):
        pass


class TextObject(CompObject):
    class FormatType(Enum):
        MARK_DOWN = 'mrkdwn'
        PLAIN_TEXT = 'plain_text'

    def __init__(self):
        super(TextObject, self).__init__()
        self.type = None
        self.text = None
        self.emoji = None
        self.verbatim = None

    def add_text(self, text, format_type, max_length=None):
        if type(format_type) is not TextObject.FormatType:
            raise ValueError('Type of format_type should be '
                             'TextObject.FormatType, got {} instead'.
                             format(type(format_type)))
        if max_length and type(max_length) is not int:
            raise ValueError('Type of max_length should be int, got {} '
                             'instead'.format(type(max_length)))
        self.text = text
        self.type = format_type

        return self

    def set_emoji(self, flag):
        if type(flag) is not bool:
            raise ValueError('Type of flag should be bool, got {} '
                             'instead'.format(type(flag)))
        self.emoji = flag

        return self

    def set_verbatim(self, flag):
        if type(flag) is not bool:
            raise ValueError('Type of flag should be bool, got {} '
                             'instead'.format(type(flag)))
        self.verbatim = flag

        return self


class ConfirmationDialog(CompObject):
    class StyleType(Enum):
        DANGER = 'danger'
        PRIMARY = 'primary'

    def __init__(self):
        super(ConfirmationDialog, self).__init__()
        self.title = None
        self.text = None
        self.confirm = None
        self.deny = None
        self.style = ConfirmationDialog.StyleType.PRIMARY

    def add_title(self, title):
        self.title = TextObject().add_text(
            title, TextObject.FormatType.PLAIN_TEXT, 100)
        return self

    def add_text(self, text, text_format):
        self.text = TextObject().add_text(text, text_format, 300)
        return self

    def add_confirm(self, text):
        self.confirm = TextObject().add_text(
            text, TextObject.FormatType.PLAIN_TEXT, 30)
        return self

    def add_deny(self, text):
        self.deny = TextObject().add_text(
            text, TextObject.FormatType.PLAIN_TEXT, 30)
        return self

    def set_style(self, style):
        if type(style) is not ConfirmationDialog.StyleType:
            raise ValueError('Type of style should be '
                             'ConfirmationDialog.StyleType, got {} instead'.
                             format(type(style)))
        self.style = style
        return self
