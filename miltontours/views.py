from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Food, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    categorys = Category.query.order_by(Category.name).all()
    return render_template('index.html', categorys = categorys)

@bp.route('/foods/<int:categoryid>/')
def categoryfoods(categoryid):
    foods = Food.query.filter(Food.category_id == categoryid)
    return render_template('categoryfood.html', foods = foods)

@bp.route('/foods/')
def search():
    search = request.arg.get('search')
    search = '%{}%'.format(search)
    foods = Food.query.filter(Food.description.like(search)).all
    return render_template('categoryfood.html', foods = foods)


# Referred to as "Basket" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    food_id = request.values.get('food_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for food in order.food:
            totalprice = totalprice + food.price
    
    # are we adding an item?
    if food_id is not None and order is not None:
        food = Food.query.get(food_id)
        if food not in order.food:
            try:
                order.food.append(food)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        food_to_delete = Food.query.get(id)
        try:
            order.food.remove(food_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for food in order.food:
                totalcost = totalcost + food.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! One of our awesome team members will contact you soon...')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)