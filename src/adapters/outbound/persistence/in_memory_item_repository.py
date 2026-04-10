from typing import List

from src.domain.models.item import Item
from src.domain.ports.item_repository_port import ItemRepositoryPort


class InMemoryItemRepository(ItemRepositoryPort):
    def __init__(self):
        self.next_id = 1
        default_item = Item(id=self.next_id, name="some item")
        
        self.items = [default_item]

    def delete(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    def get_all(self) -> List[Item]:
        return self.items

    # return list(self.items.values())

    def get_by_id(self, id: int) -> Item:
        return self.items[id]

    def create(self, item: Item) -> Item:
        self.next_id += 1
        item.id = self.next_id
        self.items[item.id] = item
        return self.items[item.id]

    def update(self, item: Item) -> Item:
        if item.id is None:
            raise RuntimeError("Item does not has an ID. It cannot be updated")

        if self.items[item.id] is None:
            raise RuntimeError("Item not found")

        self.items[item.id] = item

        return self.items[item.id]

    def delete(self, item: Item) -> bool:
        if item.id in self.items:
            del self.items[item.id]
            return True
        return False
