from flask import Flask, request, make_response, jsonify, render_template
import os
from flask_migrate import Migrate
from models import db, Clothes, Designer, CDassociation

app = Flask(__name__)
DATABASE = "sqlite:///app.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
app.debug = True
migrate = Migrate(app, db)

db.init_app(app)



@app.route('/', methods=['GET'])
def home():
    return {"message": "Welcome to Jandrew's Closet!"}

#GET ROUTE TO VEIW ALL CLOTHES FROM THE CLOTHES TABLE
@app.route('/clothes', methods=['GET'])
def get_clothes():
    clothes = Clothes.query.all()
    data = [clothes.to_dict() for clothes in clothes]

    return make_response(jsonify(data), 200)

#GET ROUTE TO VIEW CLOTHES BY ID
@app.route('/clothes/<int:clothes_id>', methods=['GET'])
def get_clothes_by_id(clothes_id: int):
    matching_clothes = Clothes.query.filter(Clothes.clothes_id == clothes_id).first()
    if matching_clothes:
        return make_response(jsonify(matching_clothes.to_dict()), 200)
    else:
        return make_response(jsonify({"message": "Clothes not found"}), 404)

    
#POST ROUTE TO ADD NEW CLOTHES TO THE CLOTHES TABLE
@app.route('/clothes', methods=['POST'])
def add_new_clothes():
    try:
        new_clothes = Clothes(
            designer_name= request.json["designer_name"],
            description= request.json["description"],
            price= request.json["price"],
            image_url= request.json["image_url"]
        )
        db.session.add(new_clothes)
        db.session.commit()
        return make_response(jsonify(new_clothes.to_dict()), 201)
    except: 
        return make_response(jsonify({"message": "Could not add new clothes"}), 400)
    
#PATCH ROUTE TO UPDATE CLOTHES BASED OFF ID
@app.route('/clothes/<int:id>', methods=['PATCH'])
def update_clothes_by_id(clothes_id: int):
    matching_clothes = Clothes.query.filter(Clothes.clothes_id == clothes_id).first()
    try:
        payload = request.get_json()
        for key in payload:
            setattr(matching_clothes, key, payload[key])
            db.session.add(matching_clothes)
            db.session.commit()
            return make_response(jsonify(matching_clothes.to_dict()), 200)
    except:
        return make_response(jsonify({"message": "Could not update clothes"}), 400)
    
#DELETE ROUTE TO DELETE CLOTHES BASED OFF ID
@app.route('/clothes/<int:id>', methods=['DELETE'])
def delete_clothes_by_id(clothes_id: int):
    matching_clothes = Clothes.query.filter(Clothes.clothes_id == clothes_id).first()
    try:
        db.session.delete(matching_clothes)
        db.session.commit()
        return make_response(jsonify({"message": "Clothes deleted"}), 200)
    except:
        return make_response(jsonify({"message": "Could not delete clothes"}), 400)
    

#GET ROUTE TO VEIW ALL DESIGNERS FROM THE DESIGNER TABLE
@app.route('/designers', methods=['GET'])
def get_designers():
    designers = Designer.query.all()
    data = [designers.to_dict() for designers in designers]

    return make_response(jsonify(data), 200)

#GET ROUTE TO VIEW DESIGNERS BY ID
@app.route('/designers/<int:designers_id>', methods=['GET'])
def get_designers_by_id(designers_id: int):
    matching_designer = Designer.query.filter(Designer.designer_id == designers_id).first()
    if matching_designer:
        return make_response(jsonify(matching_designer.to_dict()), 200)
    else:
        return make_response(jsonify({"message": "Designer not found"}), 404)

    
#POST ROUTE TO ADD NEW DESIGNERS TO THE DESIGNER TABLE
@app.route('/designers', methods=['POST'])
def add_new_designers():
    try:
        new_designers = Designer(
            name_of_designer= request.json["name_of_designer"],
            store_location= request.json["store_location"]
        )
        db.session.add(new_designers)
        db.session.commit()
        return make_response(jsonify(new_designers.to_dict()), 201)
    except: 
        return make_response(jsonify({"message": "Could not add new designers"}), 400)
    
#PATCH ROUTE TO UPDATE DESIGNERS BASED OFF ID
@app.route('/designers/<int:designers_id>', methods=['PATCH'])
def update_designers_by_id(designers_id: int):
    matching_designer = Designer.query.filter(Designer.designer_id == designers_id).first()
    if not matching_designer:
        return make_response(jsonify({"message": "Designer not found"}), 404)

    try:
        payload = request.get_json()
        for key, value in payload.items():
            if hasattr(matching_designer, key):
                setattr(matching_designer, key, value)
        db.session.commit()
        return make_response(jsonify(matching_designer.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Could not update designer", "error": str(e)}), 400)

    
#DELETE ROUTE TO DELETE DESIGNERS BASED OFF ID
@app.route('/designers/<int:designers_id>', methods=['DELETE'])
def delete_designers_by_id(designers_id: int):
    matching_designer = Designer.query.filter(Designer.designer_id == designers_id).first()
    if not matching_designer:
        return make_response(jsonify({"message": "Designer not found"}), 404)

    try:
        db.session.delete(matching_designer)
        db.session.commit()
        return make_response(jsonify({"message": "Designer deleted"}), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Could not delete designer", "error": str(e)}), 400)
    
#ASSOCIATION METHOD ROUTES


#GET ROUTE TO VIEW ALL CLOTHES ASSOCIATED TO A DESIGNER
@app.route('/designers/<int:designers_id>/clothes', methods=['GET'])
def get_clothes_by_designer(designers_id: int):
    matching_designer = Designer.query.filter(Designer.designer_id == designers_id).first()
    if not matching_designer:
        return make_response(jsonify({"message": "Designer not found"}), 404)

    # Assuming a relationship like 'clothes' exists in the Designer model
    clothes_list = matching_designer.clothes
    clothes_data = [clothes.to_dict() for clothes in clothes_list]  # Convert each clothes object to a dictionary

    return make_response(jsonify(clothes_data), 200)

#GET ROUTE TO VIEW ALL DESIGNERS ASSOCIATED TO A CLOTHES
@app.route('/clothes/<int:clothes_id>/designers', methods=['GET'])
def get_designers_by_clothes(clothes_id: int):
    matching_clothes = Clothes.query.filter(Clothes.clothes_id == clothes_id).first()
    if not matching_clothes:
        return make_response(jsonify({"message": "Clothes not found"}), 404)

    # Assuming a relationship like 'designers' exists in the Clothes model
    designers_list = matching_clothes.designers
    designers_data = [designers.to_dict() for designers in designers_list]  # Convert each designers object to a dictionary

    return make_response(jsonify(designers_data), 200)

    
if __name__ == "__main__":
    app.run(port=5000)