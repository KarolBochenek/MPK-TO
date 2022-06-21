class BrakWybranegoBiletu(Exception):
    """Exception used to indicate that no ticket was chosen."""

    def __init__(self):
        super().__init__("Nie wybrałeś żadnego biletu")