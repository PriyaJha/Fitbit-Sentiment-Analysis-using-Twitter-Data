import pickle
import json
import collections
import matplotlib.pyplot as plt
from collections import Counter
gender_guesser.download()
import gender_guesser.detector as gender

input_data = pickle.load( open( "Fitbit_SMM_TweetsData.pkl", "rb" ) )
count=0
PositiveCount = 0
NegativeCount = 0
NeutralCount = 0
genders = []
d = gender.Detector()
for record in input_data:
    if 'user_name' in record.keys():
        gender = record["user_name"].split(" ")
        if len(gender) > 0:
            val = d.get_gender(gender[0].strip())
            if val == "male" or val == "female":
                genders.append(val)

    else:
        if 'user' in record.keys():
            gender = record["user"]["name"].split(" ")
            if len(gender) > 0:
                val = d.get_gender(gender[0].strip())
                if val == "male" or val == "female":
                    genders.append(val)


data = Counter(genders)
print(data)
my_colors = ('#4286f4','#9dbdf2')
plt.title("#Fitbit - Gender Report")
labels = 'Female', 'Male'
d=[]
for i in data.values():
    d.append(i)
plt.pie(d, labels=labels, shadow=True, startangle=90, colors = my_colors)


plt.show()