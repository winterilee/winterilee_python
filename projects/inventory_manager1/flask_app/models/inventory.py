from flask_app.config.mysqlconnection import connectToMySQL

class Inventory:
    db = "python_inventory_manager1_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.inventory_name = data["inventory_name"]
        self.inventory_status = data["inventory_status"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
