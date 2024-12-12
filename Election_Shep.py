import csv
import plotly
import plotly.express as px
import pandas
import string

trumpspeech = open('cleaned_trump_speech_transcript.txt')
uselesswords= ['they', 'i', 'we','you', 'and', 'a','am','who','no','to','at', 'have','the','know','she','shes','of','with','has','he','hes','thier',"they're",'in','about','are','your','my','mine','what','would','that','make','us','all','wherever','always','but','was','one','out','behalf','because','this','be','for','there','can','so,','like','and,','or','it','not','let','from', 'its',"an","as","when","is","will","our","their","on","his","me","us.","by","more","were","than","ever","so","new","also","most","other","been","these","every","never","them","going","up","into","her","just","any"]
counts = dict()

for line in trumpspeech:
    line = line.lower()
    table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}
    new_s = line.translate(table)
    words = line.split()     
    for word in words:
        if word in uselesswords:
            continue
        if word not in counts:

            counts[word] = 1
        else:
            counts[word] += 1
#open file for writing


linecount = 0
with open('trump_freq.csv', "w") as f:
    for key, value in counts.items():
        if value > 8:
            f.writelines(key + "," + str(value) + "\n",)
            linecount += 1
            if linecount>9:
                break
            





'''
df = px.data.tips()
counts = px.pie(df, values='tip', names='day')
counts.show()

counts = dict(sorted(counts.items(), key=lambda item: -item[1]))
counts = 0
newcounter = dict()
for i in counts:
    if counts < 10:
        newcounter[i] = counts[i]
        counts += 1
    else: 
        break
    print(newcounter)

'''