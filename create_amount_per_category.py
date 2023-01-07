import requests
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
plt.style.use("dsheep_gray")
import seaborn as sns

def create():
    response = requests.get('http://34.127.13.199:8000/log/this_month/per_category')
    print(response.json())  # レスポンスのjsonをdict化して返


    # Prepare Data
    df = pd.DataFrame.from_dict(response.json(), orient="index")

    # Draw Plot
    fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))

    data = df[0]
    categories = df.index

    df.sort_values(0, inplace=True)

    # Draw plot
    fig, ax = plt.subplots()
    ax.hlines(y=df.index, xmin=11, xmax=26, color='gray', alpha=0.7, linewidth=1, linestyles='dashdot')
    ax.scatter(y=df.index, x=df[0], s=75, alpha=0.7)


    # Title, Label, Ticks and Ylim
    ax.set_title('Amount per category')
    ax.set_xlabel('Total amount')
    ax.set_yticks(df.index)
    ax.set_yticklabels(df.index, fontdict={'horizontalalignment': 'right'})
    ax.set_xlim(0, math.ceil(df[0].max()/10000)*10000)
    plt.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.9)
    plt.savefig('amount_per_category.png')