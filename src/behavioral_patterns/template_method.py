from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Seat:
    row: int
    column: int
    label: str
    type: str | None = None
    available: bool | None = None


@dataclass
class SeatArea:
    seats: list[Seat]


class LayoutFormatter(ABC):
    def format(self, raw_seats: list[dict]) -> SeatArea:
        seat_area = self.parse_seats_ids_and_label(raw_seats)
        seat_area = self.add_seat_types_to_seat_area(raw_seats, seat_area)
        seat_area = self.check_seat_availability(raw_seats, seat_area)
        return seat_area

    @abstractmethod
    def parse_seats_ids_and_label(self, raw_seats: list[dict]) -> SeatArea:
        pass

    @abstractmethod
    def add_seat_types_to_seat_area(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        pass

    @abstractmethod
    def check_seat_availability(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        pass

class CineSyncLayoutFormatter(LayoutFormatter):
    """
    {
        "row": 1,
        "column": 5,
        "label": "A5",
        "seat_type": "VIP",
        "is_available": True
    }
    """

    def parse_seats_ids_and_label(self, raw_seats: list[dict]) -> SeatArea:
        seats = [
            Seat(
                row=seat["row"],
                column=seat["column"],
                label=seat["label"]
            )
            for seat in raw_seats
        ]
        return SeatArea(seats=seats)

    def add_seat_types_to_seat_area(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        for raw, seat in zip(raw_seats, seat_area.seats):
            seat.type = raw.get("seat_type")
        return seat_area

    def check_seat_availability(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        for raw, seat in zip(raw_seats, seat_area.seats):
            seat.available = raw.get("is_available")
        return seat_area


class AdmitOneLayoutFormatter(LayoutFormatter):
    """
    {
        "position": {"r": 1, "c": 5},
        "meta": {"label": "A5"},
        "attributes": {"type": "VIP"},
        "status": "free"  # "free" | "occupied"
    }
    """

    def parse_seats_ids_and_label(self, raw_seats: list[dict]) -> SeatArea:
        seats = [
            Seat(
                row=seat["position"]["r"],
                column=seat["position"]["c"],
                label=seat["meta"]["label"]
            )
            for seat in raw_seats
        ]
        return SeatArea(seats=seats)

    def add_seat_types_to_seat_area(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        for raw, seat in zip(raw_seats, seat_area.seats):
            seat.type = raw.get("attributes", {}).get("type")
        return seat_area

    def check_seat_availability(self, raw_seats: list[dict], seat_area: SeatArea) -> SeatArea:
        for raw, seat in zip(raw_seats, seat_area.seats):
            seat.available = raw.get("status") == "free"
        return seat_area


if __name__ == "__main__":
    cine_sync_data = [
        {"row": 1, "column": 1, "label": "A1", "seat_type": "VIP", "is_available": True},
        {"row": 1, "column": 2, "label": "A2", "seat_type": "NORMAL", "is_available": False},
    ]
    admit_one_data = [
        {
            "position": {"r": 1, "c": 1},
            "meta": {"label": "A1"},
            "attributes": {"type": "VIP"},
            "status": "free"
        },
        {
            "position": {"r": 1, "c": 2},
            "meta": {"label": "A2"},
            "attributes": {"type": "NORMAL"},
            "status": "occupied"
        },
    ]

    cine_formatter = CineSyncLayoutFormatter()
    admit_formatter = AdmitOneLayoutFormatter()

    cine_result = cine_formatter.format(cine_sync_data)
    admit_result = admit_formatter.format(admit_one_data)

    print("CineSync result:")
    for seat in cine_result.seats:
        print(seat)

    print("\nAdmitOne result:")
    for seat in admit_result.seats:
        print(seat)