from abc import ABC, abstractmethod
from typing import Any

class Cheesecake:
    def __init__(self) -> None:
        self.__ingredients: list[str] = []
        self.__oven_temperature: int | None = None
        self.__oven_time: int | None = None
        self.__cookie_base: bool = False

    def add_ingredient(self, ingredients: list[str]) -> None:
        self.__ingredients = self.__ingredients + ingredients

    def add_cookie_base(self) -> None:
        self.__cookie_base = True

    def oven_baking(self, temperature: int, time: int) -> None:
        self.__oven_temperature = temperature
        self.__oven_time = time

    def list_ingredients(self) -> str:
        return f"Ingredients: {self.__ingredients}"


class PistachioCheesecake:
    def __init__(self) -> None:
        self.__ingredients: list[str] = []
        self.__oven_temperature: int | None = None
        self.__oven_time: int | None = None
        self.__cookie_base: bool = False

    def add_ingredient(self, ingredients: list[str]) -> None:
        self.__ingredients = self.__ingredients + ingredients

    def add_cookie_base(self) -> None:
        self.__cookie_base = True

    def oven_baking(self, temperature: int, time: int) -> None:
        self.__oven_temperature = temperature
        self.__oven_time = time

    def list_ingredients(self) -> str:
        return f"Ingredients: {self.__ingredients}"


class CheesecakeRecipe:
    def __init__(self) -> None:
        self.__ingredients: list[str] = []
        self.__oven_temperature: str | None = None
        self.__oven_time: int | None = None
        self.__cookie_base: bool = False
        self.__recipe: str = "Steps for making a cheesecake:"

    def add_ingredient(self, ingredients: list[str]) -> None:
        self.__ingredients = self.__ingredients + ingredients
        self.__recipe = self.__recipe + "\n" + f"- Mix the following ingredients: {self.__ingredients}"

    def add_cookie_base(self) -> None:
        self.__cookie_base = True
        self.__recipe = self.__recipe + "\n" + "- Add a cookie base"

    def oven_baking(self, temperature: int, time: int) -> None:
        self.__oven_temperature = temperature
        self.__oven_time = time
        self.__recipe = self.__recipe + "\n" + f"- Bake it in the oven at {self.__oven_temperature}°C for {self.__oven_time} minutes."

    def __str__(self) -> str:
        return self.__recipe


class CheesecakeBuilder(ABC):
    @abstractmethod
    def cheesecake(self) -> Any:
        pass

    @abstractmethod
    def add_base_ingredients(self) -> None:
        pass

    @abstractmethod
    def add_specific_ingredients(self) -> None:
        pass

    @abstractmethod
    def add_cookie_base(self) -> None:
        pass

    @abstractmethod
    def bake(self) -> None:
        pass

class ClassicCheesecakeBuilder(CheesecakeBuilder):
    def __init__(self) -> None:
        self.__cheesecake: Cheesecake = Cheesecake()

    def cheesecake(self) -> Cheesecake:
        return self.__cheesecake

    def add_base_ingredients(self) -> None:
        base_ingredients = ["500g cream cheese", "250g mascarpone cheese", "250g of sugar", "6 eggs", "200ml of heavy cream"]
        self.__cheesecake.add_ingredient(base_ingredients)

    def add_specific_ingredients(self) -> None:
        return

    def add_cookie_base(self) -> None:
        self.__cheesecake.add_cookie_base()

    def bake(self) -> None:
        self.__cheesecake.oven_baking(180, 35)

class PistachioCheesecakeBuilder(CheesecakeBuilder):
    def __init__(self) -> None:
        self.__cheesecake: PistachioCheesecake= PistachioCheesecake()

    def cheesecake(self) -> PistachioCheesecake:
        return self.__cheesecake

    def add_base_ingredients(self) -> None:
        base_ingredients = ["500g cream cheese", "250g mascarpone cheese", "250g of sugar", "6 eggs", "200ml of heavy cream"]
        self.__cheesecake.add_ingredient(base_ingredients)

    def add_specific_ingredients(self) -> None:
        specific_ingredients = ["Pistachio cream"]
        self.__cheesecake.add_ingredient(specific_ingredients)

    def add_cookie_base(self) -> None:
        self.__cheesecake.add_cookie_base()

    def bake(self) -> None:
        self.__cheesecake.oven_baking(200, 30)

class ClassicCheesecakeRecipeBuilder(CheesecakeBuilder):
    def __init__(self) -> None:
        self.__cheesecake: CheesecakeRecipe = CheesecakeRecipe()

    def cheesecake(self) -> CheesecakeRecipe:
        return self.__cheesecake

    def add_base_ingredients(self) -> None:
        base_ingredients = ["500g cream cheese", "250g mascarpone cheese", "250g of sugar", "6 eggs", "200ml of heavy cream"]
        self.__cheesecake.add_ingredient(base_ingredients)

    def add_specific_ingredients(self) -> None:
        return

    def add_cookie_base(self) -> None:
        self.__cheesecake.add_cookie_base()

    def bake(self) -> None:
        self.__cheesecake.oven_baking(180, 35)

class PistachioCheesecakeRecipeBuilder(CheesecakeBuilder):
    def __init__(self) -> None:
        self.__cheesecake: CheesecakeRecipe = CheesecakeRecipe()

    def cheesecake(self) -> CheesecakeRecipe:
        return self.__cheesecake

    def add_base_ingredients(self) -> None:
        base_ingredients = ["500g cream cheese", "250g mascarpone cheese", "250g of sugar", "6 eggs", "200ml of heavy cream"]
        self.__cheesecake.add_ingredient(base_ingredients)

    def add_specific_ingredients(self) -> None:
        specific_ingredients = ["Pistachio cream"]
        self.__cheesecake.add_ingredient(specific_ingredients)

    def add_cookie_base(self) -> None:
        self.__cheesecake.add_cookie_base()

    def bake(self) -> None:
        self.__cheesecake.oven_baking(200, 30)

class Director:
    def __init__(self, builder: CheesecakeBuilder) -> None:
        self.__builder: CheesecakeBuilder = builder

    def build_cheesecake(self) -> None:
        self.__builder.add_base_ingredients()
        self.__builder.add_specific_ingredients()
        self.__builder.bake()

    def build_cheesecake_with_cookie_base(self) -> None:
        self.__builder.add_base_ingredients()
        self.__builder.add_specific_ingredients()
        self.__builder.add_cookie_base()
        self.__builder.bake()

def create_cheesecakes_app() -> None:
    print("Making classic cheesecake...")
    builder = ClassicCheesecakeBuilder()
    director = Director(builder)
    director.build_cheesecake()
    cheesecake = builder.cheesecake()
    print(cheesecake.list_ingredients())

    builder = ClassicCheesecakeRecipeBuilder()
    director = Director(builder)
    director.build_cheesecake()
    cheesecake_recipe = builder.cheesecake()
    print(cheesecake_recipe)

    print("Making classic cheesecake with cookie base...")
    builder = ClassicCheesecakeBuilder()
    director = Director(builder)
    director.build_cheesecake_with_cookie_base()
    cheesecake = builder.cheesecake()
    print(cheesecake.list_ingredients())

    builder = ClassicCheesecakeRecipeBuilder()
    director = Director(builder)
    director.build_cheesecake_with_cookie_base()
    cheesecake_recipe = builder.cheesecake()
    print(cheesecake_recipe)

    print("Making classic pistachio cheesecake...")
    builder = PistachioCheesecakeBuilder()
    director = Director(builder)
    director.build_cheesecake()
    cheesecake = builder.cheesecake()
    print(cheesecake.list_ingredients())

    builder = PistachioCheesecakeRecipeBuilder()
    director = Director(builder)
    director.build_cheesecake()
    cheesecake_recipe = builder.cheesecake()
    print(cheesecake_recipe)

    print("Making classic pistachio cheesecake with cookie base...")
    builder = PistachioCheesecakeBuilder()
    director = Director(builder)
    director.build_cheesecake_with_cookie_base()
    cheesecake = builder.cheesecake()
    print(cheesecake.list_ingredients())

    builder = PistachioCheesecakeRecipeBuilder()
    director = Director(builder)
    director.build_cheesecake_with_cookie_base()
    cheesecake_recipe = builder.cheesecake()
    print(cheesecake_recipe)

if __name__ == "__main__":
    create_cheesecakes_app()

