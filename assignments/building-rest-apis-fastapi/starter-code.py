from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Item API")


class Item(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)


class ItemInDB(Item):
    id: int


items_db: list[ItemInDB] = []


@app.get("/health")
def read_health():
    return {"status": "ok"}


# TODO: add POST /items
# TODO: add GET /items/{item_id}
# TODO: add GET /items
