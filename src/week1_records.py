raw_record = {
    "patient_id": "  P-1042 ",
    "admit_date": "2024-01-15",
    "discharge_date": "2024-01-18",
    "diagnosis_codes": "I10, E11.9, Z79.4",
    "attending_physician": "dr. sarah chen",
    "readmitted": "Y"
}

def clean_record(record):
    return {
        "patient_id": record["patient_id"].strip(),
        "admit_date": record["admit_date"],
        "discharge_date": record["discharge_date"],
        "diagnosis_codes": record["diagnosis_codes"].split(", "),
        "attending_physician": record["attending_physician"].title(),
        "readmitted": record["readmitted"] == "Y"
    }

print(clean_record(raw_record))


#All unique diagnosis codes across all records → should be a set
#Count of readmitted patients → should be a single number
#Records grouped by physician → should be a dict of lists

records = [
    {
        "patient_id": "P-1042",
        "diagnosis_codes": ["I10", "E11.9", "Z79.4"],
        "attending_physician": "Dr. Sarah Chen",
        "readmitted": True
    },
    {
        "patient_id": "P-1043",
        "diagnosis_codes": ["I10", "J45.0"],
        "attending_physician": "Dr. James Park",
        "readmitted": False
    },
    {
        "patient_id": "P-1044",
        "diagnosis_codes": ["Z79.4", "E11.9"],
        "attending_physician": "Dr. Sarah Chen",
        "readmitted": True
    }
]

def func(records):

    unique_codes = set(code for record in records for code in record["diagnosis_codes"])
    count_pats=len([record["patient_id"] for record in records if record["readmitted"]==True])
    group_records = {
    physician: [r for r in records if r["attending_physician"] == physician]
    for physician in set(record["attending_physician"] for record in records)
}
    return unique_codes,count_pats,group_records

print(func(records))
