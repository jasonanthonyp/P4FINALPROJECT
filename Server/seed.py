from app import app
from models import db, Clothes, Designer, CDassociation
import random

with app.app_context():

    #Creating EACH DESIGNER FOR THE DESIGNER TABLE
    Supreme = Designer(name_of_designer='Supreme', store_location='NYC')
    Burberry = Designer(name_of_designer='Burberry', store_location='London')
    Calvin_Klein = Designer(name_of_designer='Calvin Klein', store_location = 'NYC')
    Aime_Leon_Dore = Designer(name_of_designer='Aime Leon Dore', store_location='NYC')
    Tom_Ford = Designer(name_of_designer='Tom Ford', store_location='NYC')
    Louis_Vuitton = Designer(name_of_designer='Louis Vuitton', store_location='Paris')
    Balmain = Designer(name_of_designer='Balmain', store_location='London')
    Dior = Designer(name_of_designer='Dior', store_location='London')
    Fendi= Designer(name_of_designer='Fendi', store_location='London')
    Dolce_and_Gabbana = Designer(name_of_designer='Dolce and Gabbana', store_location='Paris')

    Designers = [Supreme, Burberry, Calvin_Klein, Aime_Leon_Dore, Tom_Ford, Louis_Vuitton, Balmain, Dior, Fendi, Dolce_and_Gabbana]

    #CREATING EACH CLOTHING ITEM FOR THE CLOTHES TABLE
    Dolce_and_Gabbana_Sweater = Clothes(designer_name='Dolce and Gabbana', description='Sweater', price=205, image_url="Images/DGSweater.jpg")
    Dolce_and_Gabbana_Kimono= Clothes(designer_name='Dolce and Gabbana', description='Sheer Kimono', price=480, image_url="Images/DGK.jpg")
    Dior_Vneck_Top = Clothes(designer_name='Dior', description='Vneck Top', price=175, image_url="Images/DiorV.jpg")
    Dior_Sleeveless_Sweater = Clothes(designer_name='Dior', description= "sleeveless sweater", price=199, image_url="Images/DiorSweater.jpg")
    Fendi_Handbag = Clothes(designer_name='Fendi', description='Handbag', price=695, image_url="Images/FendiClutch.jpg")
    Fendi_Clutch = Clothes(designer_name='Fendi', description='Clutch', price=455, image_url="Images/FendiClutch.jpg")
    LV_Jacket= Clothes(designer_name='Louis Vuitton', description='Jacket', price=805, image_url="Images/LVJacket.jpg")
    LV_Down_Puffer_Jacket = Clothes(designer_name='Louis Vuitton', description='Down Puffer Jacket', price=1095, image_url="Images/LVPuffer.jpg")
    Balmain_Snakeskin_Jacket = Clothes(designer_name='Balmain', description='Snakeskin Jacket', price=795, image_url="Images/BalmainSnakeSkin.jpg")
    Balmain_Varsity_Jacket = Clothes(designer_name='Balmain', description='Varsity Jacket', price=896, image_url="Images/BalmainVJ.jpg")
    Tom_Ford_Sunglasses = Clothes(designer_name='Tom Ford', description='Sunglasses', price=385, image_url="Images/TFSunglasses.jpg")
    Tom_Ford_Suits = Clothes(designer_name='Tom Ford', description='Suits', price=1205, image_url="Images/TFSuit.jpg")
    ALD_Suits = Clothes(designer_name='Aime Leon Dore', description='Beige Suit', price=1200, image_url="Images/ALDSuit.jpg")
    ALD_Winter_Jacket = Clothes(designer_name='Aime Leon Dore', description='Winter Jacket', price=800, image_url="Images/ALDWinterJacket.jpg")
    CK_Underwear = Clothes(designer_name='Calvin Klein', description='Underwear', price=45, image_url="Images/CKUnderwear.jpg")
    CK_Jeans = Clothes(designer_name='Calvin Klein', description='Jeans', price=195, image_url="Images/CKJeans.jpg")
    Supreme_Denim_Jacket = Clothes(designer_name='Supreme', description='Denim Jacket', price=655, image_url="Images/SupremeDenim.jpg")
    Supreme_Tracksuit = Clothes(designer_name='Supreme', description='Tracksuit', price=995, image_url="Images/SupremeTracksuit.jpg")
    Burberry_Sunglasses = Clothes(designer_name='Burberry', description='Sunglasses', price=405, image_url="Images/BurberrySunglasses.jpg")
    Burberry_Trenchcoat = Clothes(designer_name='Burberry', description='Trenchcoat', price=2305, image_url="Images/BurberryTrench.jpg")

Clothes = [Dolce_and_Gabbana_Sweater, Dolce_and_Gabbana_Kimono, Dior_Vneck_Top, Dior_Sleeveless_Sweater, Fendi_Handbag, Fendi_Clutch, LV_Jacket, LV_Down_Puffer_Jacket,  Balmain_Snakeskin_Jacket, Balmain_Varsity_Jacket, Tom_Ford_Sunglasses, Tom_Ford_Suits, ALD_Suits, ALD_Winter_Jacket, CK_Jeans, CK_Underwear, Supreme_Denim_Jacket, Supreme_Tracksuit, Burberry_Sunglasses, Burberry_Trenchcoat]


#Define a function to create associations between clothes and designers
#Clothing and Designer are linked if Designer.name_of_designer == Clothes.designer_name
#Function randomly assignes iss_in_stock to each association
def create_association_relationships(Clothes, Designers):
    sample_association_relationship = []
    for clothes in Clothes:
        designer = next((designer for designer in Designers if designer.name_of_designer == clothes.designer_name), None)
        if designer:
            item_in_stock = random.choice([True, False])
            association = CDassociation(clothes_id=clothes.clothes_id, designer_id=designer.designer_id, item_in_stock=item_in_stock)
            sample_association_relationship.append(association)
    return sample_association_relationship
        
from app import app
from models import db, Clothes, Designer, CDassociation
import random

with app.app_context():
    # Delete existing data first
    print("\n\t>> Deleting all existing data...")
    Designer.query.delete()
    Clothes.query.delete()
    CDassociation.query.delete()
    db.session.commit()
    print("\t>> Data deletion successful!")

    # Create and add new Designers
    print("\n\t>> Generating sample data for Designers...")
    # [Create your Designer instances here]
    # Supreme, Burberry, Calvin_Klein, etc.
    designers = [Supreme, Burberry, Calvin_Klein, Aime_Leon_Dore, Tom_Ford, Louis_Vuitton, Balmain, Dior, Fendi, Dolce_and_Gabbana]
    db.session.add_all(designers)
    db.session.commit()
    print("\t>> Sample data for Designers generated!")

    # Create and add new Clothes
    print("\n\t>> Generating sample data for Clothes...")
    # [Create your Clothes instances here]
    # Dolce_and_Gabbana_Sweater, Dolce_and_Gabbana_Kimono, etc.
    clothes = [Dolce_and_Gabbana_Sweater, Dolce_and_Gabbana_Kimono, Dior_Vneck_Top, Dior_Sleeveless_Sweater, Fendi_Handbag, Fendi_Clutch, LV_Jacket, LV_Down_Puffer_Jacket, Balmain_Snakeskin_Jacket, Balmain_Varsity_Jacket, Tom_Ford_Sunglasses, Tom_Ford_Suits, ALD_Suits, ALD_Winter_Jacket, CK_Jeans, CK_Underwear, Supreme_Denim_Jacket, Supreme_Tracksuit, Burberry_Sunglasses, Burberry_Trenchcoat]
    db.session.add_all(clothes)
    db.session.commit()
    print("\t>> Sample data for Clothes generated!")

    # Generate and add associations
    print("\n\t>> Generating Associations between Clothes and Designers...")
    associations = create_association_relationships(clothes, designers)
    db.session.add_all(associations)
    db.session.commit()
    print("\t>> Associations between Clothes and Designers generated!")

    print("\n\t>> Seeding Complete!")

        


