from abc import ABC, abstractmethod
from enum import Enum

from factory_method import Musician, ClassicalPianist


class ConcertVenue(ABC):
    @abstractmethod
    def rental_price(self) -> int:
        pass

    @abstractmethod
    def music_genre(self) -> str:
        pass

class Decoration(ABC):
    @abstractmethod
    def furniture(self) -> str:
        pass


class ConcertFactory(ABC):
    @abstractmethod
    def create_venue(self) -> ConcertVenue:
        pass

    @abstractmethod
    def create_artist(self) -> Musician:
        pass

    @abstractmethod
    def create_decoration(self) -> Decoration:
        pass

class Auditorium(ConcertVenue):
    def rental_price(self) -> int:
        return 10000

    def music_genre(self) -> str:
        return "Classical Music"

class CandlelightDecoration(Decoration):
    def furniture(self) -> str:
        return "Candles"

class Stadium(ConcertVenue):
    def rental_price(self) -> int:
        return 200000

    def music_genre(self) -> str:
        return "Electronic music"

class ElectronicDecoration(Decoration):
    def furniture(self) -> str:
        return "Fireworks"

class ElectronicDj(Musician):
    def instrument(self) -> str | None:
        return "Mixing table"

    def genre(self) -> str:
        return "Electronic music"

class CandlelightConcertFactory(ConcertFactory):
    def create_venue(self) -> Auditorium:
        return Auditorium()

    def create_artist(self) -> ClassicalPianist:
        return ClassicalPianist()

    def create_decoration(self) -> CandlelightDecoration:
        return CandlelightDecoration()

class ElectronicMusicConcertFactory(ConcertFactory):
    def create_venue(self) -> Stadium:
        return Stadium()

    def create_artist(self) -> ElectronicDj:
        return ElectronicDj()

    def create_decoration(self) -> ElectronicDecoration:
        return ElectronicDecoration()

class ConcertType(Enum):
    ELECTRIC = "electronic"
    CANDLELIGHT = "candlelight"

class ConcertFactorySelector:
    def select(self, concert_type: ConcertType) -> ConcertFactory:
        if concert_type == ConcertType.ELECTRIC:
            return ElectronicMusicConcertFactory()
        elif concert_type == ConcertType.CANDLELIGHT:
            return CandlelightConcertFactory()

def create_concert_app(concert_type: ConcertType) -> None:
    concert_factory = ConcertFactorySelector().select(concert_type)
    concert_venue = concert_factory.create_venue()
    concert_artist = concert_factory.create_artist()
    concert_decoration = concert_factory.create_decoration()
    print(f"Renting the venue costs ${concert_venue.rental_price()} and is the perfect setting for a {concert_venue.music_genre()} concert.")
    print(f"The artist selected for the concert plays the instrument: {concert_artist.instrument()}, and belongs to the following genre: {concert_artist.genre()}")
    print(f"The necessary decoration for the concert is the following: {concert_decoration.furniture()}")

if __name__ == "__main__":
    print("Creating Candlelight...")
    create_concert_app(ConcertType.CANDLELIGHT)
    print("Creating an electronic music concert...")
    create_concert_app(ConcertType.ELECTRIC)