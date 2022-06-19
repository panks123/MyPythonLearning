import pymongo



if __name__ == "__main__":

    client= pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Show all the Databases
    dbs = client.list_database_names() # returns list of all the databases
    print(dbs)

    # Show all collections

    db = client['panksKart']
    collections= db.list_collection_names()
    print(collections)