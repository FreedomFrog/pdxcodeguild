class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    c1 = Card('Hearts', 'Ace', 1)
    print(c1)

