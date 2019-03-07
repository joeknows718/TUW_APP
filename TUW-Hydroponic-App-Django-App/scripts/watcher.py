import sys
import time
import json
import pymysql
import datetime


mydb = pymysql.connect(host='localhost',
user='root',
passwd='andthenhesaidlettherebelight',
db='testdb')


from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    patterns=["*.JSON"]

    def on_modified(self, event):
        with open('test_data_set.JSON') as data_file:
            raw_data = json.load(data_file)
        dataset_to_add = raw_data["datasets"][-1]
        x = dataset_to_add['datetime']

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO datasets (DateTime) VALUES (%s)",x)
        mydb.commit()
        cursor.close()
        currentDT = datetime.datetime.now()
       
        print("File was Modified at %s" %(currentDT))

if __name__ == '__main__':
    
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
