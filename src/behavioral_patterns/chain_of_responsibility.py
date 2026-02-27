from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass
class ValidateMovieRequest:
    movie_id: int
    check_session_availability: bool
    country_iso_code: str | None = None


class Validator(ABC):
    def __init__(self) -> None:
        self._next: Optional["Validator"] = None

    def set_next(self, validator: "Validator") -> "Validator":
        self._next = validator
        return validator

    def validate(self, request: ValidateMovieRequest) -> None:
        self._handle(request)
        if self._next:
            self._next.validate(request)

    @abstractmethod
    def _handle(self, request: ValidateMovieRequest) -> None:
        pass

class MovieExistsInCountryValidator(Validator):
    def _handle(self, request: ValidateMovieRequest) -> None:
        if request.country_iso_code is not None:
            print(
                f"Verifying that movie {request.movie_id} exists in {request.country_iso_code}"
            )

class MovieExistsValidator(Validator):
    def _handle(self, request: ValidateMovieRequest) -> None:
        print(f"Verifying that movie {request.movie_id} exists")

class MovieHasActiveSessionValidator(Validator):
    def _handle(self, request: ValidateMovieRequest) -> None:
        if request.check_session_availability:
            print(
                f"Verifying that movie {request.movie_id} has active sessions"
            )

def validate_movie(request: ValidateMovieRequest) -> None:
    movie_exists = MovieExistsValidator()
    movie_in_country = MovieExistsInCountryValidator()
    movie_has_session = MovieHasActiveSessionValidator()

    movie_exists.set_next(movie_in_country).set_next(movie_has_session)

    print("\n--- New validation ---")
    movie_exists.validate(request)

if __name__ == "__main__":
    request_1 = ValidateMovieRequest(
        movie_id=1,
        check_session_availability=False,
        country_iso_code=None
    )
    validate_movie(request_1)

    request_2 = ValidateMovieRequest(
        movie_id=2,
        check_session_availability=False,
        country_iso_code="ES"
    )
    validate_movie(request_2)

    request_3 = ValidateMovieRequest(
        movie_id=3,
        check_session_availability=True,
        country_iso_code=None
    )
    validate_movie(request_3)

    request_4 = ValidateMovieRequest(
        movie_id=4,
        check_session_availability=True,
        country_iso_code="US"
    )
    validate_movie(request_4)