from __future__ import annotations
from abc import ABC, abstractmethod


class Cart:
    def __init__(self, state: CartState) -> None:
        self.__state = None
        self.transition_to(state)

    def transition_to(self, state: CartState) -> None:
        print(f"Cart: Transition to {type(state).__name__}")
        self.__state = state
        self.__state.cart = self

    def book(self) -> None:
        self.__state.book()

    def cancel(self) -> None:
        self.__state.cancel()

class CartState(ABC):
    @property
    def cart(self) -> Cart:
        return self._cart

    @cart.setter
    def cart(self, cart: Cart) -> None:
        self._cart = cart

    @abstractmethod
    def book(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass

class CreatedCart(CartState):
    def book(self) -> None:
        print("Cart created: Leasing seats in provider")
        self._cart.transition_to(PreparedCart())

    def cancel(self) -> None:
        print("Discarding a created cart")
        self._cart.transition_to(CanceledCart())

class PreparedCart(CartState):
    def book(self) -> None:
        print("Cart prepared: Creating the Order and Processing Payment")
        self._cart.transition_to(ConfirmedCart())

    def cancel(self) -> None:
        print("Unleasing seats in provider and discarding cart")
        self._cart.transition_to(CanceledCart())

class ConfirmedCart(CartState):
    def book(self) -> None:
        print("Cart is already confirmed")

    def cancel(self) -> None:
        print("Cancelling order in provider and discarding cart")
        self._cart.transition_to(CanceledCart())

class CanceledCart(CartState):
    def book(self) -> None:
        print("Cart is canceled, you can't book it")

    def cancel(self) -> None:
        print("Cart is already canceled")

if __name__ == "__main__":
    print("\n--- 1. Full flow: Created -> Prepared -> Confirmed -> Canceled ---")
    cart1 = Cart(CreatedCart())
    cart1.book()
    cart1.book()
    cart1.cancel()

    print("\n--- 2. Interrupted flow: Created -> Prepared -> Canceled ---")
    cart2 = Cart(CreatedCart())
    cart2.book()
    cart2.cancel()

    print("\n--- 3. Attempt to book an already confirmed cart ---")
    cart3 = Cart(CreatedCart())
    cart3.book()
    cart3.book()
    cart3.book()

    print("\n--- 4. Operations on an already canceled cart ---")
    cart4 = Cart(CreatedCart())
    cart4.cancel()
    cart4.book()
    cart4.cancel()
