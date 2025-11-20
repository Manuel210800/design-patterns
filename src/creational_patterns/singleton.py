# ----- Singleton ----- #
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# ----- use case ----- #
@singleton
class ProductionDetailRepository:
    def find_all(self):
        pass

def singleton_app() -> None:
    repository1= ProductionDetailRepository()
    repository2= ProductionDetailRepository()

    print("===== Singleton =====\n")
    print(f"First instantiation {id(repository1)}, Second instantiation {id(repository2)}")
    if repository1 == repository2:
        print("Singleton works.")
    else:
        print("Singleton failed.")

if __name__ == "__main__":
    singleton_app()