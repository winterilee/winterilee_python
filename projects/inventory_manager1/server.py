from flask_app import app
from flask_app.controllers import users, inventories, products

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 5001)