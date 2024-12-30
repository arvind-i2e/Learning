from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data.db"
db=SQLAlchemy(app)
app.app_context().push()
class Drink(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    desc=db.Column(db.String(120))
    def __repr__(Self):
         return f"{Self.name} - {Self.desc}"

@app.route('/')
def index():
    return "Hello! universe"

@app.route('/drinks')
def drinks():
    drinks=Drink.query.all()
    output=[]
    for drink in drinks:
        drink_data={'name':drink.name,'description':drink.desc}
        output.append(drink_data)
    return {"drinks":output}
@app.route('/drinks/<id>')
def get_drink(id):
    drink=Drink.query.get_or_404(id)
    return {"name":drink.name,"description":drink.desc} # if we not use dictionary over here than we have to use jsonify module
@app.route('/drinks',methods=['POST'])
def add_drink():
    drink=Drink(name=request.json['name'],desc=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}
@app.route('/drinks/<id>',methods=['DELETE'])
def delete_drink(id):
    drink=Drink.query.get(id)
    if drink is None:
        return {"error":"Not Found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"yeet!@"}
@app.route('/drinks/<int:id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get(id)
    if not drink:
        return jsonify({"error": "Drink not found"})
    drink.name = request.json.get('name', drink.name)
    drink.desc = request.json.get('description', drink.desc)
    db.session.commit()
    return jsonify({"Message":"Updated the details successfully"})
if __name__=="__main__":
    app.run(debug=True,port=8000)