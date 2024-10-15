import httpx

async def validate_payment_gateway(transaction_data):
    # Simulando uma chamada para um gateway de pagamento externo
    async with httpx.AsyncClient() as client:
        response = await client.post("http://mock-payment-gateway/validate", json=transaction_data)
        return response.json()
    
async def get_product_price(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://product-service/products/{product_id}")
        response.raise_for_status()  # Levanta um erro se a requisição falhar
        return response.json()