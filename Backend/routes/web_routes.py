from flask import Blueprint, render_template, jsonify , render_template
from services.hardware_services import sensors



bp = Blueprint('main',__name__)


#web
@bp.route('/')
def index():
    return render_template('views/index.html')

#mobile
@bp.route('/api/sensors')
def sensor_details():
    return jsonify(sensors())

