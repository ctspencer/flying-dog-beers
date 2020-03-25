import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
import plotly.graph_objs as go

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-nodes',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '1000px'},
        elements=[
            {'data': {'id': 'MThub', 'label': 'Major Topics'}, 'position': {'x': 225, 'y': 175}, 'grabbable': False},
            {'data': {'id': 'MT1', 'label': 'Multidisciplinary Initiatives'}, 'position': {'x': 75, 'y': 75}},
            {'data': {'id': 'MT2', 'label': 'Vulnerable Populations'}, 'position': {'x': 225, 'y': 275}},
            {'data': {'id': 'MT3', 'label': 'Education & Awareness'}, 'position': {'x': 375, 'y': 75}},
            {'data': {'source': 'MThub', 'target': 'MT1'}},
            {'data': {'source': 'MThub', 'target': 'MT2'}},
            {'data': {'source': 'MThub', 'target': 'MT3'}},
        ]
    )
])


if __name__ == '__main__':
    app.run_server()
