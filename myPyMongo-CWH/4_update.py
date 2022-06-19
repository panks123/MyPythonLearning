import pymongo

if __name__ == "__main__":

    client= pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Create a new dtabase
    db= client['pymongotutsDB']

    collection = db['products']

    # Updating single document
    find_obj= {"name": "Speaker"}
    update_obj = {'$set': {"price": "399"}}
    collection.update_one(find_obj, update_obj) # It will update the first match's price to 399

    docs= collection.find()

    for item in docs:
        print(item)

    print("---------------------------------")

    # Updating multiple document
    find_obj= {"name": "Monitor"}
    update_obj ={'$set': {"available": False}}
    collection.update_many(find_obj, update_obj)  # It all update all the matches with 'available' = False

    docs= collection.find()
    
    for item in docs:
        print(item)