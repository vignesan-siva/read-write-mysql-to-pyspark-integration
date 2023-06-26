# initialize findspark in jupiter notbook
import findspark
findspark.init()

#start spark Session
from pyspark.sql import SparkSession
spark=SparkSession.\
      builder.\
      appName("mysql to pyspark connection").\
      config("spark.jars","C:\\Program Files(x86)\\Java\\jar_files\\mysql-connector-java-8.0.13.jar").\
      getOrCreate()

# display dataframe using show comment
df.show()

# here you write your transformation logic based on customer need
from pyspark.sql.functions import*
df2=df.withColumn("pro",col('product_id')+1)

# write your transformed data into destionation place like postgresql,sql,....anyone database or datawarehouse

df3.write.format('jdbc').\
    option('url',"jdbc:mysql://localhost:3306/practice").\
        option('driver','com.mysql.jdbc.Driver').\
            option('dbtable','result').\
                option('user','root').\
                    option('password','root').\
                        mode('overwrite').save()