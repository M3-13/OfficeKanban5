from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["boards"])


@router.get("/boards")
def list_boards():
    return {"message": "Not implemented"}


@router.post("/boards")
def create_board():
    return {"message": "Not implemented"}


@router.get("/boards/{id}/cards")
def list_cards(id: int):
    return {"message": "Not implemented"}


@router.post("/boards/{id}/cards")
def create_card(id: int):
    return {"message": "Not implemented"}


@router.put("/cards/{id}")
def update_card(id: int):
    return {"message": "Not implemented"}


@router.delete("/cards/{id}")
def delete_card(id: int):
    return {"message": "Not implemented"}


@router.patch("/cards/{id}/status")
def update_card_status(id: int):
    return {"message": "Not implemented"}
