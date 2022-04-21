import json
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.attributes('-topmost', True)
root.update()
root.title = 'Select file to format ( only accepts JSON exported from DiscordChatExporter by Tyrrrz)'
root.withdraw()
file_path = filedialog.askopenfilename()


f = open(file_path, 'r', encoding='utf-8')
e = json.loads(f.read())
list = []

for x in e["messages"]:
    b = {'msg': x["content"], 'user': x["author"]
         ["name"], 'time': x['timestamp']}
    list.append(b)

dict = {"messages": list}
with open("dms.json", "w") as f:
    f.write(json.dumps(dict))
