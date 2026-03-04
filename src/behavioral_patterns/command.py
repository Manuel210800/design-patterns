from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    synopsis: str
    internal_id: int | None = None

class Command(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass

class MovieCreator:
    def create(self, movie: Movie) -> None:
        print(f"Creating the movie: {movie.title}, with synopsis: {movie.synopsis}")

class MovieUpdater:
    def update(self, movie: Movie) -> None:
        print(f"Updating the movie: {movie.title}, with synopsis: {movie} and Id: {movie.internal_id}")


class CreateMovieCommand(Command):
    def __init__(self, movie_creator: MovieCreator, title: str, synopsis: str) -> None:
        self.__movie_creator = movie_creator
        self.__title = title
        self.__synopsis = synopsis

    def handle(self) -> None:
        movie = Movie(title=self.__title, synopsis=self.__synopsis)
        self.__movie_creator.create(movie)

class UpdateMovieCommand(Command):
    def __init__(self, movie_updater: MovieUpdater, internal_id: int, title: str, synopsis: str) -> None:
        self.__movie_updater = movie_updater
        self.__internal_id = internal_id
        self.__title = title
        self.__synopsis = synopsis

    def handle(self) -> None:
        movie = Movie(title=self.__title, synopsis=self.__synopsis, internal_id=self.__internal_id)
        self.__movie_updater.update(movie)

class MovieCommandFactory:
    def __init__(self, movie_creator: MovieCreator, movie_updater: MovieUpdater) -> None:
        self.__movie_creator = movie_creator
        self.__movie_updater = movie_updater

    def build(self, movie: Movie) -> Command:
        if movie.internal_id is None:
            return CreateMovieCommand(self.__movie_creator, movie.title, movie.synopsis)

        return UpdateMovieCommand(self.__movie_updater, movie.internal_id, movie.title, movie.synopsis)

class MovieAdmin:
    def execute(self, command: Command) -> None:
        command.handle()

if __name__ == "__main__":

    movie_creator = MovieCreator()
    movie_updater = MovieUpdater()
    movie_admin = MovieAdmin()

    movie_command_factory = MovieCommandFactory(movie_creator=movie_creator, movie_updater=movie_updater)

    print("\n---- CASE 1: NEW MOVIE ----")
    new_movie = Movie(title="Interstellar", synopsis="Exploration beyond the stars")
    command = movie_command_factory.build(new_movie)
    movie_admin.execute(command)

    print("\n---- CASE 2: EXISTING MOVIE ----")

    existing_movie = Movie(
        title="Interstellar (Director's Cut)", synopsis="Extended space exploration", internal_id=42,
    )
    command = movie_command_factory.build(existing_movie)
    movie_admin.execute(command)
