from flask_app.config.mysqlconnection import connectToMySQL

class Product:
    db = "python_inventory_manager1_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.product_name = data["product_name"]
        self.product_count = data["product_count"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.inventory_id = data["inventory_id"]

    @classmethod
    def create_product(cls, data):
        query = "INSERT INTO products (product_name, product_count, inventory_id) VALUES (%(product_name)s, %(product_count)s, %(inventory_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)