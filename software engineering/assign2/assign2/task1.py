from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("pickle").config("spark.some.config.option", "some-value").getOrCreate()
df = spark.read.json("data-300k.json")
uuid_list = df.select("uuid").dropDuplicates().collect()
uuid_list.toPandas()
uuid_list = [  "51c19403-bb02-3815-9efc-af3557a1b27b",
               "35a7aa0b-0656-309a-b782-6d421d947c3b", 
               "09d33e9d-fc3b-3d1e-815f-2b321e072280",
               "635b9c44-421a-3754-b2fe-23dce522e576",
               "dac6d006-c6e6-32ac-a08e-47fafc8b176c",
               "7e1357a7-1393-3f4e-a3ec-2a2870a579f4",
               "ee0fa0f9-ef15-3372-a75b-6bbcd3f3f9f3",
               "b3ffaecb-703c-341b-92ad-bf441a800d95"]
pickle_list = [0] * 8

for i in range(8):
    pickle_list[i] = df.where(df.uuid == uuid_list[i])

for i in range(len(pickle_list)):
    pickle_list[i] = pickle_list[i].toPandas()
    pd.DataFrame.to_pickle(pickle_list[i], "./data/" +uuid_list[i] + ".pickle" )



