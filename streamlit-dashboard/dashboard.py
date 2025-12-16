import streamlit as st
import pathlib
from streamlit_extras.metric_cards import style_metric_cards
from faker import Faker
import pandas as pd
import numpy as np
st.set_page_config(page_title="Dashboard", layout="wide")

def load_css(file_css):
    with open(file_css) as css:
        st.html(f"<style>{css.read()}</style>")

css_path = pathlib.Path("style.css")
load_css(css_path)

faker = Faker('es_MX')

with st.container(border=True):
    st.markdown('<h1 style="color:#354C70;"> Financial Dashboard</h1>', unsafe_allow_html=True)

    st.caption('Company XYZ &copy; 2025')

    c1, c2, c3 = st.columns(3)
    with c1:
        st.success(faker.bank())
        st.metric("Price", value=faker.pricetag(), delta=faker.numerify())
    with c2:
        st.warning(faker.bank())
        st.metric("Price", value=faker.pricetag(), delta=faker.numerify())
    with c3:
        st.info(faker.bank())
        st.metric("Price", value=faker.pricetag(), delta=faker.numerify())
        

    style_metric_cards(border_left_color="green", border_size_px=0)

    col1, col2 = st.columns([2,1])
    with col1:
        st.info("Balance")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a","b","c"])
        st.bar_chart(chart_data)   
    with col2:
        st.warning("Capital Flow")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a","b","c"])
        st.line_chart(chart_data) 

    data = {
        "Bank:": [faker.bank() for _ in range(10) ],
        "Country:": [faker.city() for _ in range(10) ],
        "Phone:": [faker.phone_number() for _ in range(10) ],
    }

    df = pd.DataFrame(data)

    st.success("### Relation of Banks")
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.markdown('''
    <p style="color:#354C70;">
        <b>Jesus L. Monroy</b>
        <br>
        <i>Economist & Data Scientist</i>
    </p>''',
    unsafe_allow_html=True
)

st.caption('Inspirado en el curso de Jorge Maldonado (Desarrollo de Web apps con Streamlit)')

