from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json

with open("seting.json", "r") as with_json_file:
    json_file = json.load(with_json_file)

folder_name = json_file['folder_name']
folder_track = json_file['folder_track']


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder_track):

            for Folder_name in folder_name:
                suffix = file.split(".")[-1].lower()

                if len(file.split(".", 1)) > 1 and (suffix in folder_name[Folder_name]):

                    if Folder_name not in os.listdir(folder_track):
                        os.mkdir(folder_track + '/' + Folder_name)

                    file, Folder_name = '/' + file, '/' + Folder_name
                    os.rename(folder_track + file, folder_track + Folder_name + file)


if __name__ == '__main__':
    handle, observer = Handler(), Observer()
    observer.schedule(handle, folder_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
