from shiny.express import ui, input
from shiny import render
from shinyswatch import theme

with ui.card():
    # title
    ui.page_opts(title='Hello world!', theme=theme.darkly)

    # widget
    ui.input_text(id='hello_text', label='Enter your name')

# function
@render.text
def show_me():
    input_text = input.hello_text()
    return 'Hello ' + input_text
