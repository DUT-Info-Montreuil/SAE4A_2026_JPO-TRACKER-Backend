
class Service:
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client.flask_database
