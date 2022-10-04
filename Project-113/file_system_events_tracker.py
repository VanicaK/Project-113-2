import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/vijay.LAPTOP-6K2HIQ6S/OneDrive/Desktop/VS Projects Python"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"Hey!, {event.src_path} has been created!")
    #2_on_deleted
    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted!")
    #3_on_modified
    def on_modified(self, event):
        print(f"Someone has modified {event.src_path}")
    #4_on_moved
    def on_moved(self, event):
        print(f"{event.src_path} has been moved to {event.dest_path}")

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped.")
    observer.stop()





