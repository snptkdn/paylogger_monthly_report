import requests
import os
import datetime
import math
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")
import seaborn as sns

def create():
    # Prepare Data
    responses = requests.get('http://34.127.13.199:8000/log/this_month/per_day')
    print(responses.json())  # レスポンスのjsonをdict化して返
    dict_day = {}
    count = 0
    for k,v in responses.json().items():
        dict_day[count] = [k, v]
        count += 1

    df = pd.DataFrame(dict_day).T
    df[0] = pd.to_datetime(df[0])
    df.sort_values(0, inplace=True)
    df.reset_index(inplace=True)
    print(df)

    x = np.arange(df.shape[0])
    y_returns = df[1]
    y_returns = np.array(y_returns, dtype=float)
    print(x)
    print(y_returns)

    # Plot
    plt.fill_between(x[0:], y_returns[0:], 0, where=y_returns[0:] >= 0, facecolor='green', interpolate=True, alpha=0.7)

    # Decorations
    xtickvals = [str(d) + "(" + str(w).upper()[:3] + ")" for d,w in zip(df[0].dt.day, df[0].dt.day_name())]
    plt.gca().set_xticks(x[::1])
    plt.gca().set_xticklabels(xtickvals[::1], rotation=90, fontdict={'horizontalalignment': 'center', 'verticalalignment': 'center_baseline'})
    plt.ylim(0, math.ceil(df[1].max()/10000)*10000)
    plt.xlim(0,x[-1])
    plt.title("Amount per day")
    plt.ylabel('Total Amount')
    plt.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.9)

    plt.savefig("amount_per_day.png")
