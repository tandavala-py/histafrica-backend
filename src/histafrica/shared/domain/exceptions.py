from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from histafrica.shared.domain.validators import ErrorFields


class InvalidUuidException(Exception):
    def __init__(self, error="ID must be a valid UUID") -> None:
        super().__init__(error)


class ValidationException(Exception):
    pass


class EntityValidationException(Exception):
    error: "ErrorFields"

    def __init__(self, error: "ErrorFields") -> None:
        self.error = error
        super().__init__("Entity Validation Error")


class LoadEntityException(Exception):
    error: "ErrorFields"

    def __init__(self, error: "ErrorFields") -> None:
        self.error = error
        super().__init__("Load Entity Error")


class NotFoundException(Exception):
    pass
