import os
import json
import csv
import pprint
from datetime import date

helping_dic = {}

# input file (containing ALL zotero data)
goodname = "Seshat_Databank_Updated_GSed.json"
# the above file can be used by itself, we don't have to convert it to CSV.


# we want to save the data in a form that is easier to be used in SSQL
with open(goodname, "r") as jsonfile:
    a_dictionary = json.load(jsonfile)
    with open("zotero_output_csv_8_Nov_2021.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t')
        for ref in a_dictionary:
            # preparation
            # Everything seems to have the id. Perfect Zotero URL
            helping_dic["zotero_id"] = ref["id"]
            # Some items do not have a title, we go for container-title
            if "title" in ref.keys():
                helping_dic["title"] = ref["title"]
            else:
                helping_dic["title"] = ref["container-title"]
            # original URL
            if "URL" in ref.keys():
                helping_dic["URL"] = ref["URL"]
            else:
                helping_dic["URL"] = ""
            # year:
            if "issued" in ref.keys():
                if "date-parts" in ref["issued"].keys():
                    helping_dic["year"] = ref["issued"]["date-parts"][0][0]
            elif "accessed" in ref.keys():
                helping_dic["year"] = ref["accessed"]["date-parts"][0][0]
            else:
                # handling bad years
                helping_dic["year"] = "0000"
                #print(ref["id"])
            # main author (editor) family name:
            if "author" in ref.keys():
                if "family" in ref["author"][0].keys():
                    helping_dic["author"] = ref["author"][0]["family"]
                elif "literal" in ref["author"][0].keys():
                    helping_dic["author"] = ref["author"][0]["literal"].split(" ")[-1]
            elif "editor" in ref.keys():
                if "family" in ref["editor"][0].keys():
                    helping_dic["author"] = ref["editor"][0]["family"]
                elif "literal" in ref["editor"][0].keys():
                    helping_dic["author"] = ref["editor"][0]["literal"].split(" ")[-1]
            else:
                helping_dic["author"] = "No Author"
                print(ref['id'])
            csv_writer.writerow([helping_dic["author"], helping_dic["title"], helping_dic["year"], "No Description", date.today(), date.today(), helping_dic["URL"], helping_dic["zotero_id"]])


    
#print(len(helping_dic))