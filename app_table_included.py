import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import numpy as np

import requests
import re
import gensim
from collections import defaultdict
from gensim import corpora, models
from gensim.similarities import MatrixSimilarity,SoftCosineSimilarity, SparseTermSimilarityMatrix
from gensim.corpora import Dictionary
from gensim.models import LsiModel


td = corpora.Dictionary.load('scratch_work/NLPScratch/brand_new_strains.dict')
m = LsiModel.load('scratch_work/NLPScratch/_fit_LSI_Model.model')
s_index = MatrixSimilarity.load('scratch_work/NLPScratch/strain_sim.index')
s_d_load = np.load('scratch_work/NLPScratch/strain_lookup_dict.npy').item()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Green-Rex: We Recommend It, You Smoke It!", style={'color' :'#008000', "textAlign": "center"}),
    
    html.Div([
        html.H2("Your words lead to your experience!"),
        dcc.Input(
            id='text-box',
            placeholder='What would you like to feel today?',
            type='text',
            value='',
            size=30),
        html.H2("Don't forget to set the number of strains to recommend!"), 
        dcc.Slider(
            id='strain-slider',
            min=2,
            max=10,
            step=1, 
            marks={2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10:'10'})
        ], className="vertical", style={'color' :'#008000', "textAlign": "center", "padding": 50, "width": "100%", "margin-left": "auto", "margin-right": "auto"}),
    dcc.Graph(id='results-slider-graph')
], className="container")

@app.callback(
    Output('results-slider-graph', 'figure'),
    [Input('text-box', 'value'),
     Input('strain-slider', 'value')])
def input_to_vec(text_box,strain_slider):
    vbow = td.doc2bow(text_box.lower().split())
    lsi = m[vbow]
    simimlarity = s_index[lsi]
    sims_sort = sorted(enumerate(simimlarity), key=lambda item: -item[1])
    top = sims_sort[:strain_slider]
    top_l =[]
    for i in top:
        top_l.append((s_d_load[i[0]],i[1]))
    names = []
    score = []
    for i in top_l:
        names.append((i[0][7:]))
        score.append(i[1])
    nu_names = []
    for i in names:
        new_i = re.sub('[-]', ' ', i)
        nu_names.append(new_i)
    #for i in score:
        #print('Recomendation Strength = {:.2%}'.format(i))

    return {
            'data': [go.Bar(
                x=score,
                y=nu_names,
                orientation = 'h', 
                marker = dict(
                    color = '#008000')
            )], 

            'layout':[go.Layout(
                margin=dict(
                        l=120,
                        r=10,
                        t=140,
                        b=80))]
        }

if __name__ == '__main__':
    app.run_server(debug=True)