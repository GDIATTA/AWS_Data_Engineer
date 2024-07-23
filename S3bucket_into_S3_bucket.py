import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1721668076348 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://myfirstbucket512/50_Startups.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1721668076348")

# Script generated for node Change Schema
ChangeSchema_node1721669262632 = ApplyMapping.apply(frame=AmazonS3_node1721668076348, mappings=[("rd_spend", "string", "rd_spend", "float"), ("marketing_spend", "string", "marketing_spend", "float"), ("state", "string", "state", "string"), ("profit", "string", "profit", "float")], transformation_ctx="ChangeSchema_node1721669262632")

# Script generated for node Amazon S3
AmazonS3_node1721669820683 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1721669262632, connection_type="s3", format="csv", connection_options={"path": "s3://myfirstbucket512/", "compression": "snappy", "partitionKeys": []}, transformation_ctx="AmazonS3_node1721669820683")

job.commit()