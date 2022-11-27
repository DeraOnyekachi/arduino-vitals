from flask import Blueprint, jsonify, request
from .models import load, save

views = Blueprint('views', __name__)

@views.route("/edit-vitals", methods=["POST"])
def edit():
    data = save(dict(request.form))
    return jsonify(data)

@views.route("/view-vitals")
def view():
    return jsonify(load())
