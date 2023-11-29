Get All Clothes:
curl http://localhost:5000/clothes

Get Clothes by ID:
curl http://localhost:5000/clothes/{clothes_id}
Replace {clothes_id} with the actual ID.
Add New Clothes:

curl -X POST http://localhost:5000/clothes -H "Content-Type: application/json" -d '{"designer_name": "Designer Name", "description": "Description", "price": 100, "image_url": "http://example.com/image.jpg"}'

Update Clothes by ID:
curl -X PATCH http://localhost:5000/clothes/{clothes_id} -H "Content-Type: application/json" -d '{"key": "value"}'
Replace {clothes_id} with the actual ID and {"key": "value"} with the actual fields you want to update.

Delete Clothes by ID:
curl -X DELETE http://localhost:5000/clothes/{clothes_id}
Replace {clothes_id} with the actual ID.

Get All Designers:
curl http://localhost:5000/designers

Get Designers by ID:
curl http://localhost:5000/designers/{designers_id}
Replace {designers_id} with the actual ID.

Add New Designers:
curl -X POST http://localhost:5000/designers -H "Content-Type: application/json" -d '{"name_of_designer": "Designer Name", "store_location": "Location"}'

Update Designers by ID:
curl -X PATCH http://localhost:5000/designers/{designers_id} -H "Content-Type: application/json" -d '{"key": "value"}'
Replace {designers_id} with the actual ID and {"key": "value"} with the actual fields you want to update.

Delete Designers by ID:
curl -X DELETE http://localhost:5000/designers/{designers_id}
Replace {designers_id} with the actual ID.

Get All Clothes Associated with a Designer:
curl http://localhost:5000/designers/{designers_id}/clothes
Replace {designers_id} with the actual ID.

Get All Designers Associated with Clothes:
curl http://localhost:5000/clothes/{clothes_id}/designers
Replace {clothes_id} with the actual ID.

Remember to replace http://localhost:5000 with the actual URL of your Flask application if it's hosted elsewhere. Also, adjust the JSON data in POST and PATCH requests according to your application's requirements.