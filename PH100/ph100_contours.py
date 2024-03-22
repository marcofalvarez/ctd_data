import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px
import datetime

df = pd.read_excel('ph100_timeseries2014.xlsx', 'Sheet3')
df['date'] = df['TIME'].map(lambda x : x.replace("T", " ").split(" ")[0])
df["DOX2"].interpolate(method="linear", direction = "forward", inplace=True)
cf = pd.read_excel('ph100_timeseries2014.xlsx', 'Sheet2')
cf['date'] = cf['TIME'].map(lambda x : x.replace("T", " ").split(" ")[0])
fig = go.Figure(data =
    go.Contour(
        z=df.PSAL,
        x=df.date, # horizontal axis
        y=-df.DEPTH, # vertical axis
        line_smoothing=0.85,
        colorscale = 'Jet',
        # contours=dict(
        #     start=0,
        #     end=8,
        #     size=2,
        # ),
        contours = dict(
            showlabels = True,
            labelfont = dict(
                family = 'Raleway',
                color = 'white'
            )
        ),
        hoverlabel = dict(
            bgcolor = 'white',
            bordercolor = 'black',
            font = dict(
                family = 'Raleway',
                color = 'black'
            )
        )
    ))
fig.add_trace(
    go.Scatter(
        x=cf.date,
        y=-cf.MLD_CD06,
        mode="markers+lines",
        # name="steepest",
        line=dict(
            color="black"
        )
    )
)
fig.show()