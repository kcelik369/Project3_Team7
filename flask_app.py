from flask import Flask, jsonify
import pandas as pd
import json

# ===== SETUP =====
app = Flask(__name__)

listings = pd.read_csv('./Resources/listings_cleaned.csv')
hosts = pd.read_csv('./Resources/hosts.csv')

listing_cols = listings.columns.to_list()
host_cols = hosts.columns.to_list()

listing_dict = dict(enumerate(listing_cols))
host_dict = dict(enumerate(host_cols))
# ===== ===== =====

@app.route("/")
def home():
    listings_explain = 'Information about the listings table and related routes can be found at "/api/v1.0/listings"'
    hosts_explain = 'Information about the hosts table and related routes can be found at "/api/v1.0/hosts"'
    cols_explain = 'If you would like to pull a pair of columns to analyze, see "/api/v1.0/cols" for details'
    return listings_explain + '<br>' + hosts_explain + '<br>' + cols_explain

# ===== LISTINGS-TABLE =====
@app.route("/listings")
def listingsInfo():
    sample_explain = 'To get a sample of this table\'s data, go to "/listings/sample"'
    full_explain = 'To get all of this table\'s data, go to "/listings/full"'
    lcols_explain = 'To get a subset of this table\'s column data, go to "/listings/cols/..."; replace the "..." with a set of indices for the columns you want to extract'
    lcols_indices = f"The columns of the listings table with their indices are {listing_dict}"
    return sample_explain + '<br>' + full_explain + '<br>' + lcols_explain + '<br><br>' + lcols_indices


@app.route("/listings/sample")
def sampleListings():
    return json.loads(listings.head(20).to_json())

@app.route("/listings/full")
def serveListings():
    return json.loads(listings.to_json())

# takes a set of column indicess split by commas and returns just those columns
# with more time, we might use user input, such as checkboxes to select columns to fetch
@app.route("/listings/cols/<deliniated>")
def colsListings(deliniated):
    str_nums = deliniated.split(',')
    int_nums = [int(s) for s in str_nums] # convert split strs to ints

    # simple error handling
    max_cols = len(listings.columns.to_list())
    for i in int_nums:
        if i > max_cols:
            return jsonify("ERROR: one or more column indices out of range")
    
    return json.loads(listings.iloc[:, int_nums].to_json())
# ===== ===== =====

# ===== HOSTS-TABLE =====
@app.route("/hosts")
def hostsInfo():
    sample_explain = 'To get a sample of this table\'s data, go to "/hosts/sample"'
    full_explain = 'To get all of this table\'s data, go to "/hosts/full"'
    hcols_explain = 'To get a subset of this table\'s column data, go to "/hosts/cols/..."; replace the "..." with a set of indices for the columns you want to extract'
    hcols_indices = f"The columns of the hosts table with their indices are {host_dict}"
    return sample_explain + '<br>' + full_explain + '<br>' + hcols_explain + '<br><br>' + hcols_indices

@app.route("/hosts/sample")
def sampleHosts():
    return json.loads(hosts.head(20).to_json())

@app.route("/hosts/full")
def serveHosts():
    return json.loads(hosts.to_json())

@app.route("/hosts/cols/<deliniated>")
def colsHosts(deliniated):
    str_nums = deliniated.split(',')
    int_nums = [int(s) for s in str_nums] # convert split strs to ints

    # simple error handling
    max_cols = len(hosts.columns.to_list())
    for i in int_nums:
        if i > max_cols:
            return jsonify("ERROR: one or more column indices out of range")
    
    return json.loads(hosts.iloc[:, int_nums].to_json())
# ===== ===== =====

# for simplicity, v1.0 only looks in hosts/listings tables, 
# but we could extend functionality to all tables by reformatting the if/else block
@app.route("/api/v1.0/<col_1>/<col_2>")
def pairCols(col_1, col_2):
    if col_1 in listing_cols and col_2 in listing_cols:
        json_str = listings.loc[:, [col_1, col_2]].to_json()
    elif col_1 in host_cols and col_2 in host_cols:
        json_str = hosts.loc[:, [col_1, col_2]].to_json()
    elif (col_1 in listing_cols and col_2 in host_cols) or (col_1 in host_cols and col_2 in listing_cols):
        merged = listings.merge(hosts, on='host_id')
        json_str = merged.loc[:, [col_1, col_2]].to_json()
    else:
        return jsonify("ERROR: one or more column parameters are invalid")
    return json.loads(json_str)

# prospective and simple extension of functionality to handle different cities
# @app.route("/api/v1.0/<city>/<col_1>/<col_2>")
# def cityPairCols(city, col_1, col_2):
    # create dictionary mapping from cities to their respective data table CSVs
    # access specific tables for the city specified in the path
    # pass those tables to a version of pairCols() that takes list of tables as a parameter
# similar extensibility exists for the above table routes, in a similar format:
# /api/v1.0/<city>/listings/..., etc.

if __name__ == "__main__":
    app.run(debug=True)