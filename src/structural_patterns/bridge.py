from abc import ABC, abstractmethod

class ContentProvider(ABC):
    @abstractmethod
    def get_plan(self) -> None:
        pass

class ContentPorviderAtomtickets(ContentProvider):
    def get_plan(self) -> None:
        print("Obtaining a plan for the Atomticketes provider ...")

class ContentProviderViator(ContentProvider):
    def get_plan(self) -> None:
        print("Obtaining a plan for the Viator provider ...")

class Fever:
    def __init__(self, content_provider: ContentProvider) -> None:
        self.__content_provider = content_provider

    def import_main_plan(self) -> None:
        print("Importing Main Plan into Fever ...")
        self.__content_provider.get_plan()

def bridge_app(content_provider: ContentProvider) -> None:
    fever = Fever(content_provider)
    fever.import_main_plan()

if __name__ == "__main__":
    print("=== Using Atomtickets Provider ===")
    atom_provider = ContentPorviderAtomtickets()
    bridge_app(atom_provider)

    print("=== Using Viator Provider ===")
    viator_provider = ContentProviderViator()
    bridge_app(viator_provider)