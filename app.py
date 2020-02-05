import os
from pathlib import Path
import dash
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import pandas as pd
import base64
import pandas as pd
#import lorem
import numpy as np
from scipy.stats import norm
import json
from scipy.stats import norm
import copy
import csv
import plotly.express as px
from collections import deque
import xarray as xr
from scipy.stats import norm

# from BOBfun import rose



############################################################################################################################################################

#################################################### TOKEN
mapbox_access_token = "pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w"
Style="mapbox://styles/seb2121/ck0goela506jn1cpi74entuub"
Style="outdoors"
mapbox = dict(
accesstoken = mapbox_access_token,
style =Style
)

#################################################### color

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

## Colours
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"




scl = [0,"rgb(255,0,0)"],[0.125,"rgb(255, 111, 0)"],[0.25,"rgb(255, 234, 0)"],\
[0.375,"rgb(151, 255, 0)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(0, 152, 255)"],\
[0.75,"rgb(0, 25, 255)"],[0.875,"rgb(0, 0, 200)"],[1,"rgb(150, 0, 90)"]

Pic_One = os.path.dirname(os.path.abspath(__file__))

def encode_image(PicName):
    PicDIR= os.path.join(Pic_One, "Picture", PicName+".png")
    encoded = base64.b64encode(open(PicDIR, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())



BasicStyle={
                'padding-top': 20,
                'padding-bottom': 20,
                "height": "400px",
                }

Sliderstyle= {
                "height": "50px",
               # 'margin-top': 25,
               # 'margin-bottom': 50,
                 'padding-top':30,
                 'padding-bottom': 30,
               #  'padding-left': "5%",
               #  'width':"50%",
               #  'float': 'hfgh',
}


######################### navbar


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("CSIR", href="https://www.csir.co.za/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="/info"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
        ],
    brand="Wind Energy Calculator",
    brand_style={'font-size': 35},
    brand_href="#",
    color="primary",
    dark=True,)





######################### Table


table_header = [html.Thead(html.Tr([html.Th("Turbine",), html.Th("Max Power Output"), html.Th("Class"), html.Th("Design for")],style={"text-align": "center"}))]

row1 = html.Tr([html.Td("Turbine 1"),html.Td("2.7 MW"), html.Td("Class 3"), html.Td("Low Wind")])
row2 = html.Tr([html.Td("Turbine 2"),html.Td("2.78 MW"), html.Td("Class 3"), html.Td("Low Wind")])
row3 = html.Tr([html.Td("Turbine 3"),html.Td("3 MW"),html.Td("Class 3"), html.Td("Low Wind")])
row4 = html.Tr([html.Td("Turbine 4"),html.Td("3 Mw"), html.Td("Class 2"), html.Td("medium Wind")])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body,striped=False, bordered=True, hover=True,)



######################### Text Instructions One


Text_Instructions_one =  html.Div([
        # html.H1(children='Wind Energy Calculator',),


        dbc.Jumbotron([    html.H3(children='Instructions', ),
                            html.P(children="The map of South Africa displays an estimated capacity factor or wind power of a "
                                            "specific turbine over a year at a particular height. The data entered below will "
                                            "be plotted on the map."),
                            html.Ol([
                                html.Li(children="Select one of the four turbine options (the different turbines with their "
                                                 "corresponding maximum power outputs are displayed in the table below to the"
                                                 " left)."),
                                html.Li(children="Select one of the four required hub heights."),
                                html.Li(children="Select the type of estimate required, namely capacity factor or wind power."),
                                html.Li(children="To submit the requirements, click the “Plot” button."),],),

                            html.P(children="The card to right of the selection criteria displays an estimate of the capacity "
                                            "factor and wind power at a specific point selected on the map."),
        ])
    ],)


######################### Text GenWind

Text_GenWind =  html.Div([
    dbc.Jumbotron([
        html.H4(children='Power Graph and Rose Chart Display', ),
        html.P(children='Further analysis of the selected point on the map of South Africa is displayed in the power '
                        'graph and rose chart. The selection can be customised using the drop-down menus for hub '
                        'height(s) and turbine(s). This allows for a graphic represent of each of the selected '
                        'criteria.'),
        html.P(children='A normal distribution for each of the hub height’s selected is plotted on the graph. The axis '
                        'on the left estimates the wind probability density percentages based on time series data '
                        'collected. Power curves are plotted over the normal distribution graphs from the turbine '
                        'selections made. The power curve(s) are linked to the right axis and are displayed as power '
                        'generated (kW).'),
        html.P(children='The rose chart to the right of the graph represents the wind direction as a percentage based '
                        'on the hub height(s) selected.'),

        ])
    ],)

######################### Text Three

Text_Method =  html.Div([
                dbc.Jumbotron([
                    html.H4(children='Method', ),
                    html.P(children='Wind data from January 2009 to December 2013 was collected using NetCDF files at '
                                    'four heights above the ground (50m, 80m, 100m and 150m). The data was used to '
                                    'determine annual hourly wind speeds at each of the four heights. Data results at '
                                    'each height were then converted into a probability density function to create a '
                                    'normal distribution. Together with power curve data for various existing wind '
                                    'turbines, the power output was calculated to estimate the capacity factor and '
                                    'amount of energy that can be produced in a year at the different heights within '
                                    'each 5x5km2 pixel for different turbines'),
                    html.P(children=''),
                    html.P(children='We would like to improve the app and include more types of turbines. Please refer '
                                    'to the block in the top right and select whether you would like to add these and'
                                    ' more turbines to the app or/and if you would prefer to include your own turbine '
                                    'information. Should you prefer to include your own turbines please indicate how '
                                    'this data will be supplied e.g. raw data or an equation.'),


                                ])
                        ],)

Info_mine =  html.Div([

                    html.P(children='This project was done in collaboration with GIZ.'),
                    html.P(children=''),
                    html.P(children='For more information please contact:'),
                    html.P(children="Sebastian Leask (sleask@csir.co.za)")

                        ],)

######################### Picture


Picture_CSIR= html.Div([
                    dbc.Container(
                        html.Img(src=encode_image("one"),

                        style={

                            'margin-top': 0,
                            'margin-right': 10,


                        },)
                                )
                    ])

Picture_Talbe= html.Div([
                    html.Div(
                        html.Img(src=encode_image("Table"),

                        style={
                            'height': '30%',
                            'width': '85%',
                            'float': 'left',
                            'position': 'relative',
                            'margin-top': 10,
                            'margin-right': 0,
                            'display': 'inline-block',
                            'padding-top': 20,

                            },
                         )
                        )
                    ])

Picture_GIZ= html.Div([
                    html.Div(
                        html.Img(src='https://raw.githubusercontent.com/Futile21/heroku4/master/Picture/GIZ%20Cooperation%20logo.png?token=AMQTZBRNK5IX5F25EAY7NLS6HM2GY',

                        style={
                            # 'height': 150,
                            # 'width': 500,
                            # 'height': '5%',
                            'width': '40%',
                            'float': 'left',
                            'position': 'relative',
                            'margin-top': 10,
                            'margin-right': 0,
                            'display': 'inline-block',
                            'padding-top': 20,

                            },
                         )
                        )
                    ])




######################################################### Dropdown

Dropdown_Height= html.Div([
             dcc.Dropdown(
                    id='DropdownHeight',
                    options=[
                        {'label': '50m', 'value': "50", },
                        {'label': '80m', 'value': "80", },
                        {'label': '100m', 'value': "100", },
                        {'label': '150m', 'value': "150", }, ],
                    value=['50'],

                    multi=True,
                    ),
            ],)

Dropdown_Turb= html.Div([
             dcc.Dropdown(
                    id='DropdownTurb',
                    options=[
                        {'label': 'Turbine 1', 'value': "Turbine 1", },
                        {'label': 'Turbine 2', 'value': "Turbine 2", },
                        {'label': 'Turbine 3', 'value': "Turbine 3", },
                        {'label': 'Turbine 4', 'value': "Turbine 4", }, ],
                    value=['Turbine 1'],

                    multi=True,
                    ),
            ],)

######################################################### Radio

Radio = html.Div([
                html.Div([html.H4(children='Selection Criteria',)]),
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            dbc.RadioItems(
                                id='RadioTurb',
                                options=[
                                    {'label': 'Turbine 1', 'value': "Turbine 1", },
                                    {'label': 'Turbine 2', 'value': "Turbine 2", },
                                    {'label': 'Turbine 3', 'value': "Turbine 3", },
                                    {'label': 'Turbine 4', 'value': "Turbine 4", }, ],
                                value='Turbine 1',
                                inline=True,

                            ),],
                            style=Sliderstyle
                            ),width={"size": 10, "offset": 1},
                        )
                    ],align="center",),
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            dbc.RadioItems(
                                    id='RadioHeight',
                                options=[
                                    {'label': '50m', 'value': "50", },
                                    {'label': '80m', 'value': "80", },
                                    {'label': '100m', 'value': "100", },
                                    {'label': '150m', 'value': "150", }, ],
                                value='50',
                                inline=True,

                            ), ],

                            style=Sliderstyle
                            ),width={"size": 10, "offset": 1},
                        )
                    ],align="center",),
                dbc.Row([
                    dbc.Col(
                        html.Div([
                                dbc.RadioItems(
                                        id='RadioPower',
                                        options=[
                                            {'label': 'Capacity Factor', 'value': "Capacity Factor [%]", },
                                            {'label': 'Wind Power', 'value': "Wind Power [MWh/year]", }, ],
                                        value='Capacity Factor [%]',
                                        inline=True,

                                ),
                                ]),
                        width={"size": 8, "offset": 1},
                        ),
                    dbc.Col(
                        html.Div([dbc.Button("Plot", color="primary", className="mr-1",id='btn'),],
                                 style=Sliderstyle
                                ),
                        width={"size": 2, },
                            ),
                    ],align="center",),


            ],)

######################### CARD

InfoCard = html.Div([
            dbc.Card([
                dbc.CardHeader(id="cardHeader"),
                dbc.CardBody(
                    [html.Div([
                        html.H5(children="Test", className="card-title", id="cardmidT"),
                        html.H5(children="Test2", className="card-text", id="cardmidM"),
                            ],),
                        ],
                   # style={"height": "125px",},
                   # align="center",
                    ),
                dbc.CardFooter(
                    [html.Div([
                        html.P(children="", className="card-title", id="cardLat"),
                        html.P(children="", className="card-text", id="cardLon"),
                            ],),
                        ],
                               ),
            ],
            outline=True,
            color="dark",)
            ],)







############################################################################################################################################################  Comp


RSAlayout=dict(
                autosize=True,
                margin=go.layout.Margin(l=0, r=35, t=35, b=0,),
                colorbar=dict(title="Colorbar",),
                title="South Africa Overview",
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    center=dict(lat=-28, lon=22),
                    style=Style,
                zoom=4,),)



Roselayout=dict(
            title='Wind Speed Distribution',
            font_size=16,
            legend_font_size=16,
            polar_radialaxis_ticksuffix='%',
            orientation=90,
            )




Powelayout = dict(
            annotations=[
                {
                    "y": -0.1,
                    "text": "Wind speed (m/s)",
                    "arrowhead": 7,
                    "ax": 0,
                    "ay": -40,
                    "font": {"size": 15},
                    "showarrow": False,
                    "xref": "paper",
                    "yref": "paper",
                    "visible": True,
                }
            ],
            autosize=True,
            dragmode="pan",
            hovermode="closest",
            legend={
                "x": 0.5,
                "y": -0.1,
                "font": {"size": 15},
                "orientation": "h",
                "xanchor": "center",
                "bgcolor": "rgb(255, 255, 255, 0)",
                },
            title="Normal distribution of Wind Vs Turbine Power",
            xaxis={
                # "title": "Wind speed (m/s)",
                "autorange": True,
                "nticks": 19,
                #    "range": [0.5, 18],
                "showgrid": True,
                "tickfont": {
                    "color": "rgb(68, 68, 68)",
                    "size": 1,
                },
                "ticks": "",
                "type": "linear",
                "zeroline": True,
            },
            yaxis={
                "title": "Probability (%)",
                "title_font_size": 30,
                "autorange": True,
                "linecolor": "rgb(190, 191, 192)",
                "mirror": True,
                "nticks": 9,
                "range": [0, 1],
                "showgrid": True,
                "showline": True,
                "side": "left",
                "tickfont": {
                    "color": "rgb(68, 68, 68)",
                    "size": 9,
                },
                "ticks": "outside",
                "ticksuffix": " ",
                "type": "linear",
                "zeroline": False,

            },
            yaxis2={
                "title": "Power Generated (kW)",
                "anchor": "x",
                "autorange": True,
                "exponentformat": "e",
                "linecolor": "rgb(190, 191, 192)",
                "nticks": 9,
                "overlaying": "y",
                #  "range": [0, 50],
                "showgrid": True,
                "side": "right",
                "tickfont": {"size": 9},
                "tickprefix": " ",
                "ticks": "outside",
                "type": "linear",
                "zerolinecolor": "rgb(190, 191, 192)",
            },)

Roselayout=go.Layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    ticksuffix='%',),
                ),
            showlegend=True,
            polar_angularaxis_rotation=90,)


############################################################################################################################################################  Data

# da=xr.open_mfdataset(r"C:\AllRun\*10.nc",combine='by_coords')
# da=xr.open_dataset(r'C:\Users\\futil\OneDrive\GIZ\Internship\seb_test_ring\\rose\maker\AllCoTurb.nc')

WindDF=pd.read_csv('https://raw.githubusercontent.com/Futile21/CSV_wind/master/Test_CF003.csv')
RoseDF=pd.read_csv('https://raw.githubusercontent.com/Futile21/CSV_wind/master/Test_Rose003.csv')
TurbDF = pd.read_csv("https://raw.githubusercontent.com/Futile21/CSV_wind/master/PowerTurb4.csv")

xspace = np.linspace(-0.0, 25, 100)
NamesDir=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]







MapData = [
       go.Scattermapbox(
           lat=WindDF['lat'],
           lon=WindDF['lon'],
           mode="markers",
           # hoverinfo=df['loc'].astype(str) + ' inches',
           # text=[i for i in list_of_locations],
           text=np.array(WindDF['CF-Turbine 1-50']).flatten(),
           marker=dict(
               color=np.array(WindDF['CF-Turbine 1-50']).flatten(),           ################ LINK
               colorscale=scl,
               reversescale=True,
               opacity=0.35,
               size=8,
               colorbar=dict(
                   # title=PowerType,
                   titlefont=dict(size=18,family="Arial"),
                   titleside="right",
                   outlinecolor="rgba(68, 68, 68, 0)",
                   ticks="outside",
                   showticksuffix="last",
                   tickmode="auto",
               ),
           ),
       ),
   ]


############################################################################################################################################################  HTML part


MapRSA= html.Div(
    [dcc.Graph(id="MapRSA",figure=dict(data=MapData,layout=RSAlayout))],
    style={
            #'padding-top': 20,
            'padding-bottom': 20,},
    )

RoseColour = ['rgb(18, 0, 57)', 'rgb(77, 0, 153)', 'rgb(102, 0, 204)', 'rgb(128, 0, 255)', 'rgb(153, 51, 255)']
Names=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]


############            ############            ############

# WSPD=da.sel(time=slice('2010-10','2010-11'))['WSPD']
# WDRO=da.sel(time=slice('2010-10','2010-11'))['WDRO']
# x=rose(1, WSPD, WDRO)
#
#
# ############
#
# Rosetraces = []
# cont = 0
# for j in reversed(list(x["50"].keys())):
# #         print(j)
# #         print(x[i][j])
#
# #         print("")
#     Rosetraces.append(
#         go.Barpolar(
#                     r=x["100"][j],
#                     name=f'Greater {j} m/s',
#                     marker_color=RoseColour[cont],
#                     theta=Names,
#                         ),
#     )
#     cont+=1
#
# Names=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]

rose = html.Div([
    dcc.Graph(
        id='rose-graph',
        # figure={
        #         'data':Rosetraces,
        #         'layout': Roselayout
        # }
    )
])

############            ############            ############

PowerGraph = html.Div([
    dcc.Graph(
        id='power-graph',
    )
])


figurePOwer = html.Div([
    dcc.Graph(
        id='figurePOwer-graph',

    )
])


############################################################################################################################################################  HTML Layout


layout1 = html.Div([

                    html.Div([navbar]),

##      Text_Instructions_one
                    html.Div(
                        dbc.Row([
                            dbc.Col(dbc.Container([
                                Text_Instructions_one, ]),
                                md=9,
                                sm=9,
                            ),
                            dbc.Col(
                                Picture_CSIR,
                                md=3,
                                sm=3,
                            ),
                        ]),
                    ),

##      Radio and InfoCard
                    html.Div(
                        dbc.Row([
                            dbc.Col(dbc.Jumbotron(
                                Radio, ),
                                md=6,
                                sm=12,
                                width={"offset": 1},
                            ),
                            dbc.Col(
                                InfoCard,
                                md=2,
                                sm=6,
                                align="center",
                                width={"offset": 1},

                            ),

                        ])
                    ),

##      Map of RSA
                    html.Div(
                        dbc.Row([
                            dbc.Col(dbc.Container([MapRSA]),
                                md=12,
                                sm=12,
                                align="center",
                                    ),
                        ]),
                    ),


##      H4 Generalized Wind Climate
                    html.Div(
                            dbc.Row([
                                dbc.Col(html.H4('Generalized Wind Climate'),
                                        align="center",
                                        width=3,
                                        ),
                            ],
                            justify="center",),
                        style = {'padding-bottom': 20,},
                        ),

##      Dropdown
                    html.Div(
                        dbc.Row([
                            dbc.Col(dbc.Container(
                                Dropdown_Height, ),
                                md=4,
                                sm=4,
                                align="center",
                                width={"offset": 2},

                            ),
                            dbc.Col(dbc.Container(
                                Dropdown_Turb, ),
                                md=4,
                                sm=4,
                                align="center",
                                # width={"offset": 2},

                            ),

                        ])

                    ),

##      Power Graph and Rose

                    html.Div(
                            dbc.Row([
                                    dbc.Col(dbc.Container(
                                        PowerGraph,),
                                        md=7,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        rose,
                                        md=4,
                                        sm=6,
                                        align="start",
                                    ),

                                ],no_gutters=True,)
                    ),

##      Picture_GIZ and Info_mine
                    html.Div(
                        dbc.Row([
                            dbc.Col(
                                Picture_GIZ,
                                md=6,
                                sm=6,
                            ),
                            dbc.Col(
                                Info_mine,
                                md=6,
                                sm=6,
                            ),
                        ])
                    ),

                ])


layout2 = html.Div([

##      Opt 1
                html.Div(
                        dbc.Row([
                            dbc.Col(
                                html.H3('Opt 1'),
                                md=11,
                                sm=11,
                            ),
                            dbc.Col(
                                    dcc.Link('Go to App', href='/'),
                                    md=1,
                                    sm=1,
                            ),
                        ]),
                    ),

##      Text_Method
                html.Div(
                    dbc.Row([
                        dbc.Col(
                            Text_Method,
                            md=12,
                            sm=12,
                        ),
                    ]),
                ),

##      table and Pic
                html.Div(
                    dbc.Row([
                        dbc.Col(
                            html.Div(
                                table,
                            ),
                            md=4,
                            sm=12,
                            align="center",
                            width={"offset": 1},

                        ),
                        dbc.Col(
                            html.Div(
                                Picture_Talbe),
                            md=7,
                            sm=12,
                        ),
                    ]),
                ),

##      Text_GenWind
                html.Div(
                    dbc.Row([
                        dbc.Col(
                            Text_GenWind,
                            md=12,
                            sm=12,
                        ),
                    ]),
                ),

            ])



############################################################################################################################################################  App


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.themes.GRID])
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

############################################################################################################################################################  Callback


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layout1
    elif pathname == '/info':
        return layout2
    else:
        return '404'



################################ CARD TOP

@app.callback(Output("cardHeader", "children"),
            [Input("RadioTurb", "value"),
             Input("RadioHeight", "value")
             ],)
def locDATA1(Turb,Height):
    return f"{Turb} at {Height}m"


################################ CARD MID

@app.callback(Output("cardmidT", "children"),
           [Input("MapRSA", "clickData"),
            Input("RadioTurb", "value"),
            Input("RadioHeight", "value"),
            ],)
def locDATA2(clickData,Turb,Height):
    if clickData is None:
        return ""
    else:
        ID = clickData['points'][0]['pointIndex']

    # CF= np.array(da["CF"].sel(ID=ID,Turb=Turb,hgt=int(Height)))
    CF=np.array(WindDF[(WindDF['ID'] == ID)]['CF-'+Turb+'-'+Height]).flatten()

    return ("CF is "+str(CF)+" %")

@app.callback(Output("cardmidM", "children"),
            [Input("MapRSA", "clickData" ),
             Input("RadioTurb", "value"),
             Input("RadioHeight", "value"),
             ],)
def locDATA3(clickData,Turb,Height):
    if clickData is None:
        return "please Click on the Map"
    else:
        ID = clickData['points'][0]['pointIndex']

    POWER=np.array(WindDF[(WindDF['ID'] == ID)]['WindPower-'+Turb+'-'+Height]).flatten()

    POWER_round = str(round(float(POWER), 1))
    return ("Power is " + str(POWER_round)+" MWh per year")


################################ CARD BOTTOM

@app.callback(Output("cardLat", "children"),
            [Input("MapRSA", "clickData" )],)
def locDATA4(clickData):
    if clickData is None:
        return ""

    else:
        XLAT = clickData['points'][0]['lat']
        XLONG = clickData['points'][0]['lon']

    lat =str( XLAT)

    lat1 = lat[1:3];lat2 = lat[4:6];lat3 = lat[6:8]
    LatSplt=lat1+"\N{DEGREE SIGN}"+lat2+u"\u2032"+lat3+u"\u2033S"

    return ("Latitude "+LatSplt)

@app.callback(Output("cardLon", "children"),
            [Input("MapRSA", "clickData" )],)
def locDATA4(clickData):
    if clickData is None:
        return ""

    else:
        XLAT = clickData['points'][0]['lat']
        XLONG = clickData['points'][0]['lon']

    long =str( XLONG)

    long1 = long[0:2];long2 = long[3:5];long3 = long[5:7]
    LongSlt=long1+"\N{DEGREE SIGN}"+long2+u"\u2032"+long3+u"\u2033E"
    return ("Longitude " + LongSlt)


################################ Power Graph

@app.callback(Output('power-graph', 'figure'),
            [
                Input("MapRSA", "clickData"),
                Input("DropdownTurb", "value"),
                Input("DropdownHeight", "value"),
                ])
def update_figurePower(clickData,DropdownTurb,DropdownHeight):

    if clickData is None:
        ID=0
    else:
        ID = clickData['points'][0]['pointIndex']

    PowerTraces = []
    for Height in DropdownHeight:

        loc = float(np.array(WindDF[(WindDF['ID'] == ID)]['loc-'+Height]))
        scale = float(np.array(np.array(WindDF[(WindDF['ID'] == ID)]['scale-'+Height])))

        PowerTraces.append(
                go.Scatter(
                    x=xspace,
                    y=norm.pdf(xspace, loc=float(loc), scale=float(scale)),
                    name=Height+" m",
                    )
            )

    for Turbtype in DropdownTurb:


        PowerTraces.append(
                go.Scatter(
                    x=np.array(TurbDF['Speed']),
                    y=np.array(TurbDF[Turbtype]),
                    name="Turbine Power Curve",
                    yaxis="y2",
                    )
                )

    figure = dict(data=PowerTraces,layout=Powelayout)
    return figure


################################ rose Graph

@app.callback(Output('rose-graph', 'figure'),
            [Input("MapRSA", "clickData"),
             Input("DropdownHeight", "value"),])
def update_figureRose(clickData,DropdownHeight):

    if clickData is None:
        ID = 0
    else:
        ID = clickData['points'][0]['pointIndex']

    RoseTraces=[]
    for Height in DropdownHeight:
        Dir = list(map(lambda x: x + "-" + Height, NamesDir))
        Dir.append(Dir[0])
        rose = np.array(RoseDF[(RoseDF['ID'] == ID)][Dir]).flatten()
        Names = NamesDir
        Names.append(Names[0])

        RoseTraces.append(
            go.Scatterpolar(r=rose, theta=Names, fill='toself', name=Height+' m'))

    figure = dict(data=RoseTraces,layout=Roselayout)
    return figure


server = app.server


if __name__ == '__main__':
    app.run_server()










































