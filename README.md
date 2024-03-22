# UC Berkeley Extension Data Analysis Project 3 - Team 7

## About our project
We are investigating a dataset for Seattle Airbnb data found on Kaggle (https://www.kaggle.com/datasets/airbnb/seattle).
The original source of the data is here (http://insideairbnb.com/get-the-data/), which provides access to more recent data and for other cities as well. The original databases, stored in CSV files: listings, calendar and reviews contain over 100 entries each, meeting the requirement of utilizing dataset(s) with at least 100 unique records.

Performing analysis on AirBnb data might be useful for a variety of interested parties. Utility that we could gain by performing analysis could include:
- Improving current listing performance or predicting which listings could perform well in the future
- Observing pricing trends over time or comparing seasonal data
- Insights about host satisfaction and listing reviews
- Correlation between important factors such as price or review score and other factors present

## Process
The project uses ETL workflows to ingest data into the database. We use Pandas to extract and transform the data, then save it to new CSV files. To demonstrate one possible option for the load step, we used PGAdmin to create tables using SQL; five tables in total. An ERD document is included in multiple formats in the folder named "ERD".

To display the data created after the ETL process is complete, we use Pandas DataFrames. We use the Seaborn library (https://seaborn.pydata.org/examples/index.html) to create a set of visualizations demonstrating how data might be analyzed within and across tables. We also serve data via a Flask application to allow for additional functionality on the most significant tables: listings and hosts.

Our project does not include any borrowed code; citations are included in-line where code was built based on external guidance or significant documentation.

The cleaned and transformed dataset could be used to answer the following questions:
- What factors are most strongly linked with good ratings / high prices / frequent bookings?
- What outliers exist for the above major factors?
- What is the correlation between these major factors and do they have any significant correlation with other minor factors?
- Can we observe any fluctuations in price based on month / season?
- If you want to start hosting in Seattle (or generally), what factors correlate with success or positive host ratings?
- Are hosts with many Airbnb listings significantly different from hosts with fewer listings?

## How to use
- The extract and load steps of the project can be performed by running the "extractX.ipynb" files found at the top level of this repository; these also contain our DataFrame displays of various data. 
- We have included documentation for our load step via SQL files and a document in the file named "SQL" as well as supplementary ERD documentation in the file named "ERD". 
- All Seaborn visualizations can be replicated by running the file "seaborn.ipynb"; this file also demonstrates utilization of multiple tables at once. 
- Finally, the Flask app can be started by running "python flask_app.py" at the top level of this repository; instructions on which routes are available and their use are detailed on the base route of the app.
    - The app provides functionality for the two largest tables: hosts and listings.
    - All functional routes begin with ".../api/v1.0/..."
    - The hosts and listings tables can be sampled, extracted in full, or have certain columns served.
    - The format for obtaining certain columns at ".../api/v1.0/X/cols/..." is to input a series of indices separated by commas. If all indices are valid, you will get an abbreviated version of the table with only the specified columns present.
    - At ".../api/v1.0/cols/...", you will add the names of two columns, separated by a "/" character (e.g. .../api/v1.0/cols/id/price). If those columns are present in either table, you will get two columns of data corresponding to the specified column names. If the columns were on separate tables, those tables were merged to provide this data.

## Data Ethics
In consideration of ethical concerns related to the data, we removed certain columns that we did not believe useful for any analyses and could reveal too much information about an individual. Among others, these included:
1. Names
1. Specific lat, long coordinates for listings

With ID columns present for hosts, listings, and reviews, we felt it was sufficient to use these to describe individual rows in our dataset. We preserved rows for larger groupings such as neighborhood. In combination, these wider descriptions could be combined to make descriptive labels for data when necessary for visualization; for example: West Town 2-bedroom apartment. 

Additionally, the full dataset is available elsewhere, and no secondary data that might be used to identify individuals was added as a result of our efforts. We therefore believe our dataset to be free of any major ethical concerns.

## Team Roles 
Kerim:
 1. Led the Team to success
 1. Transformed
 1. Seaborn data visualization creation
 1. Built a Flask App to serve JSONified data

Mari:
 1. Transformed original Calendar CSV in Jupyter Notebook to present average monthy pricing for each listing id
 1. Merged original Calendar dataset with Listings_cleaned to pull in property type and neighborhood
 1. Performed further analysis of the average pricing based on the combination of the 2 factors, mentioned above: property type and neighborhood

Elizabeth:
 1. Build ERD for all connected tables of the Dataset
 1. Assigned data types and primary keys in ERD

Kylie:
 1. Created Database and Tables in PgAdmin with SQL code
 1. Uploaded CSV files into PgAdmin to store in SQL Database

Collaborative effort to build a slide deck for presentation and refine this README.






