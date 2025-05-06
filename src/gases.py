import sys
import json
from pyspark.sql import SparkSession

#region exclude
import Data
data = Data.resolve(Data.FileData, "/mnt/c/temp/Synapse/atoms.json")
#endregion

spark = SparkSession.builder.getOrCreate()
records = json.loads(data)

# Create DataFrame from list of dicts
df = spark.createDataFrame(records)

# Filter for gaseous atoms
gases_df = df.filter(df["state"] == "gas")
gases_df.show()
