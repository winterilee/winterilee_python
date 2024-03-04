from flask_app.config.mysqlconnection import connectToMySQL

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
                "inventory_name": row["inventory_name"]
            }
            inventory_list.append(one_inventory)
        return inventory_list