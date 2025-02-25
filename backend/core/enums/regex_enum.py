from enum import Enum


class RegexEnum(Enum):
    PhoneValidator = (
        r'^\+380(50|66|95|99|63|73|93|67|67|68|77|96|97|98)\d{7}$',
        'Phone number must start with "+380" and then have 9 digits'
    )

    NameValidator = (
        r'^[A-Z][a-zA-Z0-9_-]{1,29}$',
        'Name must start with upper case and contain maximum 30 letters'
    )

    def __init__(self, pattern, message):
        self.pattern = pattern
        self.message = message
