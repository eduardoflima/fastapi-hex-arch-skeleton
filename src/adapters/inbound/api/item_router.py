from fastapi import APIRouter, status

from src.domain.models.item import ItemResponse, ItemCreateRequest, ItemUpdateRequest

next_id = 1

router = APIRouter(prefix="/items")

@router.get("/")
def get_items():
    return [ItemResponse(id=1, name="some item")]


@router.get("/{item_id}")
def get_item(item_id: int):
    return ItemResponse(id=item_id, name="some item")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreateRequest):
    global next_id
    next_id += 1
    return ItemResponse(id=next_id, name=item.name)


@router.put("/{item_id}")
def update_item(item: ItemUpdateRequest):
    return ItemResponse(id=item.id, name=item.name)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    print("deleted")
