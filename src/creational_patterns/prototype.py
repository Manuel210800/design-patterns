import copy
from enum import Enum


class CouponType(Enum):
    GODCOUPON = "god_coupon"
    TESTCOUPON = "test_coupon"
    MARKETINGCOUPON = "marketing_coupon"

class Coupon:
    def __init__(
            self,
            code: str,
            type: CouponType,
            title: str,
            available_coupons: int,
            amount: int,
            one_use_per_user: bool,
            restrictions: dict
    ) -> None:
        self.__code = code
        self.__type = type
        self.__title = title
        self.__available_coupons = available_coupons
        self.__amount = amount
        self.__one_use_per_user = one_use_per_user
        self.__restrictions = restrictions

    def __deepcopy__(self, memodict: dict | None = None) -> "Coupon":
        if memodict is None:
            memodict = {}

        restrictions = copy.deepcopy(self.__restrictions, memodict)
        new_coupon = self.__class__(
            code=self.__code,
            type=self.__type,
            title=self.__title,
            available_coupons=self.__available_coupons,
            amount=self.__amount,
            one_use_per_user=self.__one_use_per_user,
            restrictions=restrictions,
        )
        new_coupon.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new_coupon

    def __str__(self) -> str:
        return f"Code: {self.__code}, Type: {self.__type}, Title: {self.__title}, Available Coupons: {self.__available_coupons}, Amount: {self.__amount}, One use per user: {self.__one_use_per_user}, Restrictions: {self.__restrictions}"

def prototype_app():
    original = Coupon(
        code="GODCOUPONTESTING",
        type=CouponType.GODCOUPON,
        title="God coupon for testing",
        available_coupons=20,
        amount=100,
        one_use_per_user=False,
        restrictions={"min_purchase": 50, "categories": ["movie", "onebox"]}
    )

    clone = copy.deepcopy(original)

    print("=== Prototype ===")
    print("\n")
    print(f"Original ID: {id(original)}")
    print(f"Clone ID:    {id(clone)}")
    print("\n")
    print(f"Original coupon: {original}")
    print(f"Clone coupon: {clone}")
    print("\n")
    print(f"Original restrictions ID: {id(original._Coupon__restrictions)}")
    print(f"Clone restrictions ID:    {id(clone._Coupon__restrictions)}")
    print("\nUpdating clone.restrictions['min_purchase'] = 999")
    clone._Coupon__restrictions["min_purchase"] = 999
    print("Original restrictions:", original._Coupon__restrictions)
    print("Clone restrictions:", clone._Coupon__restrictions)


if __name__ == "__main__":
    prototype_app()