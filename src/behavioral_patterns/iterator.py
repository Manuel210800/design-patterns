from collections.abc import Iterable, Iterator
from typing import Any


class SeatingMapLayout(Iterable):
    def __init__(self, collection: list[list[str]] | None = None) -> None:
        self.__collection = collection or []

    def __getitem__(self, index: tuple[int, int]) -> Any:
        row, col = index
        return self.__collection[row][col]

    def __iter__(self) -> Iterator:
        return SeatingIterator(self)

    def get_seating_iterator(self) -> "SeatingIterator":
        return SeatingIterator(self)

    def get_reverse_seating_iterator(self) -> "ReverseSeatingIterator":
        return ReverseSeatingIterator(self)

    def num_rows(self) -> int:
        return len(self.__collection)

    def num_cols(self, row: int) -> int:
        return len(self.__collection[row])

    def add_row(self, row: list[str]) -> None:
        self.__collection.append(row)


class SeatingIterator(Iterator):
    def __init__(self, seating_map: SeatingMapLayout) -> None:
        self._seating_map = seating_map
        self._row = 0
        self._col = 0

    def __next__(self) -> Any:
        if self._row >= self._seating_map.num_rows():
            raise StopIteration

        if self._col >= self._seating_map.num_cols(self._row):
            self._row += 1
            self._col = 0
            return self.__next__()

        item = self._seating_map[self._row, self._col]
        self._col += 1
        return item


class ReverseSeatingIterator(Iterator):
    def __init__(self, seating_map: SeatingMapLayout) -> None:
        self._seating_map = seating_map
        self._row = 0
        self._col = (
            seating_map.num_cols(0) - 1 if seating_map.num_rows() > 0 else -1
        )

    def __next__(self) -> Any:
        if self._row >= self._seating_map.num_rows():
            raise StopIteration

        if self._col < 0:
            self._row += 1
            if self._row >= self._seating_map.num_rows():
                raise StopIteration
            self._col = self._seating_map.num_cols(self._row) - 1
            return self.__next__()

        item = self._seating_map[self._row, self._col]
        self._col -= 1
        return item


if __name__ == "__main__":
    seating = SeatingMapLayout(
        [
            ["A1", "A2", "A3"],
            ["B1", "B2", "B3"],
            ["C1", "C2", "C3"],
        ]
    )

    print("Normal iteration (left → right):")
    for seat in seating:
        print(seat, end=" ")
    print("\n")

    print("Reverse iteration (right → left):")
    reverse_iterator = seating.get_reverse_seating_iterator()
    for seat in reverse_iterator:
        print(seat, end=" ")
    print()