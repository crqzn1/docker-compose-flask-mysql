import os
from flask import Flask
from flask import current_app

import json

app = Flask(__name__)
# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))

# import mysql.connector
# def favorite_colors():
#     config = {
#         'user': 'root',
#         'password': 'root',
#         'host': 'db',
#         'port': '3306',
#         'database': 'knights'
#     }
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM favorite_colors')
#     results = [{name: color} for (name, color) in cursor]
#     cursor.close()
#     connection.close()

#     return results

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@db:3306/knights?auth_plugin=mysql_native_password"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] = True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.secret_key = '1234'
db = SQLAlchemy(app)

class Color(db.Model):
    __tablename__ = 'favorite_colors'
    name = db.Column(db.String(20), primary_key=True)
    color = db.Column(db.String(20))
    def __repr__(self):
        return "<Color: {}>".format(self.color)

def favorite_colors():
    colors = Color.query.all()
    results = [{color.name: color.color} for color in colors]
    return results

@app.route('/')
def index():
    return json.dumps({'favorite_colors': favorite_colors()})

from flask import send_from_directory
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', 
                               mimetype='image/vnd.microsoft.icon'
                               )
    # return current_app.send_static_file('static/favicon.ico')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
