import plotly.figure_factory as pf
import csv as c
import statistics as s
import pandas as pd
import random as r
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

data = df['temp'].tolist()

population = s.mean(data)
print('the mean of the data is {}'.format(population))

stdv = s.stdev(data)
print('the standard deviation for the data is {}'.format(stdv))

fig = pf.create_distplot([data], ['temp'], show_hist=False)
fig.add_trace(go.Scatter(x = [population,population], y = [0,1]))
fig.show()


def randomSetOfName(ctx):
    dataset = []
    for i in range (0,ctx):
        randomindex = r.randint(0,len(data)-1)
        val = data[randomindex]
        dataset.append(val)

    mean = s.mean(dataset)
    return

def show_fig(meanlist):
    df = meanlist
    mean = s.mean(df)
    fig = pf.create_distplot([df], ['temp'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1]))
    fig.show()

def set():
    meanlist = []
    for i in range (0,1000):
        setofmean = randomSetOfName(100)
        meanlist.append(setofmean)
    show_fig(meanlist)
    mean  =  s.mean(meanlist)
    print(mean)

set()
