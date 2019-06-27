from os import path
import json

filename = "slim_database.json"

# Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

# Use the new datastore datastructure
data = datastore["datas"]
