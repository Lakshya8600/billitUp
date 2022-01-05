from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///databases/Inventory.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Inventorydb = SQLAlchemy(app)

# I created Seperate database for inventory It Would be needed
class User(Inventorydb.Model):
    srno = Inventorydb.Column(Inventorydb.Integer, primary_key=True)
    ItemName = Inventorydb.Column(Inventorydb.String(30),  nullable=False)
    Quantity = Inventorydb.Column(Inventorydb.Integer, nullable=False)
    PerCost = Inventorydb.Column(Inventorydb.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.srno

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Inventory')
def Inventory():
    return render_template('Inventory.html')


if __name__ == '__main__':
    app.run(debug=True)