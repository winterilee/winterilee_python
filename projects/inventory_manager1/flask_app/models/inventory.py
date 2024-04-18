from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Inventory:
    db = "python_inventory_manager1_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.inventory_name = data["inventory_name"]
        self.inventory_status = data["inventory_status"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_inventory(cls, data):
        query = "INSERT INTO inventories (inventory_name, inventory_status) VALUES (%(inventory_name)s, 1);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM inventories;"
        results = connectToMySQL(cls.db).query_db(query)
        inventory_list = []
        for row in results:
            one_inventory = {
                "id": row["id"],
                "inventory_name": row["inventory_name"],
                "inventory_status": row["inventory_status"]
            }
            inventory_list.append(one_inventory)
        return inventory_list
    
    @classmethod
    def get_one(cls, inventory_id):
        query = "SELECT * FROM inventories WHERE id = %(id)s;"
        data = {"id": inventory_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update_inventory(cls, data):
        query = "UPDATE inventories SET inventory_name = %(inventory_name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_inventory(inventory):
        is_valid = True
        if len(inventory["inventory_name"]) <= 0:
            flash("Inventory name is required.", "inventory")
            is_valid = False
        elif len(inventory["inventory_name"]) < 3:
            flash("Inventory name must be at least 3 characters", "inventory")
            is_valid = False
        return is_valid