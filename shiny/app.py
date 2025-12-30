from shiny.express import ui, input

with ui.sidebar(width=200, position='left', title='Sidebar', open='open',
    bg='#f8f8f8', fg='#28282b'):
    'Inside the sidebar'

'Outside the sidebar'

with ui.layout_columns(col_widths=[4,2,6]):
    with ui.card():
        'I am in column 1'
    with ui.card():
        'I am in column 2'
    with ui.card():
        'I am in column 3'
