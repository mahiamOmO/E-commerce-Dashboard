import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Category': ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports'],
    'Sales': [2000, 1500, 1000, 1200, 800],
    'Orders': [300, 200, 150, 180, 120]
}
df = pd.DataFrame(data)

# Create a Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('E-commerce Dashboard'),

    dcc.Graph(
        id="sales-bar-chart",
        figure=px.bar(df, x='Category', y='Sales', title='Sales by Category')
    ),
    dcc.Graph(
        id='orders-pie-chart',
        figure=px.pie(df, names='Category', values='Orders', title='Orders Distribution by Category')
    ),
    html.Div([

        dcc.Dropdown(
            id="category-dropdown",
            options=[{'label': cat, 'value': cat} for cat in df['Category']],
            value=df['Category'][0],
        ),

        dcc.Graph(id='category-sales-chart')
    ])
])

# Callback to update category sales chart
@app.callback(
    Output('category-sales-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    return px.bar(filtered_df, x='Category', y='Sales', title=f'Sales for {selected_category}')


if __name__ == '__main__':
    app.run_server(debug=True)
