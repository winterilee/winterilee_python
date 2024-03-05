from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import inventory

@app.route("/dashboard")
def dashboard():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    all_inventories = inventory.Inventory.get_all()
    return render_template("dashboard.html", inventories = all_inventories)

@app.route("/new_inventory")
def new_inventory():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    return render_template("new_inventory.html")

@app.route("/create_inventory", method = ["POST"])
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
    inventory_info = inventory.Inventory.get_one(inventory_id)
    return render_template("view_inventory.html", inventory = inventory_info)