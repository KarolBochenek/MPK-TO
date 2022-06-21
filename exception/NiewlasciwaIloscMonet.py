class NiewlasciwaIloscMonet(Exception):
    """Exception used to indicate false number of coins, ie. -1"""
    def __init__(self):
        super().__init__("Niewłaściwa ilość monet")