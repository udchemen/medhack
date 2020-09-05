from flask import request, Blueprint, jsonify
import helper_functions

patient_api = Blueprint('patient_api', __name__)


# @patient_api.route("/patients", methods='GET')
# def get_patients():
#     return get_patients()


@patient_api.route("/", methods=['POST'])
def add_patient():
    data = request.get_json()
    print(data)
    return jsonify({"message": "I see your message"})
