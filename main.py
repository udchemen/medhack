from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from patientAPI import patient_api
import os
import models

app = Flask(__name__)

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:HikPl7fLHeu6lbvk@35.227.99.155/patient-db'
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)


db.create_all()
db.session.commit()

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'ThisIsSecretKey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:HikPl7fLHeu6lbvk@35.227.99.155/patient_db?auth_plugin=mysql_native_password'
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + db_user + ':' + db_password + '@' + db_connection_name + '/' + db_name + '?auth_plugin=mysql_native_password'
# print(db_user + db_password + db_name + db_connection_name)
# models.init_app(app)
# models.create_tables(app)
app.register_blueprint(patient_api)


@app.route('/')
def hello_world():
    return 'Welcome to the Patient_API'


if __name__ == '__main__':
    app.run()
