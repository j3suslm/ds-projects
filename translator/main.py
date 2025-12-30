import streamlit as st

st.set_page_config('Traducciones')

pages = {
    'Servicios': [
        st.Page('traductor.py', title='Traductor', icon=':material/translate:'),
        st.Page('traductor_archivos.py', title='Traductor de archivos', icon=':material/g_translate:'),
    ]
}

pg = st.navigation(pages=pages, position='sidebar', expanded=True)
pg.run()
