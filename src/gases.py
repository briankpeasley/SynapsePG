import sys
import json
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print(data)
records = json.loads(data)

# Create DataFrame from list of dicts
df = spark.createDataFrame(records)

# Filter for gaseous atoms
gases_df = df.filter(df["state"] == "gas")
gases_df.show()
