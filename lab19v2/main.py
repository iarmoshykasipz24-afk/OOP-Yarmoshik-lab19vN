from result import Result
from user_service import UserService
from user_not_found_exception import UserNotFoundException


def print_result(title: str, result: Result[bool]) -> None:
    if result.is_success:
        print(f"{title}: успіх (value = {result.value})")
    else:
        print(f"{title}: помилка - {result.error}")


def main() -> None:
    service = UserService()

    print("=== Метод з винятком: get_user ===")

    # Сценарій 1: користувач існує.
    try:
        user = service.get_user("ivan")
        print(f"Знайдено: {user}")
    except UserNotFoundException as ex:
        print(f"Помилка: {ex.message} (username = {ex.username})")

    # Сценарій 2: користувача немає, виняток обробляється через try-except.
    try:
        user = service.get_user("petro")
        print(f"Знайдено: {user}")
    except UserNotFoundException as ex:
        print(f"Помилка: {ex.message} (username = {ex.username})")

    print()
    print("=== Метод з Result[T]: register_user ===")

    print_result("Успішна реєстрація", service.register_user("petro", "password1"))
    print_result("Ім'я вже існує", service.register_user("ivan", "password1"))
    print_result("Занадто короткий пароль", service.register_user("olena", "123"))


if __name__ == "__main__":
    main()
