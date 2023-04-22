import os, csv, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyApp.settings')
django.setup()

# Model import
from home.models import Measurement

# Reading file
with open("measurements.csv", newline='', encoding='utf-8') as csvfileRead:
    response_reader = csv.reader(csvfileRead, delimiter=',')
    next(response_reader)
    sl = 1
    for row in response_reader:
        sl += 1
        try:
            height, weight, age, waist = row[0], row[1], row[2], row[3]
            obj = Measurement(height=height, weight=weight, age=age, waist=waist)
            obj.save()
            print("Created new object: ", obj)
        except Exception as e:
            print(e)
    print("Total: ", sl, " imported")
