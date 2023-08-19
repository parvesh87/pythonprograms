import pymongo
myClient=pymongo.MongoClient("mongodb://localhost:27017")
db=myClient["LoginDatabase"]
col=db["studentDetails"]

def signup(username,userid,password,confirmPassword):
    result=col.find()
    for person in result:
        if(person["username"]==username and person["userid")==userid):
            print("person already in the database")
            return
        if(password==confirmPassword):
        data={"username":"username","userid":"userid","password":"password"}
        x=col.insert_one(data)

        print(x.inserted_id,"successfully account created")
   else:
       print("incorrect password")

def login(userid,password):
    result=col.find()
    for person in result:
        if(person["userid"]==userid and person["password"]==password):
            person=person["_id"]
            print("login successfully",personId)
            return personId
        print("incorrect userid or password")

            
