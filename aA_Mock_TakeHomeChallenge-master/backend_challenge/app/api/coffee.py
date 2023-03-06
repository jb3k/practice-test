from flask import Blueprint, session, request, redirect


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
    


@coffee_routes.route('/coffee/delete/<int:id>', methods=['DELETE'])
def delete_coffee(id):
    coffeId = Coffee.query.get(id)

    if coffeId == None:
        return{"error": "coffee couldn't be found"}, 404
    db.session.delete(coffeeId)
    db.session.commit()
    return {'message': Successfully deleted}
