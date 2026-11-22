from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str

    def __str__(self) -> str:
        return f"User(username={self.username})"
