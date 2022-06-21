class NiewlasciwaIloscBiletow(Exception):
    """Exception used to indicate false number of tickets, ie. -3 or 0.3"""
    def __init__(self):
        super().__init__("Niewłaściwa ilość biletów")