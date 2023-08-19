import pymongo
myclient=pymongo.MongoClient("mongodb+srv://parvesh:root@cluster0.jkamguo.mongodb.net/?retryWrites=true&w=majority")
mydb=myclient["mydatabase"]
mycol=mydb["customers"]
mydict={ "name": "parvesh", "address": "Highway 37" }
x=mycol.insert_one(mydict)
print("data inserted")
 
