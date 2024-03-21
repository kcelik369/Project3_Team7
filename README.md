# UC Berkeley Extension Data Analysis Project 3 - Team 7

An overview of the project and its purpose

We are investigating a dataset for Seattle Airbnb data found on Kaggle (https://www.kaggle.com/datasets/airbnb/seattle).
Original source of the data is here (http://insideairbnb.com/get-the-data/), which provides access to more recent data and for other cities.

how to use and interact with the project
We hope to create a set of tables that could be used to answer the following questions:
- What factors are most strongly linked with good ratings / high prices / frequent bookings?
- What outliers exist for the above major factors?
- What is the correlation between these major factors and do they have any significant correlation with other minor factors?
- Can we observe any fluctuations in price (extra credit: other characteristics) based on month / season?
- If you want to start hosting in Seattle (or generally), what factors correlate with success or positive host ratings?
- Are hosts with many Airbnb listings significantly different from hosts with fewer listings?

1. Our questions are limited to the ~2016 dataset;
2. Given access to more cities' data, what might change or not?
2. Given access to more recent Seattl data, what might change or not?

efforts for ethical considerations made in the project
Data ethics: maybe provide a boolean flag for devs to keep this data?
1. Names
1. Streets
1. VERY specific lat, long
1. Dataset source: Kaggle
2. Reliability?
2. Accurate picture of AirBnb data? Already transformed?

Other Seattle datasets to add additional info / minor factors to evaluate on?
- Neighborhood Scout (?)
- Redfin (?): walk score, transit score, etc.
- Zillow (?)




The project uses ETL workflows to ingest data into the database. (10 points)

The original dataset(s) are transformed prior to storing it in the database. The database contains 3817 entries that meets requirement of at least 100 unique records. Pandas DataFrame Kerim/Mari

A database is used to house the data (SQL, MongoDB, SQLite, etc.). The database has at least two tables (SQL) or collections (NoSQL). Kylie

 

**The project documents the choice of the database used and why. (5 points)**

The project includes documentation of the ETL workflow with diagrams or ERD. Elizabeth



The project uses one additional library not covered in class related to data engineering. Kerim
Flask API with JSON output Kerim

No borrowed code








