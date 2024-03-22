# UC Berkeley Extension Data Analysis Project 3 - Team 7

An overview of the project and its purpose:

We are investigating a dataset for Seattle Airbnb data found on Kaggle (https://www.kaggle.com/datasets/airbnb/seattle).
Original source of the data is here (http://insideairbnb.com/get-the-data/), which provides access to more recent data and for other cities. The original databases, stored in CSV files: listings, calendar and listing scores, contain over 100 entries each meeting project's requirement of utilizing dataset with at least 100 unique records.

The project uses ETL workflows to ingest data into the database. 
A database is used to house the data (SQL, MongoDB, SQLite, etc.). The database has at least two tables (SQL) or collections (NoSQL).
The project includes documentation of the ETL workflow with diagrams or ERD. 
The project uses one additional library not covered in class related to data engineering. Kerim
Flask API with JSON output Kerim

Project doesn't include any borrowed code.

Limitations of the project:
1. Our questions are limited to the ~2016 dataset;
2. Given access to more cities' data, what might change or not?
2. Given access to more recent Seattl data, what might change or not?

How to use and interact with the project:

The cleaned and transformed dataset could be used to answer the following questions:
- What factors are most strongly linked with good ratings / high prices / frequent bookings?
- What outliers exist for the above major factors?
- What is the correlation between these major factors and do they have any significant correlation with other minor factors?
- Can we observe any fluctuations in price (extra credit: other characteristics) based on month / season?
- If you want to start hosting in Seattle (or generally), what factors correlate with success or positive host ratings?
- Are hosts with many Airbnb listings significantly different from hosts with fewer listings?


Efforts for ethical considerations made in the project:

1. Protect the privacy of hosts and guests names, addresses, etc.  Limit access or remove personal contact information.
2. Be aware of biases in guest reviews and ensure that predictive modeling does not inadvertently perpetuate biases or disadvantage certain hosts. 
3. Consider the impact of AirBnB on the local community - from noise complaints  to housing availability and affordability - when analyzing data such as price trends and review comments. 


**The project documents the choice of the database used and why. (5 points)**


Team roles:

Kerim:
 1. Transformed original listings_id CSV in Jupyter Notebook
 2. Created sub databases: listings_cleaned, hosts and listing_scores
 3. Incorporated a code utilizing seaborn library to present examples of visualization of the dataset
 4. Built a Flask App to store JSONified data

Mari:
 1. Transformed original Calendar CSV in Jupyter Notebook to present average monthy pricing for each listing id
 2. Merged original Calendar dataset with Listings_cleaned to pull in property type and neighborhood
 3. Performed further analysis of the average pricing based on the combination of the 2 factors, mentioned above: property type and neighborhood

Elizabeth:
 1. Build ERD for all connected tables of the Dataset
 2. Assigned data types and primary keys in ERD

Kylie:
 1. Created Database and Tables in PgAdmin with SQL code
 2. Uploaded CSV files into PgAdmin to store in SQL Database

Collaborative effort to build a slide deck for presentation.






