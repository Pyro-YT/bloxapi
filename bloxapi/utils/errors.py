class NotAutenticated(Exception):
    """
    Raised when a user is not authenticated.
    """
    pass

class FailedAuthentication(Exception):
    """
    Raised when the cookie passed is not valid.
    """
    pass