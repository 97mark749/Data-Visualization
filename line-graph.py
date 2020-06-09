from matplotlib import pyplot as plt

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y, label='Python')

# Title
plt.title("Median Salary (USD) By Age")

# Axis Labels
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# Add a Legend
#plt.legend(["All Devs", "Py Devs"])
# or
plt.legend()
plt.show()