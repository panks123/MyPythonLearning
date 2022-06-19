import pymongo

if __name__ == "__main__":

    client= pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Create a new dtabase
    db= client['pymongotutsDB'] # # It will switch to 'pymongotutsDB' database if already present or else it will create new and it will use that

    # Create a collection  -- We have to necessarily create a collection after creating a DB  
    collection = db['products'] # It will switch to 'products' collection if already present or else it will create new and it will use that

    # The database will still not be reflected in side mongoDB until we insert a document into the collection
    # Inser a single document into the collection
    # dictionary = {'name': 'Pen', 'price': 5}
    # collection.insert_one(dictionary)

    # dictionary1 = {'name': 'Notebook', 'price': 15}
    # collection.insert_one(dictionary1)

    # Insert multiple documents
    listOfProductsDicts = [
        {'name': "Monitor", 'price': 350, "available": True},  # in mongoDB schema is flexible
        {'name': "Mouse", 'price': 50},
        {'name': "Keyboard", 'price': 150},
        {'name': "Speaker", 'price': 450}
    ]
    collection.insert_many(listOfProductsDicts)