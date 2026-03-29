from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: "Observer") -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class Movie(Subject):
    def __init__(self, title: str, synopsis: str, cast: list[str], crew: list[str]) -> None:
        self.__observers = []
        self._title = title
        self._synopsis = synopsis
        self._cast = cast
        self._crew = crew
        self._cities: list[str] = []

    def add_observer(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)

    def set_cities(self, cities: list[str]) -> None:
        self._cities = cities
        self.notify()

class CreateAdsObserver(Observer):
    def update(self, subject: Subject) -> None:
        print(f"Creating ads for the movie {subject._title} in the following cities: {subject._cities} ...")

class MovieUpdatedObserver(Observer):
    def update(self, subject: Subject) -> None:
        print(f"Updating the movie {subject._title} information across all related main pages")

if __name__ == "__main__":
    print("============== EXAMPLE ==============\n")
    print("Creating movie object...")
    movie = Movie(
        title="Inception",
        synopsis="A thief who steals corporate secrets through dream-sharing technology.",
        cast=["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        crew=["Christopher Nolan"]
    )

    print("Creating and attaching observers...")
    ads_observer = CreateAdsObserver()
    movie.add_observer(ads_observer)
    update_observer = MovieUpdatedObserver()
    movie.add_observer(update_observer)

    print("Setting cities where the movie will be released...\n")
    movie.set_cities(["New York", "Los Angeles"])
    print("\nChange completed. Observers have been notified.")

    print("\nRemoving Ads observer...\n")
    movie.remove_observer(ads_observer)

    print("Updating cities again...\n")
    movie.set_cities(["Chicago", "San Francisco"])
