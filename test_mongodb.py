from pymongo import MongoClient
uri = "mongodb+srv://sarthyaprakash2007_db_user:Admin123@cluster0.rfw0ywf.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)