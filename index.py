import json
from statistics import mode
import sys
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import filedialog
from utils import stripjson, filepicker, mostFrequentWord
filtered_data, sentences, words = [], [], []


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


file_path = ''
g = False
while g == False:
    print(
        "\nChat Sentiment Analyzer \n ---------------------")
    print("""
    Select File: E
    Sentiment Analysis:S
    Find out the most used word:B
    Close Process: Q
    Validate JSON:J
    """)
    print("Selected file: ", bcolors.WARNING + file_path + bcolors.ENDC)

    m = input("Enter an option:")
    if(m.lower() == 'e'):
        file_path = filepicker()
        with open(file_path, encoding='utf-8') as f:
            data = json.loads(f.read())
        for x in data["messages"]:
            filtered_data.append(x)

    if(m.lower() == 'q'):
        sys.exit()
    if(m.lower() == 'j'):
        stripjson(file_path)
    # if(m.lower() == 'b'):
    #    for x in filtered_data:
    #        sentences.append(x["msg"])

    #   print("Most used word is:" + str(mostFrequentWord(sentences)["word"]))

    if(m.lower() == 's'):
        sia = SentimentIntensityAnalyzer()
        sia.lexicon_file = 'vader.txt'

        positive, negative, neutral = 0, 0, 0

        x = True

        for x in range(len(filtered_data)):

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
