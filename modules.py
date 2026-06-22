# =========================
# 1. DEBUGGING BASICS
# =========================

name = "Ruchika"
print("Print Debug:", name)

# PDB Debugging (removed for production)


# =========================
# 2. PYTHON CONCEPT SIMULATION
# =========================

# Fake Product data (no Django here)
products = [
    {"id": 1, "name": "Apple", "price": 100},
    {"id": 2, "name": "Orange", "price": 120},
]

# Simulate "GET API"
def get_products():
    return products

print("Products:", get_products())


# =========================
# 3. SERIALIZER SIMULATION (NO DJANGO)
# =========================

def fake_serializer(data):
    required_fields = ["name", "price"]

    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}

    return {"validated_data": data}


data = {"name": "Mango", "price": 200}
print("Serializer Output:", fake_serializer(data))


# =========================
# 4. SERVICE LAYER SIMULATION
# =========================

class ProductService:

    @staticmethod
    def get_all():
        return products

    @staticmethod
    def create(product):
        products.append(product)
        return product


print("Service Output:", ProductService.get_all())


# =========================
# 5. SIMPLE ASYNC DEMO (ONLY CONCEPT)
# =========================

import asyncio

async def hello():
    print("Async running...")
    await asyncio.sleep(1)
    print("Done async")

asyncio.run(hello())