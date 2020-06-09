from matplotlib import pyplot as plt

#  print(plt.style.available)
# execute the abaove to show a list of options for styles
# Note some style have their own grid and color preferences


# This is what to type in for styles
# plt.style.use('fivethirtyeight')
plt.xkcd() # Comic book style


"""
A format String consists of a part for color, marker, and line:
    fmt = '[marker][line][color]'
"""

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, 'k--', label='All Devs')
# or
plt.plot(ages_x, dev_y, linewidth = '4',linestyle='--' , marker='o', label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# plt.plot(ages_x, py_dev_y, 'b', label='Python')
# or
plt.plot(ages_x, py_dev_y, linewidth = '2', linestyle = ':', label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y,  linestyle = '-.', marker = '^', label = 'JavaScript')

# Title
plt.title("Median Salary (USD) By Age")

# Axis Labels
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# Add a Legend
#plt.legend(["All Devs", "Py Devs"])
# or
plt.legend()
# Below will adjust the plot parameters to give some padding
plt.tight_layout()
# Adds a grid to the graph
#plt.grid(True)

# To save the graph as an image:
# plt.savefig("[name].png") you can also pass in a full path inside the method to save it to a specific location

plt.show()