import os
import json
import csv
import pprint
from datetime import date

helping_dic = {}

# input file (containing ALL zotero data)
goodname = "Seshat_Databank_REFS_JSON.json"
# the above file can be used by itself, we don't have to convert it to CSV.


# we want to save the data in a form that is easier to be used in SSQL
with open(goodname, "r") as jsonfile:
    helping_dic = json.load(jsonfile)



    
print(len(helping_dic))