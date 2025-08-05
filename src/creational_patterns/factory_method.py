from abc import ABC, abstractmethod
from enum import Enum


class MusicianType(Enum):
    PIANIST = "pianist"
    GUITARIST = "guitarist"
    SINGER = "singer"

class Musician(ABC):
    @abstractmethod
    def instrument(self) -> str | None:
        pass

    @abstractmethod
    def genre(self) -> str:
        pass

class MusiciansAgency(ABC):
    @abstractmethod
    def hire(self, musician_type: MusicianType) -> Musician:
        pass

class RockMusicianAgency(MusiciansAgency):
    def hire(self, musician_type: MusicianType) -> Musician:
        if musician_type == MusicianType.PIANIST:
            return RockPianist()
        elif musician_type == MusicianType.GUITARIST:
            return RockGuitarist()
        elif musician_type == MusicianType.SINGER:
            return RockSinger()

class ClassicalMusicianAgency(MusiciansAgency):
    def hire(self, musician_type: MusicianType) -> Musician:
        if musician_type == MusicianType.PIANIST:
            return ClassicalPianist()
        elif musician_type == MusicianType.GUITARIST:
            return ClassicalGuitarist()
        elif musician_type == MusicianType.SINGER:
            return ClassicalSinger()


class RockPianist(Musician):
    def __str__(self):
        return "Rock pianist"
    def instrument(self) -> str:
        return "electric keyboard"

    def genre(self) -> str:
        return "Rock"

class RockGuitarist(Musician):
    def __str__(self):
        return "Rock guitarist"
    def instrument(self) -> str:
        return "electric guitar"

    def genre(self) -> str:
        return "Rock"

class RockSinger(Musician):
    def __str__(self):
        return "Rock singer"
    def instrument(self) -> None:
        return

    def genre(self) -> str:
        return "Rock"

class ClassicalPianist(Musician):
    def __str__(self):
        return "Classical pianist"
    def instrument(self) -> str:
        return "piano"

    def genre(self) -> str:
        return "Classical music"

class ClassicalGuitarist(Musician):
    def __str__(self):
        return "Classical guitarist"
    def instrument(self) -> str:
        return "spanish guitar"

    def genre(self) -> str:
        return "Classical music"

class ClassicalSinger(Musician):
    def __str__(self):
        return "Classical singer"
    def instrument(self) -> None:
        return

    def genre(self) -> str:
        return "Classical music"

def musician_agency_app() -> None:
    rock_agency = RockMusicianAgency()
    rock_pianist = rock_agency.hire(musician_type=MusicianType.PIANIST)
    print("New hire")
    print(f"Instrument: {rock_pianist.instrument()}")
    print(f"Genre: {rock_pianist.genre()}")

    classical_agency = ClassicalMusicianAgency()
    classical_guitarist = classical_agency.hire(musician_type=MusicianType.GUITARIST)
    print("New hire")
    print(f"Instrument: {classical_guitarist.instrument()}")
    print(f"Genre: {classical_guitarist.genre()}")
    classical_singer = classical_agency.hire(musician_type=MusicianType.SINGER)
    print("New hire")
    print(f"Instrument: {classical_singer.instrument()}")
    print(f"Genre: {classical_singer.genre()}")

if __name__ == "__main__":
    musician_agency_app()