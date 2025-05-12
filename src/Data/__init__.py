from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, input_file_name

def transcripts(directory):
    spark = SparkSession.builder.getOrCreate()
    df_raw = spark.read.json(directory)
    df_with_exec = df_raw.withColumn("file_path", input_file_name())
    df_with_exec = df_with_exec.withColumn("execution_id", regexp_extract(col("file_path"), "(transcript[0-9]+)\\.json", 1))
    return df_with_exec.select("execution_id", "t", "p", "ts", "seq", "id")