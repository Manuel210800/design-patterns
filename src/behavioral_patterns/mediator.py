from abc import ABC, abstractmethod
from typing import Optional


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

class NotificationService:
    EVENT = "purchase_notified"
    def __init__(self, checkout_mediator: Mediator) -> None:
        self.__checkout_mediator = checkout_mediator

    def notify_purchase(self) -> None:
        print("Notifying purchase...")
        print("Purchase notified")
        self.__checkout_mediator.notify(self, self.EVENT)

class PaymentService:
    EVENT = "payment_processed"
    def __init__(self, checkout_mediator: Mediator) -> None:
        self.__checkout_mediator = checkout_mediator

    def process_payment(self) -> None:
        print("Processing Payment...")
        print("Payment processed")
        self.__checkout_mediator.notify(self, self.EVENT)

class InventoryService:
    EVENT = "inventory_reserved"
    def __init__(self, checkout_mediator: Mediator) -> None:
        self.__checkout_mediator = checkout_mediator

    def reserve_items(self) -> None:
        print("Reserving items...")
        print("Items reserved")
        self.__checkout_mediator.notify(self, self.EVENT)

class LoggingService:
    def __init__(self, checkout_mediator: Mediator) -> None:
        self.__checkout_mediator = checkout_mediator

    def log_event(self, event: str) -> None:
        print(f"Logging event: {event}")

class CheckoutMediator(Mediator):
    def __init__(
            self,
    ) -> None:
        self.__notification_service: Optional[NotificationService] = None
        self.__payment_service: Optional[PaymentService] = None
        self.__inventory_service: Optional[InventoryService] = None
        self.__logging_service: Optional[LoggingService] = None

    def notify(self, sender: object, event: str) -> None:

        if event == PaymentService.EVENT:
            self.logging_service.log_event(event)
            self.inventory_service.reserve_items()

        elif event == InventoryService.EVENT:
            self.logging_service.log_event(event)
            self.notification_service.notify_purchase()

        elif event == NotificationService.EVENT:
            self.logging_service.log_event(event)
            print("Checkout process finished!")

if __name__ == "__main__":
    mediator = CheckoutMediator()

    payment_service = PaymentService(mediator)
    inventory_service = InventoryService(mediator)
    notification_service = NotificationService(mediator)
    logging_service = LoggingService(mediator)

    mediator.payment_service = payment_service
    mediator.inventory_service = inventory_service
    mediator.notification_service = notification_service
    mediator.logging_service = logging_service

    print("User confirms checkout\n")
    payment_service.process_payment()
