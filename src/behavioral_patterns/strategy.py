from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Venue:
    venue_id: int
    vendor_id: str
    vendor_venue_id: int

@dataclass
class Showtime:
    production_id: int
    vendor_showtime_id: int

class DiscoveryService(ABC):
    @abstractmethod
    def get_showtimes(self, venue: Venue) -> list[Showtime]:
        pass

class CinesyncDiscoveryService(DiscoveryService):
    def get_showtimes(self, venue: Venue) -> list[Showtime]:
        print(f"Retrieving showtimes from vendor {venue.vendor_id} using the CINESYNC POS system")
        return [Showtime(production_id=1, vendor_showtime_id=34), Showtime(production_id=2, vendor_showtime_id=84)]

class AdmitOneDiscoveryService(DiscoveryService):
    def get_showtimes(self, venue: Venue) -> list[Showtime]:
        print(f"Retrieving showtimes from vendor {venue.vendor_id} using the ADMITONE POS system")
        return [Showtime(production_id=3, vendor_showtime_id=56), Showtime(production_id=4, vendor_showtime_id=92)]

class AtomticketsDiscoveryService(DiscoveryService):
    def get_showtimes(self, venue: Venue) -> list[Showtime]:
        print(f"Retrieving showtimes from the database for vendor {venue.vendor_id}")
        return [Showtime(production_id=5, vendor_showtime_id=63), Showtime(production_id=6, vendor_showtime_id=74)]

class DiscoveryServiceSelector:
    def select(self, venue: Venue) -> DiscoveryService:
        if venue.vendor_id == "TEST_CINESYNC":
            return CinesyncDiscoveryService()
        if venue.vendor_id == "TEST_ADMITONE":
            return AdmitOneDiscoveryService()

        return AtomticketsDiscoveryService()

class IngestionManager:
    def __init__(self, discovery_service_selector: DiscoveryServiceSelector):
        self.__discovery_service_selector = discovery_service_selector

    def get_showtimes(self, venue: Venue) -> list[Showtime]:
        discovery_service = self.__discovery_service_selector.select(venue)
        return discovery_service.get_showtimes(venue)

if __name__ == "__main__":
    selector = DiscoveryServiceSelector()
    manager = IngestionManager(selector)

    print("\n--- 1. Using Cinesync strategy ---")
    cinesync_venue = Venue(
        venue_id=1,
        vendor_id="TEST_CINESYNC",
        vendor_venue_id=101
    )
    showtimes = manager.get_showtimes(cinesync_venue)
    print(f"Retrieved showtimes: {showtimes}")

    print("\n--- 2. Using AdmitOne strategy ---")
    admitone_venue = Venue(
        venue_id=2,
        vendor_id="TEST_ADMITONE",
        vendor_venue_id=202
    )
    showtimes = manager.get_showtimes(admitone_venue)
    print(f"Retrieved showtimes: {showtimes}")

    print("\n--- 3. Using default (AtomTickets) strategy ---")
    atom_venue = Venue(
        venue_id=3,
        vendor_id="UNKNOWN_VENDOR",
        vendor_venue_id=303
    )
    showtimes = manager.get_showtimes(atom_venue)
    print(f"Retrieved showtimes: {showtimes}")
