from flask import Blueprint, session, request, redirect

coffee_routes = Blueprint('coffee', __name__)

@coffee_routes.route('/coffee/ping', methods=['GET'])
def get_status():
    return {'status': 'good'}
