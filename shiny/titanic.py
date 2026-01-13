import pandas as pd
from shiny import reactive
from shiny.express import ui, input
import plotly.express as px
from shinywidgets import render_plotly
from shinyswatch import theme

df = pd.read_csv('titanic.csv')

# fill missing values
df['Embarked'] = df['Embarked'].fillna('Unknown')

# unique values
embarked_port = list(df['Embarked'].unique())
gender = list(df['Sex'].unique())

# page title
ui.page_opts(title='Titanic Dashboard', theme=theme.minty())

# filtering
@reactive.calc
def filter_df():
    df_result = df[df['Embarked']==input.port_dropdown()]
    df_result = df_result[df_result['Sex']==input.gender_dropdown()]
    return df_result

# cards selectors
with ui.card():
    'Card test'
    with ui.layout_columns(col_widths=[4,-4,4]):
        # embarkment
        ui.input_selectize(
            choices=embarked_port,
            label='Port of embarkment',
            id='port_dropdown',
        )
        # sex
        ui.input_selectize(
            choices=gender,
            label='Gender',
            id='gender_dropdown',
        )

    # charts
    with ui.layout_columns(col_widths=[9,3]):
        @render_plotly
        def hist():
            plot = px.histogram(
                data_frame=filter_df(),
                template='ggplot2',
                title='Distribution of age',
                facet_col='Survived',
                x='Age',
            )
            return plot

        @render_plotly
        def pie_chart():
            df_plot = filter_df()
            df_plot = df_plot.loc[:, ['PassengerId','Survived']].groupby(['Survived']).count().reset_index()
            df_plot.rename(
                {'PassengerId':'Count of passengers'},
                axis='columns',
                inplace=True,
            )
        
            plot = px.pie(
                data_frame=df_plot,
                template='ggplot2',
                title='Count of passengers that survived',
                values='Count of passengers',
                names='Survived',
            )
            return plot

    @render_plotly
    def box_display():
        df_plot = filter_df()
        plot = px.box(
            data_frame=df_plot,
            y='Fare',
            x='Survived',
            color='Survived',
            title='Distribution of fare across survival status',
            template='ggplot2',
        )
        return plot
