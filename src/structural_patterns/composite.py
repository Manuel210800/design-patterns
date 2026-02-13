from abc import ABC, abstractmethod


class Plan(ABC):
    @abstractmethod
    def price(self) -> int:
        pass

    @abstractmethod
    def add_booking_fees(self) -> None:
        pass

class Movie(Plan):
    def __init__(self) -> None:
        self.__price = 15
        self.__booking_fees = 4

    def price(self) -> int:
        return self.__price

    def add_booking_fees(self) -> None:
        print(f"[FEES] Adding booking fees ({self.__booking_fees}) to Movie")
        self.__price += self.__booking_fees

class Dinner(Plan):
    def __init__(self) -> None:
        self.__price = 30
        self.__booking_fees = 0

    def price(self) -> int:
        return self.__price

    def add_booking_fees(self) -> None:
        print(f"[FEES] Adding booking fees ({self.__booking_fees}) to Dinner")
        self.__price += self.__booking_fees

class Candlelight(Plan):
    def __init__(self) -> None:
        self.__price = 35
        self.__booking_fees = 2

    def price(self) -> int:
        return self.__price

    def add_booking_fees(self) -> None:
        print(f"[FEES] Adding booking fees ({self.__booking_fees}) to Candlelight")
        self.__price += self.__booking_fees

class Bundle(Plan):
    def __init__(self) -> None:
        self.__plans: list[Plan] = []

    def add(self, plan: Plan) -> None:
        print(f"[ADD] Adding {plan.__class__.__name__} to Bundle")
        self.__plans.append(plan)

    def remove(self, plan: Plan) -> None:
        self.__plans.remove(plan)

    def price(self) -> int:
        print("[PRICE] Calculating Bundle total price...")
        total_price = 0
        for plan in self.__plans:
            total_price += plan.price()

        return total_price

    def add_booking_fees(self) -> None:
        print("[FEES] Propagating booking fees to Bundle children...")
        for plan in self.__plans:
            plan.add_booking_fees()

def valentines_day_plan():
    print("\n===== VALENTINE'S DAY PLAN =====")

    candlelight = Candlelight()
    dinner = Dinner()

    valentines_day_plan = Bundle()
    valentines_day_plan.add(candlelight)
    valentines_day_plan.add(dinner)

    print("\n[ACTION] Applying booking fees...")
    valentines_day_plan.add_booking_fees()

    print("\n[ACTION] Calculating total price...")
    price = valentines_day_plan.price()

    print(f"\n[RESULT] Valentine's Day total price: {price}€")
    return price

def valentines_weekend_plan():
    print("\n===== VALENTINE'S WEEKEND PLAN =====")

    candlelight = Candlelight()
    dinner_1 = Dinner()

    saturday_plan = Bundle()
    saturday_plan.add(candlelight)
    saturday_plan.add(dinner_1)

    movie = Movie()
    dinner_2 = Dinner()

    sunday_plan = Bundle()
    sunday_plan.add(movie)
    sunday_plan.add(dinner_2)

    valentines_weekend_plan = Bundle()
    valentines_weekend_plan.add(saturday_plan)
    valentines_weekend_plan.add(sunday_plan)

    print("\n[ACTION] Applying booking fees to entire weekend plan...")
    valentines_weekend_plan.add_booking_fees()

    print("\n[ACTION] Calculating total weekend price...")
    price = valentines_weekend_plan.price()

    print(f"\n[RESULT] Valentine's Weekend total price: {price}€")
    return price

if __name__ == "__main__":
    print("======= COMPOSITE PATTERN DEMO =======")

    day_price = valentines_day_plan()
    weekend_price = valentines_weekend_plan()

    print("\n======= SUMMARY =======")
    print(f"Valentine's Day Plan: {day_price}€")
    print(f"Valentine's Weekend Plan: {weekend_price}€")
