def salesEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "productName":item["productName"],
        "quantity":item["quantity"],
        "price":item["price"],
        "totalPrice":item["totalPrice"]
    }

def salesListEntity(entity) -> list:
    return [salesEntity(item) for item in entity]