from pydantic import BaseModel

class ItemCreateRequest(BaseModel):
    name: str

class ItemUpdateRequest(BaseModel):
    id: int
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str