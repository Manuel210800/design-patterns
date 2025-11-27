from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from uuid import UUID


class Redis:
    def set(self, key: str, object: dict) -> None:
        print(f"Storing the object {object} in key {key} ...")

    def get(self, key: str) -> Optional[dict]:
        print(f"Obtaining the object associated with the key: {key} ...")
        return {"id": "11111111-1111-1111-1111-111111111111", "title": "Mocked attribute"}

    def invalidate(self, key: str) -> None:
        print(f"Removing the key entry: {key} ...")

@dataclass
class Attribute:
    id: UUID
    title: str

class AttributeCacheAdapter(ABC):
    @abstractmethod
    def save(self, attribute: Attribute) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[Attribute]:
        pass

    @abstractmethod
    def delete(self, attribute: Attribute) -> None:
        pass

class RedisAttributeCacheAdapter(AttributeCacheAdapter):
    def __init__(self, redis: Redis) -> None:
        self.__redis = redis

    def save(self, attribute: Attribute) -> None:
        object = {"id": attribute.id, "title": attribute.title}
        key = str(attribute.id)
        self.__redis.set(key, object)

    def find_by_id(self, id: UUID) -> Optional[Attribute]:
        object = self.__redis.get(id)
        if object is None:
            return None

        return Attribute(**object)

    def delete(self, attribute: Attribute) -> None:
        key = str(attribute.id)
        self.__redis.invalidate(key)

def adapter_app() -> None:
    cache_adapter: AttributeCacheAdapter = RedisAttributeCacheAdapter(Redis())

    attribute = Attribute(id="11111111-1111-1111-1111-111111111111", title="Mocked attribute")

    print("\n--- SAVING ATTRIBUTE ---")
    cache_adapter.save(attribute)

    print("\n--- RETRIEVING ATTRIBUTE ---")
    retrieved = cache_adapter.find_by_id(attribute.id)
    print("Retrieved:", retrieved)

    print("\n--- DELETING ATTRIBUTE ---")
    cache_adapter.delete(attribute)

if __name__ == "__main__":
    adapter_app()