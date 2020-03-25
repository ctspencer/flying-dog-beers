import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
import plotly.graph_objs as go

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])


if __name__ == '__main__':
    app.run_server()
