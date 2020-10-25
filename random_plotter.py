#Imprting libraries
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from random import randint
import plotly.express as px

# Creating dash environment
app = Dash(__name__)

# Constructing the layout
app.layout = html.Div([
    # Title
    html.Div(dcc.Markdown("Random number plotter"), style={"textAlign":"center", 'font-size':'300%'}),
    # Num. of point selection area, our N
    html.Div(["Number of points: ", dcc.Input(id='number_of_pts', value=100, type='number', min=1, style={'height': '25px', 'width':'100px'})], style={'padding-left':'80px', 'padding-top':'30px', 'display': 'inline-block', 'font-size':'150%'}),
    # Max range selection area, our K
    html.Div(["Max range: ", dcc.Input(id='upper_bound', value=100, type='number', min=1, style={'height': '25px', 'width': '100px'})], style={'padding-left': '50px', 'display': 'inline-block', 'font-size':'150%'}),
    # Our scatter plot
    dcc.Graph(id='random_graph', style={'height':'800px'}),
    # Title for the selected data area
    html.Div([dcc.Markdown("Selected points: ", style={'padding-left':'80px', 'font-size':'200%'})]),
    # Selected data area
    html.Div(html.Pre(id='selected_data', style={'border': 'thin lightgrey solid', 'overflowY': 'scroll', 'font-size':'200%'}), style={'width':'90%', 'padding-left':'80px'})])

# Callback function for number of points and range selection
@app.callback(
    Output("random_graph", "figure"),
    [Input("number_of_pts", "value"),
     Input("upper_bound", "value")])
def update_graph(number_of_pts, max_range):
    if(number_of_pts and max_range != None):  # Check whether arguments are null
        A_array = []
        for i in range(number_of_pts):
            A_array.append(randint(1, max_range))
        fig = px.scatter(y=A_array, labels={"x":"index", "y":"value"})
        fig.update_layout(showlegend=False)
        return fig       # return updated scatter plot
    return px.scatter()  # Return empty scatter plot

# Callback function for graph selection
@app.callback(
    Output("selected_data", "children"),
    [Input("random_graph", "selectedData")])
def update_selecteData(data):
    try:
        data = data["points"]
        print(data)
        points = []
        for point in data:
            points.append("Index: {}, Value: {} \n".format(point["x"], point["y"]))  # Make a string list of selected data, from Indexes and Values
        return points
    except:
        return ""

# Run Dash app
app.run_server()
