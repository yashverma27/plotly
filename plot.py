
from turtle import color
from flask import Flask, render_template,request
import flask
import plotly
import plotly.graph_objs as go
import jinja2

import pandas as pd
import numpy as np
import json


app=Flask(__name__, template_folder='C:/Users/vermyas/OneDrive - Baker Hughes/Pictures/jinjs/',static_url_path='/static')

@app.route('/')
# def index():
#     feature='bar'
#     bar=create_plot(feature)
#     return render_template('index.html',plot=bar)

def create_plot():
    # if feature=='bar':
    labels=['c1','c2','c3','c4','c5','c6','c7','c8','c9']
    values=[20,32,25,42,121,234,543,88,432]
    
    df=pd.DataFrame({'x':labels,'y':values})
    mean=sum(values)/len(values)
    
    graphs = [
        dict(
            data=[
                dict(
                    x=df['x'],
                    
                    y=df['y'],
                    type='bar'
                ),

            ],
            layout=dict(
                title='first graph',
                paper_bgcolor='black',
                plot_bgcolor='black',
                
        
                
                

            )
        ),
    
        dict(
            data=[
                dict(
                    x=[1, 3, 5],
                    y=[10, 50, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='second graph',
                paper_bgcolor='black',
                plot_bgcolor='black'
                
            )
        )
    ]
       
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    print(ids)
    
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    # print(graphJSON)

    return render_template("render.html",ids=ids,graphJSON = graphJSON,mean=mean)

   

if __name__=='__main__':
    app.run(port=8080)


    

