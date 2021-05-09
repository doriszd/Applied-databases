import pymongo

myclient = None

# connecting to mongo deamon
def connect():  
    # global variable created at beginning of script
    global myclient   
    # defining pymongo as myclient
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')
    

# function for option 6 in the menu
def find(Address):
    # checking if are we already connected, if not it will automatically connect
    if (not myclient): #check are we already connected
        connect() 
    # database name proj20DB
    mydb = myclient["proj20DB"]  
    # collection name docs
    docs = mydb["docs"]   
    # writing mongo query:
    query = [{"$match":{"details.address":{"$eq": Address}}}, {"$project": {"details.name":1, "details.age":1, "qualifications":{"$ifNull":["$qualifications", " "]}}}]
    result = docs.aggregate(query)   #mongo query executed
    return result  #results returned

# function for option 7 in the menu
def insert(ID, Name, Level):
    # checking if are we already connected, if not it will automatically connect
    if (not myclient): 
             connect() 
    # database name proj20DB
    mydb = myclient["proj20DB"] 
    # collection name docs
    docs = mydb["docs"]   
    query = {"_id" : ID, "name" : Name, "level" : Level}  
    try:
        #if correct data is entered, it will be inserted to docs collection
        docs.insert_one(query) 
    # duplicate key error in a case the same id is entered
    except pymongo.errors.DuplicateKeyError as e: 
        print("*** ERROR ***: _id DATA already exists") 
    # other errors
    except Exception as e: 
        print("Error:", e)
        
# main function
def main():
    # checking if are we already connected, if not it will automatically connect
    if (not myclient): 
        try:
            connect() 
        except Exception as e:
             # error will be printed if connection is a problem
            print("Problem connecting to database", e)

# main function called
if __name__ == "__main__":
    main()    