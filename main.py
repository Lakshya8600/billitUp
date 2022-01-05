from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Inventory.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Inventorydb = SQLAlchemy(app)

# I created Seperate database for inventory It Would be needed
class InventoryClass(Inventorydb.Model):
    sno = Inventorydb.Column(Inventorydb.Integer, primary_key=True)
    ItemName = Inventorydb.Column(Inventorydb.String(30),  nullable=False)
    Quantity = Inventorydb.Column(Inventorydb.Integer, nullable=False)
    PerCost = Inventorydb.Column(Inventorydb.Integer, nullable=False)

    def __repr__(self):
        return f"{self.sno} "

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Inventory', methods=['GET','POST'])
def Inventory():
    if request.method == 'POST':
        InventoryData = InventoryClass(ItemName=request.form['ItemName'],Quantity=request.form['ItemQuantity'],PerCost=request.form['ItemPerCost'])
        Inventorydb.session.add(InventoryData)
        Inventorydb.session.commit()

    InventoryList = InventoryClass.query.all()
    return render_template('Inventory.html' , InventoryList=InventoryList )


if __name__ == '__main__':
    app.run(debug=True)