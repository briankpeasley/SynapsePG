from pyspark.sql.functions import avg
import Data

#region exclude
from pyspark.sql import SparkSession
import Data
spark = SparkSession.builder.getOrCreate()
data = Data.transcripts("/mnt/c/temp/transcripts/raw/")
#endregion

df_counts = data.groupBy("execution_id", "t").count()
df_avg_t = df_counts.groupBy("t").agg(avg("count").alias("avg_count_per_execution"))

df_counts.show()
df_avg_t.show()
