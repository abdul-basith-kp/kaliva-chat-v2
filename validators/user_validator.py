
from validators.general_validator import GeneralValidator
from exceptions import ValidationError


class UserValidator:

    def __init__(self, general_validator: GeneralValidator) -> None:
        self.gv = general_validator

    def validate_username(self, username: str) -> None:
        self.gv.validate_blank_input(username)
        if len(username) < 4:
            raise ValidationError('username too short')

    def validate_password(self, password: str) -> None:
        self.gv.validate_blank_input(password)
        if len(password) < 4:
            raise ValidationError('password too short')
