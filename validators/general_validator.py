
from exceptions import ValidationError

class GeneralValidator:

    def __init__(self):
        pass

    def validate_blank_input(self, **inputs) -> None:
        for key, value in inputs:
            if not value.strip():
                raise ValidationError(f"{key} cannot be blank")

    def validate_ids(self, **ids) -> None:
        for key, value in ids:
            if not isinstance(value, int) or value <= 0:
                raise ValidationError(f"Invalid {key}")