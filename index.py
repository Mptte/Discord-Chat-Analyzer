import json
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
print(sia.lexicon_file)

filtered_data = []
positive, negative, neutral = 0, 0, 0


x = True
with open("dms.json", encoding='utf-8') as f:
    data = json.loads(f.read())

for x in data["messages"]:
    b = {'msg': x["content"], 'user': x["author"]
         ["name"], 'time': x["timestamp"]}
    filtered_data.append(b)

for x in range(len(filtered_data)):
    # print(str(sia.polarity_scores(
    #    filtered_data[x]["msg"])) + filtered_data[x]["msg"])

    if(sia.polarity_scores(filtered_data[x]["msg"])["neu"] == 1.0):
        neutral += 1
        pass
    if(sia.polarity_scores(filtered_data[x]["msg"])["pos"] > sia.polarity_scores(filtered_data[x]["msg"])["neg"]):
        positive += 1
    else:
        negative += 1

x = True
while x == True:
    if(input("Test neutrality:") == 'y'):
        x = False
        print("Testing neutrality!")
        print("Negativity:" +
              str(round((negative/(positive+negative+neutral))*100)) + "%")
        print("Positivity:" +
              str(round((positive/(positive+negative+neutral))*100)) + "%")
        print("Neutrality:" +
              str(round((neutral/(positive+negative+neutral))*100)) + "%")
        break

    if(input("Test sentiment(y/n):") == 'n'):
        break
