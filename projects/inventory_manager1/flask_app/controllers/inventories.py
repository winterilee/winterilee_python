from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import inventory, product

@app.route("/dashboard")
def dashboard():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" in session:
        session.pop("current_inventory")
    all_inventories = inventory.Inventory.get_all()
    return render_template("dashboard.html", inventories = all_inventories)

@app.route("/new_inventory")
def new_inventory():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    return render_template("new_inventory.html")

@app.route("/create_inventory", methods = ["POST"])
def create_inventory():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if not inventory.Inventory.validate_inventory(request.form):
        return redirect(url_for("new_inventory"))
    else:
        data = {
            "inventory_name": request.form["inventory_name"]
        }
        inventory.Inventory.create_inventory(data)
    return redirect(url_for("dashboard"))

@app.route("/view_inventory/<int:inventory_id>")
def view_inventory(inventory_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" in session:
        session.pop("current_inventory")
    session["current_inventory"] = inventory_id
    inventory_info = inventory.Inventory.get_one(inventory_id)
    product_list = product.Product.get_all(inventory_id)
    return render_template("view_inventory.html", inventory = inventory_info, products = product_list)

@app.route("/edit_inventory/<int:inventory_id>")
def edit_inventory(inventory_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" in session:
        session.pop("current_inventory")
    session["current_inventory"] = inventory_id
    inventory_info = inventory.Inventory.get_one(inventory_id)
    return render_template("edit_inventory.html", inventory = inventory_info)

@app.route("/update_inventory/<int:inventory_id>", methods = ["POST"])
def update_inventory(inventory_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if not inventory.Inventory.validate_inventory(request.form):
        return redirect("/edit_inventory/" + str(inventory_id))
    else:
        data = {
            "id": request.form["id"],
            "inventory_name": request.form["inventory_name"]
        }
        inventory.Inventory.update_inventory(data)
    return redirect(url_for("dashboard"))