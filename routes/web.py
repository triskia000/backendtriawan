from flask import Blueprint
from controllers.menu_controllers import get_all_menu, add_menu, update_menu, delete_menu

web = Blueprint('web', __name__)
web.route('/menu', methods=['GET'])(get_all_menu)
web.route("/menu", methods=['POST'])(add_menu)
web.route("/menu/<int:id_menu>", methods=['PUT'])(update_menu)
web.route("/menu/<int:id_menu>", methods=['DELETE'])(delete_menu)