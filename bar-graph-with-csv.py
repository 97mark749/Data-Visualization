from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

#  print(plt.style.available)
# execute the abaove to show a list of options for styles
# Note some style have their own grid and color preferences

# This is what to type in for styles
plt.style.use('fivethirtyeight')
# plt.xkcd() # Comic book style

# to load in a csv file
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

    #row = next(csv_reader)
    # To split the values from the semi colon just use the split method
    print(row['LanguagesWorkedWith'].split(';'))
    
print(language_counter.most_common(15))
"""
A format String consists of a part for color, marker, and line:
    fmt = '[marker][line][color]'
"""


# # Title
# plt.title("Median Salary (USD) By Age")
#
# # Axis Labels
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
#
# # Add a Legend
# # plt.legend(["All Devs", "Py Devs"])
# # or
# plt.legend()
# # Below will adjust the plot parameters to give some padding
# plt.tight_layout()
# Adds a grid to the graph
# plt.grid(True)

# To save the graph as an image:
# plt.savefig("[name].png") you can also pass in a full path inside the method to save it to a specific location

plt.show()
