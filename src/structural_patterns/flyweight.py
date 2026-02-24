from typing import Dict, List


class SessionType:
    def __init__(self, session_cover_image: str, fever_logo: str) -> None:
        self.__session_cover_image = session_cover_image
        self.__fever_logo = fever_logo

    def display(self, session_intrinsic_state: Dict) -> None:
        print(f"Session [{session_intrinsic_state['starts_at']}, {session_intrinsic_state['price']}] "
              f"-> Cover Image: {self.__session_cover_image}, Fever Logo: {self.__fever_logo}")


class SessionTypeFactory:
    _flyweights: Dict[str, SessionType] = {}

    def get_flyweight(self, session_cover_image: str, fever_logo: str) -> SessionType:
        key = f"{session_cover_image}_{fever_logo}"
        if key not in self._flyweights:
            print("SessionTypeFactory: Creating new SessionType Flyweight.")
            self._flyweights[key] = SessionType(session_cover_image, fever_logo)
        else:
            print("SessionTypeFactory: Reusing existing SessionType Flyweight.")
        return self._flyweights[key]

    def list_flyweights(self):
        print(f"SessionTypeFactory has {len(self._flyweights)} flyweights:")
        for key in self._flyweights:
            print(f"- {key}")


class Session:
    def __init__(self, starts_at: str, price: float, session_type_flyweight: SessionType) -> None:
        self.__starts_at = starts_at
        self.__price = price
        self.__session_type_flyweight = session_type_flyweight

    def display(self):
        self.__session_type_flyweight.display({
            "starts_at": self.__starts_at,
            "price": self.__price
        })


class MainPlan:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__sessions: List[Session] = []

    def add_session(self, session: Session) -> None:
        self.__sessions.append(session)

    def display_sessions(self):
        print(f"\nMainPlan: {self.__name} sessions:")
        for session in self.__sessions:
            session.display()


if __name__ == "__main__":
    factory = SessionTypeFactory()

    child_type = factory.get_flyweight("child_cover.png", "fever_logo.png")
    adult_type = factory.get_flyweight("adult_cover.png", "fever_logo.png")

    factory.list_flyweights()

    main_plan = MainPlan("Plan Vacacional Febrero")

    main_plan.add_session(Session("2026-03-01 10:00", 20.0, child_type))
    main_plan.add_session(Session("2026-03-01 14:00", 25.0, adult_type))
    main_plan.add_session(Session("2026-03-02 10:00", 22.0, child_type))
    main_plan.add_session(Session("2026-03-02 14:00", 27.0, adult_type))

    main_plan.display_sessions()