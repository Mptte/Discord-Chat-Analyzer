import json
import sys
from time import sleep
import tkinter as tk
from tkinter import filedialog


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def filepicker():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.update()
    root.title = 'Select file to format ( only accepts JSON exported from DiscordChatExporter by Tyrrrz)'
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if(file_path == ''):
        print(bcolors.FAIL + "Invalid File Path, Please Select A File")
        sleep(3)
        sys.exit()
    f = open(file_path, 'r', encoding='utf-8')
    e = json.loads(f.read())
    list = []

    for x in e["messages"]:
        b = {'msg': x["content"], 'user': x["author"]
             ["name"], 'time': x['timestamp']}
        list.append(b)

    dict = {"messages": list}
    with open("dms_out.json", "w") as f:
        f.write(json.dumps(dict))
