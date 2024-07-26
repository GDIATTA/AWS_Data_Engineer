### ------------------------------------ AWS_Data_Engineer -----------------------------------

#### Chapter 1 : -------------------------------- Visual ETL with AWS Glue Studio --------------------------------------------- :
 

 Make an ETL like : Source : **S3 Bucket  --------> Transform --------> Target : S3 Bucket** <br>
 
**AWS Glue Studio**, It's a simple visual interface in AWS Glue Studio to create your ETL/ELT jobs. For that, the first thing you're going to do, is creating a job :<br>
 1. **Connect to the console**.<br>
 2. **Choose ETL jobs from the navigation pane**.<br>
 3. **Select an option create a job from a sample job**: <br>
   - 3.1. Visual ETL job to join multiple sources – Read three CSV files, combine the data, change the data types, then write the data to Amazon S3 <br> and catalog <br> it for querying later.<br>
   - 3.2. Spark notebook using Pandas – Explore and visualize data using the popular Pandas framework combined with Spark.<br>
   - 3.3. Spark notebook using SQL – Use SQL to get started quickly with Apache Spark. Access data through the AWS Glue Data Catalog and transform it<br> using familiar <br> commands.<br>
4. **Choose Create sample job**.<br>
Once you are there, an interface to Build an ETL job.<br>
Let's start to build a sample ETL/ELT whose data source from is S3 Bucket, need to transform before load into the target S3 Bucket.<br>
   - 4.1. To add a node source : let's click on the one in the list of source(AWS Glue Data Catalog, AWS S3, Amazon Kinesis, Apache Kafka, Relational DB,Amazon Redshift,<br> MySQL, PostgreSQL, Oracle SQL, Microsoft SQL Server, Amazon DynamoDB, Snowflake, Google BigQuery, Teradata Vantage, Vertica, Azure SQL, SAP HANA, Azure Cosmos, Mongo DB<br> and Salesforce). After adding the node, you need to setting it. For that :<br>
      + 4.2.1. Click on the selected node to show the including informations about the setting node.<br>
      ![Capture d’écran 2024-07-22 181227](https://github.com/user-attachments/assets/b54e2782-b4d9-4a9e-aec7-50e999982405)
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
     > Choose a default AWS Glue service role for your account. A service role is an IAM role that AWS Glue uses to access resources in other AWS services on your behalf.<br> For 
       more information, see Service roles for AWS Glue.<br>
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
     ![Capture d’écran 2024-07-22 191628](https://github.com/user-attachments/assets/0072d613-f7bb-44a7-8678-ce7a6c65a6cc)
- 4.3. **Transform Data** : we're going to do the same like the choice of source node. In this case, we want to do drop the feature "administration" and then change the data type 
     of some features into float. Here is the list of Transforms, we can use it : <br>
     **Data Preparation Recipe, Change Schema, Join, SQL Query, Detect Sensitive Data, Evaluate Data Quality, Fill Missing Values, Aggregate, Custom Transform, Drop Duplicates 
       Drop Fields, Drop Null Fields, Filter, Rename Field, Conditional Router, Select Fields, Select From Collection, Spigot, Split Dataset By Fields, Union, Array To Columns,
       Concatenate Columns, Derived Column, Explode Array Or Map Into Rows, Extract JSON Path, Lookup, etc**.). We will choose "**Change Schema**"<br>
       ![Capture d’écran 2024-07-22 192907](https://github.com/user-attachments/assets/a99f0e88-813f-474a-912b-645c1f834dea)
- 4.4. **Target Data** : The choice of node is the same like other. In this case, we want to save the transformed data into S3 Bucket. and the settings this node.<br>
![Capture d’écran 2024-07-22 194010](https://github.com/user-attachments/assets/3405717d-90ba-4fc1-adfb-86eb81eaaaeb)
- 4.5. **Save and then running the job**.<br>

- 4.6. **To monitoring the job running** : <br>
  > Choose Job run monitoring on the left pane.<br>
  > Check the new file into S3 Bucket, after it succeeded.<br>

---------------------------------------------------------------------------

 Create a **Data Catalog** where the source data is from S3 bucket<br>

The **AWS Glue Data Catalog** is your persistent technical metadata store. It is a managed service that you can use to store, annotate, and share metadata in the AWS Cloud.<br>
In this tutorial, we will do the following using the AWS Glue console:<br>
> 1. **Create a database**<br>
> 2. **Create a table**<br>
> 3. **Use an Amazon S3 bucket as a data source**<br>

**Step 1: Create a database**<br>

To get started, sign in to the AWS Management Console and open the AWS Glue console.<br>
To create a database using the AWS Glue console:<br>
> 1. In the AWS Glue console, choose Databases under Data catalog from the left-hand menu.<br>
> 2. Choose Add database.<br>
![Capture d’écran 2024-07-24 010721](https://github.com/user-attachments/assets/5ec883e8-7208-462d-a46c-a2661c7612eb)
> 3. In the Create a database page, enter a name for the database. In the Location - optional section, set the URI location for use by clients of the Data Catalog. If you don't know this, you can continue with creating the database.<br>
> 4. (Optional). Enter a description for the database.<br>
> 5. Choose Create database.<br>
Your new database will appear in the list of available databases. You can edit the database by choosing the database's name from the Databases dashboard.<br>
![Capture d’écran 2024-07-24 010823](https://github.com/user-attachments/assets/8f53e41e-86fc-4f34-aa57-033f7e32219b)

**Step 2. Create a table**<br>

In this step, you create a table using the AWS Glue console.<br>
> 1. In the AWS Glue console, choose Tables in the left-hand menu.<br>
> 2. Choose Add table.<br>
> 3. Add crawler table<br>
> 4. Set your crawler properties by entering a name for your crawler and then choose next.<br>
> 5. Choose data sources and classifiers by choose a data source configuration, then add a data source and check the Customer classifiers which is optional. Choose next step.<br>
> 6. Configure security settings by choose or create an IAM role, then leave the other options as default and click next.<br>
> 7. Set output and scheduling by :<br>
>> 7.1 Output configuration. For that :<br>
>>> a. Choose Target database which is the database created right now.<br>
>>> b. And then leave the other options as default.<br>
>>
>> 7.2 Crawler Schedule, by choose the frequency from options as On demand, Hourly, Daily, Weekly, Monthly and Custom<br>

> 8. Review and create<br>
![Capture d’écran 2024-07-24 010823](https://github.com/user-attachments/assets/8f53e41e-86fc-4f34-aa57-033f7e32219b)
> 9. Run crawler<br>
![Capture d’écran 2024-07-24 013830](https://github.com/user-attachments/assets/2734ed62-e992-41fd-9985-23c6ff735f5a)
Your newly created table will appear in the Tables dashboard. From the dashboard, you can modify and manage all your tables.<br>

-----------------------------------------------------------------------------------------------------------------------------------------------

Create a **Data Catalog** using **Glue ETL**, with the data source being an **S3 bucket**.<br>

The ETL process should be as follows:<br>

**Source (S3 Bucket) ----------> Transform ----------> Target (Data Catalog)**.<br>

The processing steps are the same as in the previous ETL process, with the only change being the **target**. The target in this case is a **Data Catalog**, meaning the data will be stored in a **table** within a **database**. There is no need to repeat the steps for creating the **source node and its settings**, or the **transformation node and its settings**. The only thing, you want to focus on, is the **target**.<br>

How to Create and Configure a **Data Catalog Node**:<br>
The procedure for creating and configuring the **Data Catalog node** is the same as in the previous example. Please refer to the previous Data Catalog instructions for detailed steps.<br>

Here are the expected results.<br>

![Capture d’écran 2024-07-25 021941](https://github.com/user-attachments/assets/a4257cdb-70e5-4172-b519-ef8936eead72)

------------------------------------------------------------------------------------------------------------------------------------------------

### --------------------------------------------------       AWS Athéna      -------------------------------------------------------:

 #### ---------------------------------------------         **What is Amazon Athena ?**      --------------------------------------------------<br>
 
**Amazon Athena** is an interactive query service that makes it easy to **analyze data directly in Amazon Simple Storage Service (Amazon S3)** using standard **SQL**. With a few actions in the **AWS Management Console**, you can point **Athena** at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.<br>

**Amazon Athena** also makes it easy to interactively run data analytics using **Apache Spark without having to plan for, configure, or manage resources**. When you run **Apache Spark applications on Athena**, you submit Spark code for processing and receive the results directly. Use the simplified notebook experience in Amazon Athena console to develop **Apache Spark applications using Python or Athena notebook APIs**.<br>

**Athena SQL and Apache Spark on Amazon Athena are serverless**, so there is no infrastructure to set up or manage, and **you pay only for the queries you run**. Athena scales automatically—running queries in parallel—so results are **fast**, even with **large datasets** and **complex queries**.<br>

#### --------------------------------------------     **When should you use Athena ?**     -----------------------------------------------------<br>

**Athena** helps you **analyze unstructured, semi-structured, and structured** data stored in **Amazon S3**. Examples include **CSV, JSON, or columnar data formats** such as **Apache Parquet and Apache ORC**. You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena.<br>

**Athena** integrates with **Amazon QuickSight** for easy data visualization. You can use Athena to generate reports or to explore data with business intelligence tools or **SQL clients connected with a JDBC or an ODBC driver**.<br>

**Athena** integrates with the **AWS Glue Data Catalog**, which offers a persistent metadata store for your data in **Amazon S3**. This allows you to create **tables** and **query data** in Athena based on a central metadata store available throughout your Amazon Web Services account and integrated with the ETL and data discovery features of AWS Glue.<br>

**Amazon Athena** makes it easy to **run interactive queries** against data directly in **Amazon S3** without having to **format data or manage infrastructure**. For example, Athena is useful if you want to run a quick query on web logs to troubleshoot a performance issue on your site. With Athena, you can get started fast: you just define a table for your data and start querying using standard SQL.<br>

You should use Amazon Athena if you want to **run interactive ad hoc SQL queries** against data on **Amazon S3**, without having to **manage any infrastructure or clusters**. Amazon Athena provides the easiest way to run ad hoc queries for data in Amazon S3 without the need to setup or manage any servers.<br>


#### ----------------------------------------     **Client and programming tools for using Athena**     -------------------------------------------:<br>

You can access **Athena** using a variety of client and programming tools. These tools include the **AWS Management Console, a JDBC or ODBC connection, the Athena API, the Athena CLI, the AWS SDK, or AWS Tools for Windows PowerShell**.<br>


**Getting started using AWS Management Console**<br>

This tutorial walks you through using **Amazon Athena** to query data. You'll create a **table** based on sample data stored in **Amazon Simple Storage** Service, query the table, and check the results of the query.<br>
In the previous chapter, we explored the **Data Catalog**. In this tutorial, we will use it.<br>
Let's recap what we accomplished with the **Data Catalog**: we first created a **database** and then created a **table** with data sourced from an **S3 bucket**. Now, we will continue using these in the **Athena platform**.<br>

Once the **Data Catalog** is created, follow these steps to open **Athena**:<br>
> Search for **Athena** in the service search box.<br>
> Click on **Explore data** on the **Athena** page.<br>
> In the left pane, find **Data Source** and select **AwsDataCatalog**.<br>
> In the left pane, find **Database** and select your database (e.g., **database1**). Refresh to see all the **tables** included in your database.<br>
You should now see the following page.<br>

At the top of this page, you will see a **prompt to configure a location to store the query results in an Amazon S3 bucket before running your first query**.



