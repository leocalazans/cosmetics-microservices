from fastapi import APIRouter, HTTPException, Depends
from .schemas import TransactionCreate, CartItem
from .redis_client import add_item_to_cart, get_cart, clear_cart
from .database import SessionLocal
from .models import Transaction
from .services import validate_payment_gateway, get_product_price

router = APIRouter()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart")
async def add_to_cart(item: CartItem):
    user_id = item.user_id  # Supondo que o ID do usuário é passado no corpo do item
    add_item_to_cart(user_id, item)
    return {"message": "Item added to cart."}

@router.get("/cart/{user_id}")
async def view_cart(user_id: int):
    cart = get_cart(user_id)
    if not cart:
        return {"message": "Your cart is empty."}
    return cart

@router.post("/checkout")
async def checkout(transaction: TransactionCreate):
    cart = get_cart(transaction.user_id)
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty.")

    total_price = 0
    for item in transaction.items:
        product_info = await get_product_price(item.product_id)
        total_price += product_info['price'] * item.quantity  # Considerando que o preço está no campo 'price'

    transaction_data = {
        "user_id": transaction.user_id,
        "total_price": total_price,
        "items": cart
    }

    payment_response = await validate_payment_gateway(transaction_data)

    if payment_response.get("accepted"):
        new_transaction = Transaction(user_id=transaction.user_id, total_price=total_price, status="accepted")
        # Aqui você deve adicionar a lógica para salvar a nova transação no banco de dados.
        clear_cart(transaction.user_id)  # Limpar o carrinho após a compra
        return {"message": "Transaction successful."}
    else:
        return {"message": "Transaction failed.", "status": "rejected"}