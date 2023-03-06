from flask import Blueprint, session, request, redirect
from app.forms import CoffeeForm
from app.models import Coffee


coffee_routes = Blueprint('coffee', __name__)

@coffee_routes.route('/coffee/ping', methods=['GET'])
def get_status():
    return {'status': 'good'}


@coffee_routes.route('/coffee', methods=['GET'])
def get_coffee():
    # get index of all coffees in asc order by name


@coffee_routes.route('/coffee/<int:id>', methods=['GET'])
def get_coffee_id():
    coffeeId = Coffee.query.get(id)
    if coffeeId == None:
        return{"error": "coffee couldn't be found"}, 404
    return coffeeId


@coffee_routes.route('/coffee/create', methods=['POST'])
def create_coffee():
    form = CoffeeForm()
    all_coffees = Coffee.query.all()

    if form.validate_on_submit():
        new_coffee = Coffee(
            name = form.data['name'],
            year = form.data['year'],
            caffine = form.data['caffine']
        )
        db.session.add(new_coffee)
        db.session.commit()
        return {'coffee': [items.to_dict for items in all_coffees]}
    return {'error': validation_errors_to_error_message(CoffeeForm.errors)}, 400



@coffee_routes.route('/coffee/delete/<int:id>', methods=['DELETE'])
def delete_coffee(id):
    coffeId = Coffee.query.get(id)

    if coffeId == None:
        return{"error": "coffee couldn't be found"}, 404
    db.session.delete(coffeeId)
    db.session.commit()
    return {'message': Successfully deleted}
