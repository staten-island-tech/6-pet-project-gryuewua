wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}

for ward, value in wards.items():
    for v in value:
        if v in staff:
            "hi"
        else:
            staff[v] = {
                'ward': ward
            }
print(staff)