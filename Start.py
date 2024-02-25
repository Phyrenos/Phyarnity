from Gui import Main
import os
from time import sleep
import requests

def Start():
    os.system("Title Phyarnity")
    print("Thank you for using Phyarnity Version 1.0.0...")
    print("Checking if this is the first installation...")

    appdata_path = os.path.expanduser(os.getenv('APPDATA'))
    file_path = os.path.join(appdata_path, "Phyarnity/")
    if not os.path.exists(file_path):
        print("This is your first time running this application...")
        print("Creating folder {}...".format(file_path))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        print("Downloading Database and necessary data...")

        open(os.path.dirname(file_path) + "/db.json", "x")
        with open(os.path.dirname(file_path) + "/db.json", "w") as db:
            db.write(requests.get(url="https://raw.githubusercontent.com/Phyrenos/Phyarnity/main/db.json").text)
    print("Passed check...")

    print("Starting Main GUI now...")
    sleep(3)
    Main.start()

Start()