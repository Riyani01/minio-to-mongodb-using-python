from http import client
from minio import Minio
import pandas as pd
import pymongo
client = Minio('127.0.0.1:9000',
            access_key='minioadmin',
            secret_key='minioadmin',
            secure=False)
            
obj = client.get_object("bucket-kelompok","GoFood_dataset_clean.csv")
data = pd.DataFrame(pd.read_csv(obj))
print(data)

clientMongo = pymongo.MongoClient("mongodb://localhost:27017")
db = clientMongo["dbKelompok"]
col = db["colKelompok"]

data = data.to_dict(orient="records")
col.insert_many(data)

if col.inserted_ids is not None:
   print("Object berhasil disimpan di mongoDB")
else:
        ("Object gagal disimpan di mongoDB")