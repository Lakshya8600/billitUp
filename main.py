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
    return render_template('Inventory.html' , InventoryList=InventoryList, InventaryUpdate=0, Heading="Add", btnname="Submit" )

@app.route('/Inventorydelete/<int:sno>')
def Inventorydelete(sno):
    InventoryList2 = InventoryClass.query.filter_by(sno=sno).first()
    Inventorydb.session.delete(InventoryList2)
    Inventorydb.session.commit()
    return redirect("/Inventory")

@app.route('/InventoryUpdate/<int:sno>', methods=['GET','POST'])
def InventoryUpdate(sno):
    InventoryList = InventoryClass.query.all()
    InventoryList3 = InventoryClass.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        
        Inventorydb.ItemName = request.form['ItemName']
        Inventorydb.Quantity = request.form['ItemQuantity']
        Inventorydb.PerCost = request.form['ItemPerCost']
        Inventorydb.session.add(InventoryList3)
        Inventorydb.session.commit()
        return redirect('/Inventory')

    return render_template('Inventory.html' , InventoryList=InventoryList, InventaryUpdate=InventoryList3, Heading="Update",btnname="Update")

if __name__ == '__main__':
    app.run(debug=True)