from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from patientAPI import patient_api
import os
import sqlalchemy
import models

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
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+mysqlconnector://' + db_user + ':' + db_password + '@35.227.99.155/patient_db?auth_plugin=mysql_native_password'

# models.init_app(app)
# models.create_tables(app)
app.register_blueprint(patient_api)


@app.route('/')
def hello_world():
    return 'Welcome to the Patient_API'


if __name__ == '__main__':
    app.run()
