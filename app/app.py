from dash import (
    Dash,
    html,
    dcc,
    Input,
    Output
)

from flask import Flask


def create_dash(server):

    app = Dash(__name__,
    server=server,
    url_base_pathname='/')

    app.layout=html.Div(
        [
            html.Div(
                [
                    html.H1("Header")
                ],
                className='grid-item single-header'
                ),
            html.Div(
                [
                    html.H3("Choose one or more Numbers"),
                    dcc.Dropdown(id="dropdown-selection",
                    options=[1,2,3,4,5],
                    multi=True,
                    ),
                    html.H3("Choose a Date"),
                    dcc.DatePickerSingle(id="date-selection",
                    min_date_allowed='2023-01-01',
                    max_date_allowed='2023-06-01',
                    ),
                    html.H3("Choose one or more Sport"),
                    dcc.Checklist(id="checklist-selection",
                    options=['Soccer','Basketball'],
                    ),
                    html.H3("What's your Name?"),
                    dcc.Input(id='input-string',
                    placeholder='Your Name',
                    ),
                    html.H3("How tall are you?"),
                    dcc.Slider(id="slider-selection",
                    min=4.5,max=7.5,step=.1,
                    marks={5:"5'",5.5:"5'6\"",6:"6'",6.5:"6'6\"",7:"Stop Lying"}
                    ),
                ],
                className='grid-item option-bar'
                ),
                html.Div(id="response-div",className='grid-item full-content')
            
        ],
        className='grid-container'
    )

    @app.callback(
        Output('response-div','children'),
        Input('dropdown-selection','value'),
        Input('date-selection','date'),
        Input('checklist-selection','value'),
        Input('input-string','value'),
        Input('slider-selection','value'),
    )
    def make_content(numbers,date,sports,name,height):

        if ((numbers is not None)&
            (date is not None)&
            (sports is not None)&
            (name is not None)&
            (height is not None)
            ):

            ns = [str(i) for i in numbers]
            message = f"""
            Hi {name}, your favorite numbers are {', '.join(ns)} 
            and on {date} you will play {', '.join(sports)}. You are 
            {height} feet tall which is pretty cool.
            """

            return html.P(message)
        
        return html.P("Choose some choices!")


    return app

def create_app():
    server = Flask(__name__)
    app = create_dash(server=server)

    @server.route("/")
    def home():
        return app.index()
    
    return server

def main():
    app=create_app()
    app.run()
    return

if __name__=='__main__':
    main()