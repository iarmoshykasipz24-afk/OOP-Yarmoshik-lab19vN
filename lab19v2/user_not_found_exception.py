class UserNotFoundException(Exception):
    """Виняток: користувача з вказаним іменем не знайдено."""

    def __init__(self, username: str | None = None, message: str | None = None):
        if message is None:
            message = (
                f"Користувача '{username}' не знайдено."
                if username is not None
                else "Користувача не знайдено."
            )
        super().__init__(message)
        self.username = username
        self.message = message

    def __reduce__(self):
        # Підтримка серіалізації (pickle) разом із додатковою властивістю username.
        return (self.__class__, (self.username, self.message))
