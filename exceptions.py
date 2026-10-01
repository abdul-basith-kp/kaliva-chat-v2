
class ApplicationError(Exception):
    pass

class DatabaseConnectionError(ApplicationError):
    pass

class ValidationError(ApplicationError):
    pass