from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

#  print(plt.style.available)
# execute the above to show a list of options for styles
# Note some style have their own grid and color preferences

# This is what to type in for styles
plt.style.use('fivethirtyeight')
# plt.xkcd() # Comic book style

# to load in a csv file
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

    #row = next(csv_reader)
    # To split the values from the semi colon just use the split method
    #gprint(row['LanguagesWorkedWith'].split(';'))
# Prints the results fo the counter and splits it up to the 15 most common

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)


print(languages,"\n",popularity)

#print(language_counter.most_common(15))
"""
A format String consists of a part for color, marker, and line:
    fmt = '[marker][line][color]'
"""


# # Title
plt.title("Programming Language Popularity")
#
# Axis Labels
plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use it")
#
# # Add a Legend
# # plt.legend(["All Devs", "Py Devs"])
# # or
# plt.legend()
# # Below will adjust the plot parameters to give some padding
plt.tight_layout()
# Adds a grid to the graph
# plt.grid(True)

# To save the graph as an image:
# plt.savefig("[name].png") you can also pass in a full path inside the method to save it to a specific location

plt.show()
