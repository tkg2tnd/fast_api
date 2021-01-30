from fastapi import APIRouter

router = APIRouter()

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@router.get("/")
async def get_items():
    return {"items": items}

@router.get("/{item_id}")
async def get_item(item_id: str):
    return {"item": items[item_id]}