import os
from flask import Flask
import json

app = Flask(__name__)

# import mysql.connector
# import config
# def favorite_colors():
#     connection = mysql.connector.connect(**config.MYSQL_CONNECTOR_CONFIG)
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM favorite_colors')
#     results = [{name: color} for (name, color) in cursor]
#     cursor.close()
#     connection.close()
#     return results

from flask_sqlalchemy import SQLAlchemy
import config
app.config.from_object(config)
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
