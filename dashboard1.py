import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import os

os.chdir(os.path.join(os.path.sep, 'home', 'tkokkeng', 'Documents', 'comfort-study'))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'white',
    'text': '#7FDBFF'
}

scale = .002

df = pd.read_csv(os.path.join('data', 'all_data.csv'))

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Building Electrical and Cooling Consumption',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='PWM/Area vs BTU/Area', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='PWM/Area vs BTU/Area vs Area',
            figure={
                'data': [
                    go.Scatter(
                        x=df.loc[df['Type'] == i]['BTU/Area'],
                        y=df.loc[df['Type'] == i]['PWM/Area'],
                        # text=df.loc[df['Type'] == i]['Building'] + '\nArea = '+ str(df.loc[df['Type'] == i]['GFA sqm']),
                        text=[i[0] + i[1] for i in zip(df.loc[df['Type'] == i]['Building'], df.loc[df['Type'] == i]['GFA sqm'].map(lambda x: 'Area = ' + str(x)))],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            # 'size': 15,
                            'size': df.loc[df['Type'] == i]['GFA sqm'] * scale,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in df.Type.unique()
                ],
                'layout': go.Layout(
                    # xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                    # xaxis={'title': 'BTU/Area'},
                    xaxis=go.layout.XAxis(title='BTU/Area', automargin=True),
                    # yaxis={'title': 'PWM/Area'},
                    yaxis=go.layout.YAxis(title='PWM/Area', automargin=True),
                    autosize=False,
                    width=1200,
                    height=800,
                    # margin={'l': 100, 'b': 40, 't': 10, 'r': 100},
                    legend={'x': 1, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)