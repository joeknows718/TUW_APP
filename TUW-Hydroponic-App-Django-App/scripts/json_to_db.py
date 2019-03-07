import json
import pymysql

mydb = pymysql.connect(host='localhost',
user='root',
passwd='andthenhesaidlettherebelight',
db='testdb')

with open('test_data_set.JSON') as data_file:
    raw_data = json.load(data_file)
    

dataset_to_add = raw_data["datasets"][-1]
x = dataset_to_add['datetime']


cursor = mydb.cursor()

cursor.execute("INSERT INTO datasets (DateTime) VALUES (%s)",x)
mydb.commit()
cursor.close()
print("Done")
