from fastapi import Depends
from typing import Annotated

from src.domain.ports.item_service_port import ItemServicePort
from src.domain.services.item_service import ItemService


def get_item_service() -> ItemServicePort:
    return ItemService()


ItemServiceDep = Annotated[ItemServicePort, Depends(get_item_service)]
