class InvalidCommand(Exception):
    def __init__(self, message = "Nevaliden nomer"):
        self.message = message


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message


class CharacterExists(Exception):
    def __init__(self, message = "Sushetvuva takova ime"):
        self.message = message


class InvalidCharacterClass(Exception):
    def __init__(self, message):
        self.message = message


class CharacterNotFound(Exception):
    def __init__(self, message = "Niama takuv geroi"):
        self.message = message