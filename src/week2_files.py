import csv
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "patients.csv")

def clean_record(record):
    return {
        "patient_id": record["patient_id"].strip(),
        "admit_date": record["admit_date"],
        "discharge_date": record["discharge_date"],
        "diagnosis_codes": record["diagnosis_codes"].split(","),
        "attending_physician": record["attending_physician"].title(),
        "readmitted": record["readmitted"] == "Y"
    }

with open(data_path, mode='r',newline='') as file:
    reader=csv.DictReader(file)
    next(reader)
    for row in reader:
        cleaned=clean_record(row)
        #print(cleaned)


cleaned_records = []

with open(data_path, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cleaned_records.append(clean_record(row))

# now write to JSON
output_path = os.path.join(BASE_DIR, "output", "cleaned_patients.json")

#with open(output_path, "w") as f:
#    json.dump(cleaned_records, f, indent=4)
a=len([element["patient_id"] for element in cleaned_records])
b=len([element["patient_id"] for element in cleaned_records if element["readmitted"]])
c=len({x for l in [element["diagnosis_codes"] for element in cleaned_records] for x in l})
d=max(["Dr. Sarah Chen", "Dr. James Park"], key=lambda name: name.count("a"))

print(a,b,c,d)