from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from patientAPI import patient_api
import os
import heap
import sqlalchemy
import helper_functions
import uuid
import heapq


# import models

app = Flask(__name__)

# db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_user = 'root'
# db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_password = 'HikPl7fLHeu6lbvk'
# db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_name = 'patient_db'
# db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
db_connection_name = 'flask-gcloud:us-east1:patient-db'
db_socket_dir = os.environ.get("/cloudsql")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + db_user + ':' + db_password + '@35.227.99.155/patient_db?auth_plugin=mysql_native_password'
db = SQLAlchemy(app)

# creating a heap
h = []

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    breathing_difficulty = db.Column(db.Integer, nullable=False)
    conscious = db.Column(db.Boolean, nullable=False)
    pain = db.Column(db.Integer, nullable=False)
    bleeding = db.Column(db.String(30), nullable=False)
    additional_info = db.Column(db.String(500), nullable=False)
    treated = db.Column(db.Boolean, nullable=False)


db.create_all()
db.session.commit()
app.register_blueprint(patient_api)


@app.route('/patients', methods=['GET'])
#def get_all_patients():
def get_priority_patient():
    patients = Patient.query.filter(Patient.treated.like('0'))
#    heap.arrange_into_heap(helper_functions.combine_results(patients))
    # pop the element of the heap
    if len(h) != 0:
        next_patient = heapq.heappop(h)
        #return jsonify({'patients': helper_functions.combine_results(patients)})
        return jsonify({'patients': next_patient})
    else:
        return jsonify({'patients': None})

# helper function - can be moved to a different file if you want

bleeding_dict = {"No": 0, "Little": 1, "Mild": 2, "Important": 5}

def sum_values(patient):
    bleeding_value = patient.bleeding #patients[i]['bleeding']
    # if conscious == False, give 1
    # unconscious --> 8
    if (patient.conscious == False):
        conscious_num = 8
    else:
        conscious_num = 0
    sum = patient.breathing_difficulty +conscious_num + patient.pain + bleeding_dict[bleeding_value]
    return sum

@app.route('/patient/add', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_uuid = str(uuid.uuid4())
    patient = Patient(public_id=new_uuid,
                      first_name=data['first_name'],
                      last_name=data['last_name'],
                      address=data['address'],
                      date_of_birth=data['date_of_birth'],
                      postal_code=data['postal_code'],
                      breathing_difficulty=data['breathing_difficulty'],
                      conscious=data['conscious'],
                      pain=data['pain'],
                      bleeding=data['bleeding'],
                      additional_info=data['additional_info'],
                      treated=0
                      )
    db.session.add(patient)
    db.session.commit()
    # Adding elements to the heap
    priority_index = -1 * sum_values(patient)
    print(f"priority_index: {priority_index}")
    heapq.heappush(h, (priority_index, patient.public_id))
    #print(new_uuid)
    # Printing the heap
    print(h)
    return jsonify({"message": "Patient added"})


@app.route('/')
def hello_world():
    return 'Welcome to the Patient_API'


if __name__ == '__main__':
    app.run(debug=True)
