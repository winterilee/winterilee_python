from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products JOIN inventories ON products.inventory_id = inventories.id;"
        results = connectToMySQL(cls.db).query_db(query)
        product_list = []
        for row in results:
            one_product = {
                "id": row["id"],
                "product_name": row["product_name"],
                "product_count": row["product_count"],
                "inventory_id": row["inventories.id"]
            }
            product_list.append(one_product)
        return product_list
    
    @classmethod
    def get_one(cls, product_id):
        query = "SELECT * FROM products WHERE id = %(id)s;"
        data = {"id": product_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @staticmethod
    def validate_product(product):
        is_valid = True
        if len(product["product_name"]) <= 0:
            flash("Product name is required.", "product")
            is_valid = False
        elif len(product["product_name"]) < 3:
            flash("Product name must be at least 3 characters.", "product")
            is_valid = False
        if product["product_count"] <= 0:
            flash("Invalid amount.", "product")
            is_valid = False
        return is_valid