from typing import TypeVar, Callable, ParamSpec
from uuid import UUID, uuid4

S = TypeVar("S")
P = ParamSpec("P")
ALLOWED_USERS: list[UUID] = [UUID("11111111-1111-1111-1111-111111111111"), UUID("22222222-2222-2222-2222-222222222222")]
def auth_required(allow_all_users: bool = False) -> Callable[[Callable[P, S]], Callable[P, S]]:
    def decorator(function: Callable[P, S]) -> Callable[P, S]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> S:
            if not allow_all_users:
                user_id = args[1]
                if user_id not in ALLOWED_USERS:
                    print(f"Unauthorized user: {user_id}")
                    raise Exception(f"Unauthorized user: {user_id}")

            return function(*args, **kwargs)

        return wrapper

    return decorator

class OrderController:
    def __init__(self) -> None:
        pass

    @auth_required(allow_all_users=True)
    def get(self, user_id: UUID, order_id: UUID) -> dict:
        print(f"Retrieving Order {str(order_id)} associated with User {str(user_id)} ...")
        return {"order_id": str(order_id)}

    @auth_required()
    def post(self, user_id: UUID) -> None:
        print(f"Creating an order for user {str(user_id)} ...")


def decorator_app() -> None:
    controller = OrderController()

    allowed_user = UUID("11111111-1111-1111-1111-111111111111")
    unauthorized_user = UUID("99999999-9999-9999-9999-999999999999")

    order_id = uuid4()

    print("\n--- CASE 1: Public endpoint (allow_all_users=True) ---")
    controller.get(unauthorized_user, order_id)

    print("\n--- CASE 2: Protected endpoint, AUTHORIZED user ---")
    try:
        controller.post(allowed_user)
    except Exception as e:
        print("ERROR:", e)

    print("\n--- CASE 3: Protected endpoint, UNAUTHORIZED user ---")
    try:
        controller.post(unauthorized_user)
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    decorator_app()
