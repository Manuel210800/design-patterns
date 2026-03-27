from abc import ABC, abstractmethod
from typing import Any


class Memento(ABC):
    @abstractmethod
    def get_state(self) -> Any:
        pass


class SeatingMemento(Memento):
    def __init__(self, seats: list[tuple[int, int]]) -> None:
        self.__seats = seats.copy()

    def get_state(self) -> list[tuple[int, int]]:
        return self.__seats


class SeatingMap:
    def __init__(self, selected_seats: list[tuple[int, int]]) -> None:
        self.__selected_seats = selected_seats

    def select_seat(self, row: int, col: int) -> None:
        print(f"Selecting seat ({row}, {col})")
        self.__selected_seats.append((row, col))
        print(f"Current seats: {self.__selected_seats}")

    def select_best_seats(self) -> None:
        print("Choosing the best seats ...")
        best_seats: list[tuple[int, int]] = []

        for i in range(len(self.__selected_seats)):
            best_seats.append((5, 4 + i))

        self.__selected_seats = best_seats
        print(f"Seats updated to: {self.__selected_seats}")

    def restore(self, memento: Memento) -> None:
        self.__selected_seats = memento.get_state()
        print(f"Seats restored: {self.__selected_seats}")

    def create_snapshot(self) -> SeatingMemento:
        print("Creating a snapshot ...")
        return SeatingMemento(self.__selected_seats)

    def show(self) -> None:
        print(f"Current seats: {self.__selected_seats}")


class SeatingMapCareTaker:
    def __init__(self, seating_map: SeatingMap) -> None:
        self.__backups: list[SeatingMemento] = []
        self.__seating_map = seating_map

    def backup(self) -> None:
        print("\nSaving SeatingMap state ...")
        self.__backups.append(self.__seating_map.create_snapshot())

    def undo(self) -> None:
        if not self.__backups:
            print("No history to undo")
            return

        backup = self.__backups.pop()
        print("\nRestoring previous state ...")
        self.__seating_map.restore(backup)

    def show_history(self) -> None:
        print("\nHistory of states:")
        for i, backup in enumerate(self.__backups):
            print(f"{i}: {backup.get_state()}")


if __name__ == "__main__":
    print("\n========== PROGRAM START ==========\n")
    seating_map = SeatingMap(selected_seats=[])
    caretaker = SeatingMapCareTaker(seating_map)

    print("\n--- Step 1: Initial manual seat selection ---")
    seating_map.select_seat(1, 1)
    seating_map.select_seat(1, 2)

    print("\n--- Step 2: Saving snapshot (State A) ---")
    caretaker.backup()

    print("\n--- Step 3: User continues selecting seats ---")
    seating_map.select_seat(2, 3)

    print("\n--- Step 4: Saving snapshot (State B) ---")
    caretaker.backup()

    print("\n--- Step 5: System selects best seats automatically ---")
    seating_map.select_best_seats()

    print("\nCurrent state after automatic selection:")
    seating_map.show()

    print("\n--- Step 6: Performing UNDO (restore to State B) ---")
    caretaker.undo()
    seating_map.show()

    print("\n--- Step 7: Performing another UNDO (restore to State A) ---")
    caretaker.undo()
    seating_map.show()

    print("\n--- Step 8: Attempting another UNDO (no more history expected) ---")
    caretaker.undo()

    print("\n--- Step 9: Showing remaining history ---")
    caretaker.show_history()

    print("\n========== PROGRAM END ==========\n")