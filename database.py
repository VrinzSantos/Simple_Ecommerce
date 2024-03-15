from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["sales"]  # Replace "sales" with your desired collection name

    def insert_sale(self, product):
        self.collection.insert_one({"product": product})

    def get_latest_sales(self, limit=10):
        return list(self.collection.find().sort("_id", -1).limit(limit))

# Sample usage
if __name__ == "__main__":
    # Example MongoDB URI and database name
    uri = "mongodb://localhost:27017/"
    dbname = "ecommerce"

    # Initialize MongoDB manager
    manager = MongoDBManager(uri, dbname)

    # Sample product data (replace with actual product data)
    products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6", "Product 7", "Product 8"
                , "Product 9", "Product 10", "Product 11", "Product 12"]

    # Insert sample sales data
    for product in products:
        manager.insert_sale(product)

    # Retrieve latest sales data
    latest_sales = manager.get_latest_sales()
    print("Latest sales:")
    for sale in latest_sales:
        print(sale)
