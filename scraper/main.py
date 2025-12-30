import streamlit as st
from shortener import shortener
from scraper import scraper

st.set_page_config('Scraper')

tab1, tab2 = st.tabs(['URL Shortener','Wikipedia Scraper'])

with tab1:
    shortener()

with tab2:
    scraper()
