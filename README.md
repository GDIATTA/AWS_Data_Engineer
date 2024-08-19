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

### Chapter 2 : ----------------- Create a Data Catalog -------------------

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

#### Chapter3: -----------------------------------------------       AWS Athéna      -------------------------------------------------------:

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
![Capture d’écran 2024-07-24 014407](https://github.com/user-attachments/assets/d58a18f7-a3ad-4cab-a202-063d399ad524)

At the top of this page, you will see a **prompt to configure a location to store the query results in an Amazon S3 bucket before running your first query**.<br>
Once this is set up, you should see the following page.

![Capture d’écran 2024-07-25 021546](https://github.com/user-attachments/assets/3dfc963e-3df8-42f3-8444-d890a45b7a02)

Now you can write your first query. In this tutorial, we will execute a simple query that retrieves all records from the table. Here is the expected result.

![Capture d’écran 2024-07-25 021634](https://github.com/user-attachments/assets/f4df1ce4-df63-4b3b-9efa-7062790ee796)

-------------------------------------------------------------------------------------------------------------------------------------------------

#### Chapter4: --------------------------------------------  Amazon Redshift Serverless  ---------------------------------------------------:

The basic flow of **Amazon Redshift Serverless** is to create serverless resources, connect to **Amazon Redshift Serverless**, load sample data, and then run queries on the data.<br>

#### Creating a data warehouse with Amazon Redshift Serverless <br>
The first time you log in to the **Amazon Redshift Serverless** console, you are prompted to access the getting started experience, which you can use to create and manage serverless resources. In this tutorail, you'll create serverless resources using **Amazon Redshift Serverless**'s default settings. <br>

**Pre-requirements :** <br>
> **Redshift Serverless** requires an **Amazon VPC with three subnets in three different availability zones**. **Redshift Serverless** also requires at **least 37 available IP addresses**. Make sure that the **Amazon VPC** that you use for **Redshift Serverless has three subnets in three different availability zones, and at least 37 available IP addresses**, before continuing. <br>

**To configure with default settings:** <br>

- 1. Sign in to the **AWS Management Console** and open the **Amazon Redshift console at https://console.aws.amazon.com/redshiftv2/** <br>
- 2. Choose Try **Redshift Serverless Free Trial**.
Under Configuration, choose **Use default settings**. **Amazon Redshift Serverless** creates a **default namespace with a default workgroup** associated with this **namespace**. Choose **Save configuration**. <br>
![Capture d’écran 2024-07-26 152753](https://github.com/user-attachments/assets/66f620c2-b43d-43dc-83aa-ee8a0918a2ef)
![Capture d’écran 2024-07-26 152858](https://github.com/user-attachments/assets/6afbccb1-ac5a-43e0-93bb-20ccb1eb66fe)

**Note**: <br>
> A **Namespace** is a **collection of database objects and users**. **Namespaces group** together all of the resources you use in **Redshift Serverless**, such as **schemas, tables, users, datashares, and snapshots**. <br>
> A **Workgroup** is a **collection of compute resources**. **Workgroups house** compute resources that **Redshift Serverless** uses to run computational tasks. <br>

- 3. After setup completes, choose **Continue** to go to your Serverless dashboard. You can see that the serverless **workgroup** and **namespace** are available. <br>
![Capture d’écran 2024-07-26 153206](https://github.com/user-attachments/assets/6a24bdc0-0d60-4f3b-bb50-ff6459076739)

#### Loading sample data <br>
Now that you've set up your **data warehouse** with **Amazon Redshift Serverless**, you can use the **Amazon Redshift query editor v2 to load sample data**.<br>
![Capture d’écran 2024-07-26 153549](https://github.com/user-attachments/assets/3706426c-869d-4a35-abdd-86b783246095)

- 1. To launch **query editor v2 from the Amazon Redshift Serverless console**, choose **Query data**. When you invoke query editor v2 from the Amazon Redshift Serverless console, a new browser tab opens with the query editor. The query editor v2 connects from your client machine to the Amazon Redshift Serverless environment.<br>
- 2. For this tutorial, you'll use your **AWS administrator account and the default AWS KMS key**. <br>
- 3. To connect to a **workgroup**, choose the workgroup name in the tree-view panel. <br>
- 4. When connecting to a **new workgroup for the first time within query editor v2**, you must select the type of authentication to use to connect to the workgroup. For this tutorial, leave **Federated user** selected, and choose **Create connection**. <br>
Once you are connected, you can choose to **load sample data from Amazon Redshift Serverless or from an Amazon S3 bucket**. <br>
- 5. Under the **Amazon Redshift Serverless default workgroup**, expand the **sample_data_dev** database. There are **three sample schemas** corresponding to **three sample datasets** that you can load into the **Amazon Redshift Serverless** database. Choose the **sample dataset** that you want to load, and choose **Open sample notebooks**. <br>
![Capture d’écran 2024-07-26 154126](https://github.com/user-attachments/assets/ac8713c2-19c7-478d-b65d-5aff9f548394)
![Capture d’écran 2024-07-26 160732](https://github.com/user-attachments/assets/09c69b56-5e37-4f9a-af61-56bc38739f85)
![Capture d’écran 2024-07-26 160918](https://github.com/user-attachments/assets/0bde1b3e-da16-445a-943b-432b5346bd1e)

**Note**:
> A **SQL notebook** is a container for SQL and Markdown cells. You can use notebooks to organize, annotate, and share multiple SQL commands in a single document.<br>

- 6. When **loading data for the first time**, query editor v2 will prompt you to create a **sample database**. Choose **Create**. <br>
 
 #### Loading in data from Amazon S3 : <br>
After creating your **data warehouse**, you can load data from **Amazon S3**. <br>
At this point, you have a database named **dev**. Next, you will create some **tables** in the **database**, upload data to the tables, and try a query. For your convenience, the sample data that you load is **available** in an **Amazon S3 bucket**.<br>
- 1. Before you can load data from **Amazon S3**, **you must first create an IAM role with the necessary permissions and attach it to your serverless namespace**. To do so, choose **Namespace configuration** from the navigation menu, choose **your namespace**, and then choose **Security and encryption**. Then, choose **Manage IAM roles**. <br>
![Capture d’écran 2024-07-26 162215](https://github.com/user-attachments/assets/8c9552a1-659e-4988-9dee-dceee1641b0b)
![Capture d’écran 2024-07-26 162303](https://github.com/user-attachments/assets/2d1867f2-1925-42c3-9508-fb692c73c7da)
![Capture d’écran 2024-07-26 162449](https://github.com/user-attachments/assets/12902fae-81ab-4eb2-9f5e-5a951b5d71bf)
- 2. Expand the Manage IAM roles menu, and choose **Create IAM role**. <br>
![Capture d’écran 2024-07-26 162836](https://github.com/user-attachments/assets/175fc210-d2c9-4fdd-ad1d-13f77467550b)
- 3. Choose **the level of S3 bucket access** that you want to grant to this role, and choose **Create IAM role as default**. <br>
![Capture d’écran 2024-07-26 163120](https://github.com/user-attachments/assets/4d75a347-7e94-48e7-961a-db6df279dba8)
- 4. Choose **Save changes**. You can now load sample data from Amazon S3. <br>
![Capture d’écran 2024-07-26 163330](https://github.com/user-attachments/assets/28c93a05-ed86-40b5-94d1-c4f77bbb8945)

#### Load sample data from Amazon S3

![Capture d’écran 2024-07-26 171045](https://github.com/user-attachments/assets/3d287828-1e24-4d4f-a011-086c55027534)
![Capture d’écran 2024-07-26 171415](https://github.com/user-attachments/assets/fb7fc979-3066-4031-8697-009f4fd903da)
![Capture d’écran 2024-07-26 171450](https://github.com/user-attachments/assets/fe95c09c-7620-4f2d-9ecf-36852b7f11e5)
![Capture d’écran 2024-07-26 171807](https://github.com/user-attachments/assets/67a793ce-ca91-453c-abb1-5708d8a0880a)


#### Chapter5 : -------------------------------------------- Amazon RDS ---------------------------------------------:

##### ----------------- **What is Amazon Relational Database Service (Amazon RDS)?** ---------:
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

##### ---------------- **Why do you want to run a relational database in the AWS Cloud?** ---------------:
Because AWS takes over many of the difficult and tedious management tasks of a relational database.

Before you work, you should need to know all the following concept : <br>
**DB instances**:is an isolated database environment in the AWS Cloud. The basic building block of Amazon RDS is the DB instance. <br>
Your DB instance can contain one or more user-created databases. You can access your DB instance by using the same tools and applications that you use with a standalone database instance. You can create and modify a DB instance by using the AWS Command Line Interface (AWS CLI), the Amazon RDS API, or the AWS Management Console. <br>
**DB engines** : is the specific relational database software that runs on your DB instance. Amazon RDS currently supports the following engines: <br>
> Db2 <br>
> MariaDB <br>
> Microsoft SQL Server <br>
> MySQL <br>
> Oracle <br>
> PostgreSQL <br>

Each DB engine has its own supported features, and each version of a DB engine can include specific features. Support for Amazon RDS features varies across AWS Regions and specific versions of each DB engine. <br>

**DB instance classes**: determines the computation and memory capacity of a DB instance. A DB instance class consists of both the DB instance type and the size. Each instance type offers different compute, memory, and storage capabilities. For example, db.m6g is a general-purpose DB instance type powered by AWS Graviton2 processors. Within the db.m6g instance type, db.m6g.2xlarge is a DB instance class. <br>
You can select the DB instance that best meets your needs. If your needs change over time, you can change DB instances. <br>
**DB instance storage**: <br>
> Amazon EBS provides durable, block-level storage volumes that you can attach to a running instance. DB instance storage comes in the following types:<br>
>  General Purpose (SSD)<br>
> Provisioned IOPS (PIOPS)<br>
> Magnetic <br>

The storage types differ in performance characteristics and price. You can tailor your storage performance and cost to the needs of your database.<br>
Each DB instance has minimum and maximum storage requirements depending on the storage type and the database engine it supports. It's important to have sufficient storage so that your databases have room to grow. Also, sufficient storage makes sure that features for the DB engine have room to write content or log entries.<br>
**Amazon Virtual Private Cloud (Amazon VPC)** : <br>
You can run a DB instance on a virtual private cloud (VPC) using the Amazon Virtual Private Cloud (Amazon VPC) service. When you use a VPC, you have control over your virtual networking environment. You can choose your own IP address range, create subnets, and configure routing and access control lists. The basic functionality of Amazon RDS is the same whether it's running in a VPC or not. Amazon RDS manages backups, software patching, automatic failure detection, and recovery. There's no additional cost to run your DB instance in a VPC.<br>
**AWS Regions and Availability Zones** : <br>
Amazon cloud computing resources are housed in highly available data center facilities in different areas of the world (for example, North America, Europe, or Asia). Each data center location is called an AWS Region.<br>
Each AWS Region contains multiple distinct locations called Availability Zones, or AZs. Each Availability Zone is engineered to be isolated from failures in other Availability Zones. Each is engineered to provide inexpensive, low-latency network connectivity to other Availability Zones in the same AWS Region. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.<br>
**Security**:<br>
A security group controls the access to a DB instance. It does so by allowing access to IP address ranges or Amazon EC2 instances that you specify.
**Amazon RDS monitoring** : <br>
There are several ways that you can track the performance and health of a DB instance. You can use the Amazon CloudWatch service to monitor the performance and health of a DB instance. CloudWatch performance charts are shown in the Amazon RDS console. You can also subscribe to Amazon RDS events to be notified about changes to a DB instance, DB snapshot, or DB parameter group.<br>

Get started : <br>

------------------- **How to create an RDS Database** ------------------: <br>

For that, you will create the DB instance. To do this, you need to follow these steps :<br>
> Firstly open the Amazon RDS service console.<br>
> Click Create database to start the configuration process.<br>
> In the Choose a database creation method section, ensure the Standard Create option is selected. Next,<br>
> In the Engine options section, choose the PostgreSQL engine type and the PostgreSQL 14.10-R2 version. <br>

![Capture d’écran 2024-08-19 014718](https://github.com/user-attachments/assets/e14ac63b-0f2b-4d19-b094-d9618b4bab0d)

> In the Templates section, select Free tier.<br>

![Capture d’écran 2024-07-30 132805](https://github.com/user-attachments/assets/5cdb7ca7-a74a-4b5d-9292-e224ca2d8a1f)

> In settings, as follows : <br>
>> Give a name of BD instance, database-1<br>
>> Give a Master usename, postgres<br>
>> In Manage master credentials in AWS Secrets Manager, Choose Auto generate a password like <br>
>> In DB instance class, select Burstable classes, and choose t3.medium <br>
>> In Storage section, select polyvalent SSD(gp2) and set 20 as Allocated Storage <br>

![Capture d’écran 2024-07-30 134024](https://github.com/user-attachments/assets/6e017d05-6a90-4111-a7e5-f174aafea240)
![Capture d’écran 2024-07-30 134647](https://github.com/user-attachments/assets/4278a4cf-4171-462e-b4ea-55956a5dc6d6)


> In the Connectivity section : <br>
>> Set the option to not connect to EC2, and select IPv4 as the network type.<br>
>> For the Virtual Private Cloud (VPC), choose the desired VPC.<br>
>> In the Database subnets group, select the one associated with the chosen VPC.<br>
>> For public access, select "Yes."<br>
>> In the Security group section, select an existing group and then choose the corresponding VPC security group.<br>

![Capture d’écran 2024-07-30 135206](https://github.com/user-attachments/assets/34563982-01e3-4114-b4ec-0db598e87d60)
![Capture d’écran 2024-07-30 135634](https://github.com/user-attachments/assets/cde12275-0981-4ca3-84c5-9cfdddb2a6a3)

> Leave the remaining settings as default, and then click on "Create database."<br>

![Capture d’écran 2024-07-30 141520](https://github.com/user-attachments/assets/ffc9d7af-10f7-4267-865b-43701b0362f3)
![Capture d’écran 2024-07-30 141710](https://github.com/user-attachments/assets/f6bd55a5-d6c1-414e-8154-8cb6762770be)
![Capture d’écran 2024-07-30 141940](https://github.com/user-attachments/assets/a11d0d25-5854-44d1-996f-1f39675dc234)
![Capture d’écran 2024-07-30 142340](https://github.com/user-attachments/assets/b1205fa8-8257-497a-b32c-00e63f3f5cd7)

##### ------------- How to connect the DB instance in local pgAdmin  -------------- :
After Amazon RDS provisions your DB instance, you can use any standard SQL client application to connect to the instance. Before you can connect, the DB instance must be available and accessible. Whether you can connect to the instance from outside the VPC depends on how you created the Amazon RDS DB instance: <br>
> If you created your DB instance as public, devices and Amazon EC2 instances outside the VPC can connect to your database. <br>
> If you created your DB instance as private, only Amazon EC2 instances and devices inside the Amazon VPC can connect to your database. <br>

To check whether your DB instance is public or private, use the AWS Management Console to view the Connectivity & security tab for your instance. Under Security, you can find the "Publicly accessible" value, with No for private, Yes for public. <br>

![Capture d’écran 2024-08-19 015800](https://github.com/user-attachments/assets/4f71b378-777b-4655-b37d-4af2e55941c9)
![Capture d’écran 2024-08-19 015933](https://github.com/user-attachments/assets/ee77a076-a4e6-4c39-80ad-490ffb8fbfbc)
![Capture d’écran 2024-08-19 021030](https://github.com/user-attachments/assets/501c852f-5f14-41f1-9357-5f4419020029)

**-------------- Finding the connection information for an RDS for PostgreSQL DB instance ---------------:** <br>
If the DB instance is available and accessible, you can connect by providing the following information to the SQL client application: <br>
> The **DB instance endpoint**, which serves as the host name (DNS name) for the instance. <br>
> The **port** on which the DB instance is listening. For PostgreSQL, the default port is 5432. <br>
> The **username and password** for the DB instance. The default 'master username' for PostgreSQL is postgres. <br>
> The **name and password** of the database (DB name). <br>

![Capture d’écran 2024-08-19 020032](https://github.com/user-attachments/assets/91de5448-e7b3-4338-a5a7-cca083dcaa4a)

**---------------- Using pgAdmin to connect to a RDS for PostgreSQL DB instance ----------------:** <br>
You can use the open-source tool pgAdmin to connect to your RDS for PostgreSQL DB instance. You can download and install pgAdmin from http://www.pgadmin.org/
without having a local instance of PostgreSQL on your client computer. <br>
To connect to your RDS for PostgreSQL DB instance using pgAdmin <br>
> Launch the pgAdmin application on your client computer. <br>

![Capture d’écran 2024-08-19 021134](https://github.com/user-attachments/assets/331a4de5-34f4-4218-86cd-b342b6d328ac)

> On the Dashboard tab, choose Add New Server. <br>

![Capture d’écran 2024-08-19 021232](https://github.com/user-attachments/assets/709018c0-7b96-43ca-8079-8c213868b481)

> In the Create - Server dialog box, type a name on the General tab to identify the server in pgAdmin. <br>
> On the Connection tab, type the following information from your DB instance: <br>
>> For Host, type the endpoint, for example mypostgresql.c6c8dntfzzhgv0.us-east-2.rds.amazonaws.com. <br>
>> For Port, type the assigned port. <br>
>> For Username, type the user name that you entered when you created the DB instance (if you changed the 'master username' from the default, postgres). <br>
>> For Password, type the password that you entered when you created the DB instance. <br>

![Capture d’écran 2024-08-19 022127](https://github.com/user-attachments/assets/58fcba3a-39cf-4892-9581-14252e7e1fd2)
![Capture d’écran 2024-08-19 022249](https://github.com/user-attachments/assets/0ba430b1-ed52-42c6-b211-a0729f6e0938)
![Capture d’écran 2024-08-19 022550](https://github.com/user-attachments/assets/7259bcd5-845a-4500-85c8-868f9052bbe7)
![Capture d’écran 2024-08-19 023714](https://github.com/user-attachments/assets/b5648b9b-5109-41c0-8360-cba57a2adac2)
![Capture d’écran 2024-08-19 023850](https://github.com/user-attachments/assets/de0f04d2-fba5-4b0d-8b20-f51c4c55cec0)




















