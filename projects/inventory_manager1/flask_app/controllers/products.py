from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import product

@app.route("/new_product/<int:inventory_id>")
def new_product(inventory_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" in session:
        session.pop("current_inventory")
    session["current_inventory"] = inventory_id
    return render_template("new_product.html")

@app.route("/create_product", methods = ["POST"])
def create_product():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if not product.Product.validate_product(request.form):
        return redirect(url_for("new_product"))
    else:
        data = {
            "product_name": request.form["product_name"],
            "product_count": int(request.form["product_count"]),
            "inventory_id": request.form["inventory_id"]
        }
        product.Product.create_product(data)
    return redirect("/view_inventory/<int:session['current_inventory']>")