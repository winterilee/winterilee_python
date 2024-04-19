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
        return redirect("/new_product/" + str(session['current_inventory']))
    else:
        data = {
            "product_name": request.form["product_name"],
            "product_count": int(request.form["product_count"]),
            "inventory_id": request.form["inventory_id"]
        }
        product.Product.create_product(data)
    return redirect("/view_inventory/" + str(session['current_inventory']))

@app.route("/edit_product/<int:product_id>")
def edit_product(product_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" not in session:
        return redirect(url_for("dashboard"))
    product_info = product.Product.get_one(product_id)
    return render_template("edit_product.html", product = product_info)

@app.route("/update_product/<int:product_id>", methods = ["POST"])
def update_product(product_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if "current_inventory" not in session:
        return redirect(url_for("dashboard"))
    if not product.Product.validate_product(request.form):
        return redirect("/edit_product/" + str(product_id))
    else:
        data = {
            "id": request.form["id"],
            "product_name": request.form["product_name"],
            "product_count": request.form["product_count"]
        }
        product.Product.update_product(data)
    return redirect("/view_inventory/" + str(session['current_inventory']))