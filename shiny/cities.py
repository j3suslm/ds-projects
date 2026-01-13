import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from shinyswatch import theme
from shiny.express import ui, input
from shiny import reactive

# read data
df = pd.read_csv('us_cities_top_1k_multi_year.csv')

# data preprocessing
unique_years = list(df['year'].unique())
unique_years.sort()

unique_states = list(df['State'].unique())
unique_states.sort()

with ui.card():
    ui.page_opts(
        title='Shiny Dashboard',
        full_width=False,
        theme=theme.minty
    )

with ui.card():
    ui.panel_title(title='US Cities')

with ui.layout_columns():
    ui.input_slider(
        id='selected_year',
        label='Select year',
        min=unique_years[0],
        value=unique_years[0],
        max=unique_years[-1],
    )
    
    ui.input_selectize(
        id='selected_state',
        label='Select state',
        choices=unique_states,
    )

# map across years showing cities as dots
@reactive.calc
def filter_year():
    data = df[df['year']==input.selected_year]
    return data

# charts
with ui.card():
    @render_plotly
    def show_map():
        plot = px.scatter_mapbox(
            data_frame=filter_year(),
            lat='lat',
            lon='lon',
            size='Population',
            zoom=3,
            mapbox_style='open-street-map',
            template='ggplot2',
        )
        return plot


