class ChessGame:
    _clock_limit: int
    _clock_increment: int
    _variant: str
    _position: str
    _rated: bool
    _name: str

    def __init__(self,
                 clock_limit,
                 clock_increment,
                 variant,
                 rated,
                 name):

        self._clock_limit = clock_limit
        self._clock_increment = clock_increment
        self._variant = variant
        self._rated = rated
        self._name = name





    # clock_limit = speed,
    # clock_increment = increment,
    # variant = variant,
    # position = None,
    # rated = rated,
    # name = name

    # newGame = ChessGame(speed, increment, variant, rated, name)


    #
    # @property
    # def lichessID(self):
    #     return self._lichessID
    #
    # @property
    # def balance(self):
    #     return self._balance
    #
    # @property
    # def rating(self):
    #     return self._lichess_rating
    #
    # def balanceAdd(self, value):
    #     print("Called")
    #     self._balance += value