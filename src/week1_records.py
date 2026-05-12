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

#print(clean_record(raw_record))


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

#print(func(records))


employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000, "active": True},
    {"name": "Bob", "department": "Marketing", "salary": 72000, "active": False},
    {"name": "Carol", "department": "Engineering", "salary": 105000, "active": True},
    {"name": "Dave", "department": "Marketing", "salary": 68000, "active": True},
    {"name": "Eve", "department": "Engineering", "salary": 89000, "active": False},
]

def employee_agg(employeelist):
    actives1=[element["name"] for element in employeelist if element["active"]==True]
    actives2=[]
    for elem in employeelist:
        if elem["active"]==True:
            actives2.append(elem["name"])
    totalsal=sum([element["salary"] for element in employeelist if element["active"]==True])
    groups={
    depts: [r["name"] for r in employeelist if r["department"]==depts]
    for depts in set(element["department"] for element in employeelist)

    }
    
    return actives1,actives2,totalsal,groups



print(employee_agg(employees))



raw_order = {
    "order_id": "  ORD-5521 ",
    "customer": "jane doe",
    "items": "burger, fries, soda",
    "total": "29.99",
    "delivered": "N"
}

def clean_order(order):
    
    return order['order_id'].strip(),order["customer"].title(),order["items"].split(","),float(order["total"]),order["delivered"]=="Y"

print(clean_order(raw_order))