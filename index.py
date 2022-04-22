import json
import sys
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import filedialog
from stripjson import filepicker


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


g = False
while g == False:
    print(bcolors.BOLD + bcolors.OKBLUE +
          "Chat Sentiment Analyzer \n ---------------------")
    print("""
    Open File Explorer: E
    Close Process: Q
    Validate JSON:J
    """)
    m = input("Enter an option:")
    if(m.lower() == 'e'):
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.update()
        root.withdraw()
        g = True

        file_path = filedialog.askopenfilename()
        print(file_path)
    if(m.lower() == 'q'):
        sys.exit()
    if(m.lower() == 'j'):
        filepicker()


sia = SentimentIntensityAnalyzer()

filtered_data = []
positive, negative, neutral = 0, 0, 0


x = True
with open(file_path, encoding='utf-8') as f:
    data = json.loads(f.read())


for x in data["messages"]:
    filtered_data.append(x)


for x in range(len(filtered_data)):
    # print(str(sia.polarity_scores(
    #   filtered_data[x]["msg"])) + filtered_data[x]["msg"])

    if(sia.polarity_scores(filtered_data[x]["msg"])["neu"] == 1.0):
        neutral += 1
        pass
    if(sia.polarity_scores(filtered_data[x]["msg"])["pos"] > sia.polarity_scores(filtered_data[x]["msg"])["neg"]):
        positive += 1
    else:
        negative += 1


print("Testing neutrality!")
print("Negativity:" +
      str(round((negative/(positive+negative+neutral))*100)) + "%" + " Negative: ", negative)
print("Positivity:" +
      str(round((positive/(positive+negative+neutral))*100)) + "%"+"Postives: ", positive)
print("Neutrality:" +
      str(round((neutral/(positive+negative+neutral))*100)) + "%"+" Neutral:", neutral)
