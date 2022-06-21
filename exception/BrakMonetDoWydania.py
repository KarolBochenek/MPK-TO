class BrakMonetDoWydania(Exception):
    '''Exception indicates that machine has no coins for change'''
    def __init__(self):
        super().__init__("Brak monet do wydania")