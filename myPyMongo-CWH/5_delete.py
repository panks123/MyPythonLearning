import pymongo

if __name__ == "__main__":

    client= pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Create a new dtabase
    db= client['pymongotutsDB']

    collection = db['products']

    # Deleting single document
    # record = {"name": "Keyboard"}
    # collection.delete_one(record)  # deletes the first matching record with name: Keyboard

    # Deleting multiple documents
    record = {"name": "Mouse"}
    up =collection.delete_many(record)
    print(up.deleted_count) # It will return the no. of deleted documents

    docs= collection.find()

    for item in docs:
        print(item)

