import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url="mongodb://demop-cosmosdb:tmSXPe5dUZUsh7anjO4xIHQiQC5CyRD2DUIR1RFNhbLbijoDc6TVRfD7e8SY8HxJttGpiUto0rVCuGefpme86g==@demop-cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@demop-cosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['demop-cosmosdb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

