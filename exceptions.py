
class ApplicationError(Exception):
    pass

class DatabaseConnectionError(ApplicationError):
    pass