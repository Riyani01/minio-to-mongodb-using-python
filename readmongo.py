from http import client
from sqlite3 import Cursor
from minio import Minio
import pandas as pd
import pymongo
#terhubung keserver mongodb
clientMongo = pymongo.MongoClient("mongodb://localhost:27017")
db = clientMongo["dbKelompok"]
col = db["colKelompok"]
#mengambil data dari collection
cursor = col.find()
#mengkonversi kedalam dataframe
df = pd.DataFrame(list(cursor))
#menampilkan dataframe
print(df)