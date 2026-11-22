from result import Result
from user import User
from user_not_found_exception import UserNotFoundException

MIN_PASSWORD_LENGTH = 6


class UserService:
    def __init__(self) -> None:
        # Початкові дані для демонстрації (ключі в нижньому регістрі).
        self._users: dict[str, User] = {"ivan": User("ivan", "secret123")}

    def get_user(self, username: str) -> User:
        """Повертає користувача. Якщо його немає, викидає UserNotFoundException."""
        user = self._users.get(username.lower())
        if user is None:
            raise UserNotFoundException(username)
        return user

    def register_user(self, username: str, password: str) -> Result[bool]:
        """Реєструє користувача. Очікувані помилки повертаються як Result.failure."""
        if not username or not username.strip():
            return Result.failure("Ім'я користувача не може бути порожнім.")

        if username.lower() in self._users:
            return Result.failure(f"Користувач '{username}' вже існує.")

        if not password or len(password) < MIN_PASSWORD_LENGTH:
            return Result.failure(
                f"Пароль занадто короткий (мінімум {MIN_PASSWORD_LENGTH} символів)."
            )

        self._users[username.lower()] = User(username, password)
        return Result.success(True)
