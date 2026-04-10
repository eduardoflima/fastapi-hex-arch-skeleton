from typing import List

from src.domain.models.item import Item
from src.domain.ports.item_service_port import ItemServicePort


class ItemService(ItemServicePort):

    def getItems(self) -> List[Item]:
        return [Item(id=1, name="some item")]

    def getItem(self, id: int) -> Item:
        return Item(id=id, name="some existing item")

    def createItem(self, name: str) -> Item:
        return Item(id=2, name=name)

    def updateItem(self, id: int, name: str) -> Item:
        return Item(id=id, name=name)

    def deleteItem(self, id: int) -> None:
        print(f"deleted item id {id}")
