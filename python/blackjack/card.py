class Card:
    def __init__(self, en_value, suit):
        self.en_value = en_value
        self.suit = suit
        self.bk_value = self.set_bk_value()

    def __str__(self):
        return '{} of {}'.format(self.en_value, self.suit)

    def __repr__(self):
        return '{}:{}'.format(self.en_value, self.suit)

    def set_bk_value(self):
        en_value_dict = {
            'ace': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'jack': 10,
            'queen': 10,
            'king': 10
        }
        self.bk_value = en_value_dict[self.en_value]
        return self.bk_value
