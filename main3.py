from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json


with open("seting.json", "r") as with_json_file:
    json_file = json.load(with_json_file)


for f in json_file["folder_name"]:
    if f not in os.listdir(json_file["folder_track"]):
        os.mkdir(json_file["folder_track"] + "/" + f)



class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(json_file["folder_track"]):
            for folder_name in json_file["folder_name"]:
                if len(filename.split(".", 1)) > 1 and (filename[::-1].split(".", 1)[0].lower()[::-1] in json_file["folder_name"][folder_name]):
                    os.rename(json_file["folder_track"] + "/" + filename, json_file["folder_track"] + "/" + folder_name + "/" + filename)



if __name__ == '__main__':
    handle = Handler()
    observer = Observer()
    observer.schedule(handle, json_file["folder_track"], recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
