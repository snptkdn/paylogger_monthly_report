import requests
import datetime
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")
import seaborn as sns
import matplotlib.lines as mlines

today = datetime.date.today()
response = requests.get('http://34.127.13.199:8000/log/month/per_category?month=' + str(today.month))
# Import Data
# Prepare Data
df = pd.DataFrame.from_dict(response.json(), orient="index")
print(df)

left_label = [str(c) + ', '+ str(round(y)) for c, y in zip(df.index, df[0])]
right_label = [str(c) + ', '+ str(round(y)) for c, y in zip(df.index, df[0])]
klass = ['red' if (y1-y2) < 0 else 'green' for y1, y2 in zip(df[0], df[0])]

# draw line
# https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib/36479941
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='red' if p1[1]-p2[1] > 0 else 'green', marker='o', markersize=6)
    ax.add_line(l)
    return l

fig, ax = plt.subplots(1,1,)
str_color = "#595959"

# Vertical Lines
ax.vlines(x=1, ymin=500, ymax=13000, color=str_color, alpha=0.7, linewidth=1, linestyles='dotted')
ax.vlines(x=3, ymin=500, ymax=13000, color=str_color, alpha=0.7, linewidth=1, linestyles='dotted')

# Points
ax.scatter(y=df[0], x=np.repeat(1, df.shape[0]), s=10, color=str_color, alpha=0.7)
ax.scatter(y=df[0], x=np.repeat(3, df.shape[0]), s=10, color=str_color, alpha=0.7)

# Line Segmentsand Annotation
for p1, p2, c in zip(df[0], df[0], df.index):
    newline([1,p1], [3,p2], color=str_color)
    ax.text(1-0.05, p1, c + ', ' + str(round(p1)), horizontalalignment='right', color=str_color, verticalalignment='center', fontdict={'size':14})
    ax.text(3+0.05, p2, c + ', ' + str(round(p2)), horizontalalignment='left', color=str_color, verticalalignment='center', fontdict={'size':14})

# 'Before' and 'After' Annotations
ax.text(1-0.05, 13000, 'BEFORE', horizontalalignment='right', color=str_color, verticalalignment='center', fontdict={'size':18, 'weight':700})
ax.text(3+0.05, 13000, 'AFTER', horizontalalignment='left', color=str_color, verticalalignment='center', fontdict={'size':18, 'weight':700})

# Decoration
ax.set_title("Slopechart: Comparing GDP Per Capita between 1952 vs 1957")
ax.set(xlim=(0,4), ylim=(0,30000), ylabel='Mean GDP Per Capita')
ax.set_xticks([1,3])
ax.set_xticklabels(["1952", "1957"])
plt.yticks(np.arange(500, 13000, 2000))

# Lighten borders
plt.grid(False)
plt.subplots_adjust(left=0.15, bottom=0.1, top=0.85, right=0.9)
plt.savefig('amount_compair.png')


