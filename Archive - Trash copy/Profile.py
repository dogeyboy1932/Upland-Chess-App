class Profile:
    _lichessID: str = ""
    _lichess_rating: int = 1000
    _uplandID: str = ""
    _balance: int = 10

    def __init__(self, liID, rating, upland):
        self._lichessID = liID
        self._lichess_rating = rating
        self._uplandID = upland

        # print(self._lichessID)

    @property
    def lichessID(self):
        return self._lichessID

    @property
    def balance(self):
        return self._balance

    @property
    def rating(self):
        return self._lichess_rating

    def balanceAdd(self, value):
        print("Called")
        self._balance += value
