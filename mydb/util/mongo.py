import pymongo
from pymongo.errors import PyMongoError
from bson import ObjectId
class Mongo:
    def __init__(self, dbName, colName):  #created name and collection dynamically
        client= pymongo.MongoClient('mongodb://localhost:27017') #establish connection
        db=client[dbName] #database (like a folder)
        self.col=db[colName] #collection in database (one collection inside folder)

    def insert(self, data):
        try:
            myResponse= self.col.insert_one(data)
            data['_id']= myResponse.inserted_id
            return data
        except PyMongoError as error:
            return str(error)
        except:
            print("Invalid")
        

        # let't read
    def fetchAll(self,query={}, qty=0):
        try:
            data=[]
            res= self.col.find(query).limit(qty) #limit is necessary for stopping the load
            for item in res:
                data.append(item)
            return data
        except PyMongoError as error:
            return str(error)
        except:
            return "Invalid"
        
        # fetch single
    def fetch(self,query):
        try:
            res= self.col.find_one(query)
            return res
        except PyMongoError as error:
            return str(error)
        except:
            return "Invalid"
        
        # fetch by id
    def fetchById(self,id):
        try:
            res= self.col.find_one({'_id':ObjectId(id)})
            return res 
        except:
            return "error"
        
        # Update
    def update(self, id, data):
        try:
            self.col.update_one({'_id':ObjectId(id)},{'$set': data} )
            data=self.fetchById(id)
            return data
        except PyMongoError as error:
            return str(error)
        except:
            return "Couldn't update"
        

    def delete(self, id):
        try:
            res= self.col.delete_one({'_id':ObjectId(id)})
            return res
        except PyMongoError as error:
            return str(error)
        except:
            return "Couldn't update"