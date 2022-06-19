import pymongo

if __name__ == "__main__":

    client= pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Create a new dtabase
    db= client['pymongotutsDB']

    collection = db['products']

    one = collection.find_one() # It will fetch the first document from the collection
    print(one)

    one = collection.find_one({"name": "Keyboard"}) # It will fetch the first document from the collection with name = "Keyboard"
    print(one)

    print("--------------------------------")

    allDocs = collection.find() # It will return an iterable (A cursur object)
    print(allDocs)

    for item in allDocs:
        print(item)

    print("--------------------------------")

    allDocs = collection.find().limit(3) # limit(3) limits the no. of documents to 3 only in the output
    print(allDocs)

    for item in allDocs:
        print(item)
    print("--------------------------------")
    allDocs = collection.find({"name": "Speaker"}, {"name": 1,"price": 1,  "_id": 0})  

    for item in allDocs:
        print(item)

