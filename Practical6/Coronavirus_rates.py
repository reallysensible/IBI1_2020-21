# a frequency dictionary
my_dict = {}
Total_Cases = {'USA' :29862124, 'India' :11285561, 'Brazil' :11205972, 'Russia' :4360823, 'UK' :4234924}

# a pie chart from the frequency table
# TIP: try the 'pyplot.pie' function in matplotlib

# use figure
import matplotlib.pyplot as plt
import numpy as np
# dict to list
labels=list(Total_Cases.keys())
sizes=list(Total_Cases.values())

cmap = plt.get_cmap("terrain")
colors = cmap([1, 20, 40, 60, 80])

fig, ax = plt.subplots()
ax.pie(sizes, autopct='%1.1f%%', shadow=False, startangle=90,colors=colors)
# legend
for ax in [ax]:
    ax.legend(labels,
            title="Countries",
            loc="center left",
            bbox_to_anchor=(1,0,0.5,1))
# set_title
    ax.set_title("Coronavirus Infection")

plt.show()
