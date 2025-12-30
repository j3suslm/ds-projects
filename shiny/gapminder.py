import plotly.express as px
from shiny.express import ui, input
from shinywidgets import render_plotly
from shinyswatch import theme
import pandas as pd

## data preparation
# read data
df = pd.read_csv('gapminder_data.csv')
# create list of years
years_list = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
    2015, 2016, 2017, 2018,]

# create shiny canvas
ui.page_opts(title='Gapminder Dashboard in Shiny',
    theme=theme.superhero,
    )

# dropdown widget
ui.input_selectize(id='select_year', 
    label='Select year',
    choices=years_list,
    )

# create chart
@render_plotly
def show_graph():
    # create variable of selected year
    selected_year = int(input.select_year())
    # scatter chart
    plot = px.scatter(
        df[df['year']==selected_year],
        x='gdp',
        y='life_exp',
        hover_name='country',
        color='continent',
        title=f'Life Expectacy vs GDP - {selected_year}',
        template='ggplot2',
    )

    return plot

