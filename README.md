### -------------------------------------------- AWS_Data_Engineer ------------------------------------------

#### Chapter 1 : 
#### ------------------------------------------------------- Visual ETL with AWS Glue Studio ------------------------------------------------------------- :

 We want to make an ETL like : Source : S3 Bucket  --------> Transform --------> Target : S3 Bucket <br>
**AWS Glue Studio** It's a simple visual interface in AWS Glue Studio to create your ETL/ELT jobs. For that, the first thing we are going to do, is creating a job :<br>
1. **Connect to the console**.<br>
2. **Choose ETL jobs from the navigation pane**.<br>
3. **Select an option create a job from a sample job**: <br>
   - 3.1. Visual ETL job to join multiple sources – Read three CSV files, combine the data, change the data types, then write the data to Amazon S3 <br> and catalog <br> it for querying later.<br>
   - 3.2. Spark notebook using Pandas – Explore and visualize data using the popular Pandas framework combined with Spark.<br>
   - 3.3. Spark notebook using SQL – Use SQL to get started quickly with Apache Spark. Access data through the AWS Glue Data Catalog and transform it<br> using familiar <br> commands.<br>
4. **Choose Create sample job**.<br>
Once we is there, an interface to Build an ETL job.<br>
Let's start to build a sample ETL/ELT whose data source from is S3 Bucket, need to transform before load into the target S3 Bucket.<br>
   - 4.1. To add a node source : let's click on the one in the list of source(AWS Glue Data Catalog, AWS S3, Amazon Kinesis, Apache Kafka, Relational DB,Amazon Redshift,<br> MySQL, PostgreSQL, Oracle SQL, Microsoft SQL Server, Amazon DynamoDB, Snowflake, Google BigQuery, Teradata Vantage, Vertica, Azure SQL, SAP HANA, Azure Cosmos, Mongo DB<br> and Salesforce). After adding the node, we need to setting it. For that :<br>
      + 4.2.1. Click on the selected node to show the including informations about the setting node.<br>
      + 4.2.2. Click on Browser S3 to establish the connection between node source and the chosen file from S3 Bucket.<br>
      + 4.2.3. Choose the data format of the file,then delimiter and Quote character <br>
      + 4.2.4. Setting IAM role. For that Getting started : <br>
     > Come back on the starting page of Glue. Let's find Set up IAM(roles and users) <br>
     > Set up IAM permissions <br>
     > Choose the IAM identities (roles or users) that you want to give AWS Glue permissions to. AWS Glue attaches <br> the AWSGlueConsoleFullAccess managed policy to these
       identities. You can skip this step if you want to set these permissions manually or only want to set a default service role.<br>
     > Choose Next.<br>
     > Choose the level of Amazon S3 access that your roles and users need. The options that you choose in this step are applied to all of the identities that you selected.<br>
     > Under Choose S3 locations, choose the Amazon S3 locations that you want to grant access to.<br>
     > Next, select whether your identities should have Read only (recommended) or Read and write access to the locations that you <br> previously selected. AWS Glue adds
       permissions policies to your identities based on the combination of locations and read or write permissions you select.<br>
     > Choose Next.<br>
     > Choose a default AWS Glue service role for your account. A service role is an IAM role that AWS Glue uses to access resources in other AWS services on your behalf.<br> For more 
     information, see Service roles for AWS Glue.<br>
     >> When you choose the standard AWS Glue service role, AWS Glue creates a new IAM role in your AWS account named<br> AWSGlueServiceRole with the following managed policies 
        attached. If your account already has an IAM role named AWSGlueServiceRole, AWS Glue attaches these policies to the existing role.<br>
     >>> AWSGlueServiceRole<br>
     >>> AmazonS3FullAccess<br>
     >>
     >> When you choose an existing IAM role, AWS Glue sets the role as the default, but doesn't add any permissions to it. Ensure that you've configured the role to use as a 
        service role for AWS Glue.<br> For more information, see<br>
     >>> Step 1: Create an IAM policy for the AWS Glue service and<br>
     >>> Step 2: Create an IAM role for AWS Glue.<br>
     >
     > Choose Next.<br>
     > Finally, review the permissions you've selected and then choose Apply changes. When you apply the changes, AWS Glue<br> adds IAM permissions to the identities that you 
       selected. You can view or modify the new permissions in the IAM console at https://console.aws.amazon.com/iam/<br>
       ![Capture d’écran 2024-07-22 183045](https://github.com/user-attachments/assets/cf93f76d-09b9-458e-b03e-4d15c2c317b6)
     > Refresh the page, to get the printed data preview<br>
- 4.3. **Transform Data** : we're going to do the same like the choice of source node. In this case, we want to do drop the feature "administration" and then change the data<br> type 
     of some features into float. Here is the list of Transforms, we can use it : <br>
     **Data Preparation Recipe, Change Schema, Join, SQL Query, Detect Sensitive Data, Evaluate Data Quality, Fill Missing Values, Aggregate, Custom Transform, Drop Duplicates,<br> 
       Drop Fields, Drop Null Fields, Filter, Rename Field, Conditional Router, Select Fields, Select From Collection, Spigot, Split Dataset By Fields, Union, Array To Columns, <br>
       Concatenate Columns, Derived Column, Explode Array Or Map Into Rows,<br> Extract JSON Path, Lookup, etc**.). We will choose "**Change Schema**"<br>
- 4.4. **Target Data** : The choice of node is the same like other. In this case, we want to save the transformed data into S3 Bucket. and the settings this node.<br>
- 4.5. **Save and then running the job**.<br>

- 4.6. **To monitoring the job running** : <br>
      > Choose Job run monitoring on the left pane.<br>
      > Check the new file into S3 Bucket, after it succeeded.<br>

---------------------------------------------------------------------------

