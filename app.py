from dash import html, Dash, dcc, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import yfinance as yf

# Assuming get_data_from_yfinance and symbol_list are defined elsewhere
# from some_module import get_data_from_yfinance, symbol_list
symbol_list = ['TSLA', 'NVDA', 'AMD', 'META', 'BABA', 'SPY', 'QQQ']

app = Dash()


@app.callback(
    [Output(component_id='stock_plot', component_property='figure'),
     Output(component_id='data_table', component_property='data')],
    [Input(component_id='ticker_selection', component_property='value')]
)
def update_graph(ticker):
    dff = get_data_from_yfinance(ticker)
    fig = px.line(dff, x='Date', y='Close')
    fig.update_layout(
        plot_bgcolor='#D1C4E9',  # Light purplish background for the plot area
        paper_bgcolor='#E6B0AA',  # Light reddish-purple background for the surrounding area
        font=dict(color='#4B0082')  # Optional: Adjust the font color for better readability
    )
    dff = dff.sort_values('Date', ascending=False)
    columns = [{"name": i, "id": i} for i in dff.columns]
    data = dff.to_dict('records')
    return fig, data


def get_data_from_yfinance(ticker):
    data = yf.download(ticker, period='max', auto_adjust=True)
    data.reset_index(inplace=True)
    return data


background_style = {
    'backgroundColor': '#A1887F',  # Soft purplish background color
    'padding': '20px'  # Padding around the content
}

tab_style = {
    'backgroundColor': '#D1C4E9',  # Soft reddish-purple background color
    'padding': '20px',  # Padding around the tab content
    'border': 'none'
}

selected_tab_style = {
    'backgroundColor': '#E6B0AA',  # Soft purplish background color for selected tab
    'padding': '20px',  # Padding around the tab content
    'border': 'none'
}

data_table_style = {
    'backgroundColor': '#E6B0AA'  # Soft reddish-purple background color for the table
}

dropdown_style = {
    'backgroundColor': '#F8BBD0',  # Reddish-brown background color
    'color': '#4B2E2A',  # Text color
    'border': 'none',  # No border
    'padding': '10px',  # Padding inside the dropdown
    'font-size': '16px'  # Font size
}

graph_style = {'backgroundColor': '#E0F7FA'}

tabs = dcc.Tabs(children=[
    dcc.Tab(label='Chart', children=dcc.Graph(id='stock_plot', style=graph_style), style=tab_style,
            selected_style=selected_tab_style),
    dcc.Tab(
        label='Table',
        children=dash_table.DataTable(
            id='data_table',
            page_size=10,
            style_table={'backgroundColor': '#E6B0AA'},  # Table background color
            style_data={'backgroundColor': '#E6B0AA', 'color': '#4B0082'},  # Data cell background and text color
            style_header={'backgroundColor': '#E0F7FA', 'color': '#4B0082'}  # Header cell background and text color
        ),
        style=tab_style, selected_style=selected_tab_style
    )
])

app.layout = html.Div(style=background_style, children=[
    html.H1("Yahoo Finance App", style={'text-align': 'center'}),
    html.Div(children=[
        html.H2("Select a stock"),
        dcc.Dropdown(options=[{'label': sym, 'value': sym} for sym in symbol_list], id='ticker_selection', value='QQQ',
                     style=dropdown_style),
        tabs
    ])

])

