from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Product
from flask_login import login_required, current_user
from . import db


routes = Blueprint("routes", __name__)


@routes.route("/products")
@login_required
def products():
    products = Product.query.filter_by(user_id=current_user.id).order_by(Product.created_at.desc()).all()
    return render_template("products.html", title="Products", user=current_user, products=products)

@routes.route("/product/<int:id>/edit", methods=['POST', 'GET'])
@login_required
def edit_product(id):
    products = Product.query.get_or_404(id)
    if request.method == 'POST':
        name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        currency = request.form.get("currency")
        price = request.form.get("price")
        
        
        products.name = name
        products.category = category
        products.quantity = quantity
        products.currency = currency
        products.price = price
        
        db.session.commit()
        
        flash('Product updated successfully', category='success')
        
        return redirect(url_for("routes.products"))

    return render_template("edit_product.html", title="Edit Product", user=current_user, product=products)



@routes.route("product/<int:id>/delete", methods=['POST', 'GET'])
@login_required
def delete_product(id):
    products = Product.query.get_or_404(id)
    
    db.session.delete(products)
    db.session.commit()
    
    flash("Product deleted successfully!", category='success')
    return redirect(url_for("routes.products"))



@routes.route("/products/add", methods=["POST", "GET"])
@login_required
def add_product():
    if request.method == "POST":
        
        name = request.form.get("name")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        currency = request.form.get("currency")
        price = request.form.get("price")
        
        product = Product.query.filter_by(name=name, user_id=current_user.id).first()
        if product:
            flash("Product with that name already exists.", category="error")
            return redirect(url_for("routes.add_product"))

        new_product = Product(
            name=name,
            category=category,
            quantity=quantity,
            currency=currency,
            price=price,
            user_id=current_user.id,
        )

        db.session.add(new_product)
        db.session.commit()
        flash("Product has been added, check your product page", category="success")
        return redirect(url_for("routes.add_product"))

    return render_template("add_product.html", title="Add Product", user=current_user)

