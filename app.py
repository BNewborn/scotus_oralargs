import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()

df = pd.read_pickle("master_df")
doc_topics  = df.drop(axis=1,labels=['x','y','cluster']).set_index('index')

def get_top_topics(case):
    return pd.DataFrame(doc_topics.T[case].nlargest(5))

def generate_table(dataframe, max_rows=5):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +


        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )



app.layout =html.Div(children=[
    html.H1(children='t-SNE SCOTUS ORAL ARGUMENTS'),
    html.Div([
    dcc.Graph(
        id='scatter',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['index'] == i]['x'],
                    y=df[df['index'] == i]['y'],
                    text=df[df['index'] == i]['index'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'color': df[df['index'] == i]['color'],
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df['index'].unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10,'pad':4},
                showlegend=False,
                # title = 't-SNE Plot - SCOTUS Oral Arguments',
                # legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
, #end of scatter div

    #THIS GUY CAN BE ALLOWED BACK WHEN WE FIGURE OUT HOW THE FUCK TO WORK WITH A GODDAMN Table
    #FUCK YOU Table


    # html.Div(children=[
    #             html.H4(children='Case Topics',id='table_topics'),
    #             generate_table(doc_topics.T)
    #          ]
    #
    #         )

])

# @app.callback(
#     dash.dependencies.Output('table_topics','children'),
#     [dash.dependencies.Input('scatter','hoverData')]
#     )
# def update_table(hoverData):
#     # print(hoverData['points'][0]['text'])
#     case = hoverData['points'][0]['text']
#     doc_topics_new = doc_topics[case]
#     print(get_top_topics(case))
#     return doc_topics_new

if __name__ == '__main__':
    app.run_server(debug=True)
