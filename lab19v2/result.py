from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Result(Generic[T]):
    """Узагальнений результат операції: успішне значення або повідомлення про помилку."""

    def __init__(self, value: T | None, is_success: bool, error: str):
        # За угодою Python, створювати Result слід через Success/Failure.
        self._value = value
        self._is_success = is_success
        self._error = error

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def value(self) -> T | None:
        return self._value

    @property
    def error(self) -> str:
        return self._error

    @classmethod
    def success(cls, value: T) -> Result[T]:
        return cls(value, True, "")

    @classmethod
    def failure(cls, error: str) -> Result[T]:
        return cls(None, False, error)

    @classmethod
    def failure_from_exception(cls, ex: Exception) -> Result[T]:
        """Аналог Failure(Exception): створює невдачу з повідомлення винятку."""
        return cls(None, False, str(ex))
