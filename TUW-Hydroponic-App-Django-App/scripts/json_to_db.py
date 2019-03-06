import json


with open('test_data_set.JSON') as data_file:
    raw_data = json.load(data_file)
    

dataset_to_add = raw_data["datasets"][-1]

for x,y in dataset_to_add.items():
    print(x,y)
