from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData 

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata= MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

#DEFINING THE CLOTHES TABLE 
class Clothes(db.Model, SerializerMixin):
    __tablename__ = 'clothes'
    clothes_id = db.Column(db.Integer, primary_key=True)
    designer_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)

    #ASSOCIATION PROXIES
    #relationship to CDassociation table
    CDassociation= db.relationship("CDassociation", back_populates="clothes")
    designer= association_proxy("CDassociation", "designer")
    serialize_rules = ("-CDassociation.clothes", )

#VALIDATION FOR THE DESIGNER NAME
    @validates('designer_name')
    def validate_designer_name(self, key, designer_name):
        if len(designer_name) > 100:
            print('Designer name is too long')
        return designer_name
    
    #VALIDATION FOR THE DESCRIPTION
    @validates('description')
    def validate_description(self, key, description):
        if len(description) > 1000:
            print('Description is too long')
        return description
    
    #VALIDATION FOR THE PRICE
    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, int):
            print('Price must be an integer')
        return price
    
    def __repr__(self):
        return f"clothes '{self.name}'"

#DEFINING THE DESIGNER TABLE 
class Designer(db.Model, SerializerMixin):
    __tablename__ = 'designer'
    designer_id = db.Column(db.Integer, primary_key=True)
    name_of_designer = db.Column(db.String(100), nullable=False)
    store_location = db.Column(db.String(1000), nullable=False)

    #ASSOCIATION PROXIES
    #relationship to Clothes table
    CDassociation = db.relationship("CDassociation", back_populates="designer")
    clothes = association_proxy("CDassociation", "clothes")
    serialize_rules = ("-CDassociation.designer",)

    #VALIDATING NAME OF DESIGNER
    @validates('name_of_designer')
    def validate_name_of_designer(self, key, name_of_designer):
        if len(name_of_designer) > 100:
            print('Name of designer is too long')
        return name_of_designer
    
    #VALIDATING STORE LOCATION
    @validates('store_location')
    def validate_store_location(self, key, store_location):
        if len(store_location) > 1000:
            print('Store location is too long')
        return store_location
    
    def __repr__(self):
        return f"designer '{self.name}'"

#DEFINING THE CD TABLE 
class CDassociation(db.Model, SerializerMixin):
    __tablename__ = 'cdassociation'
    cd_id = db.Column(db.Integer, primary_key=True)
    clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.clothes_id'))
    designer_id = db.Column(db.Integer, db.ForeignKey('designer.designer_id'))
    item_in_stock = db.Column(db.Boolean, nullable=False)

    #ASSOCIATION PROXIES
    clothes= db.relationship("Clothes", back_populates="CDassociation")
    designer= db.relationship("Designer", back_populates="CDassociation")
    serialize_rules = ("-clothes.CDassociation", "-designer.CDassociation")

    #VALIDATING ITEM IN STOCK
    @validates('item_in_stock')
    def validate_item_in_stock(self, key, item_in_stock):
        if not isinstance(item_in_stock, bool):
            print('Item in stock must be a boolean')
        return item_in_stock