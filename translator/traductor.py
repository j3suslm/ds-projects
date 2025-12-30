import streamlit as st
from deep_translator import GoogleTranslator #5000 characte max
import pyperclip

st.title('Traductor')

def copy_text(text):
    pyperclip.copy(text)

text_to_translate = st.text_area('Escribe el texto a traducir')

languages = {
    'Español':'es',
    'Inglés':'en',
    'Francés':'fr',
    'Alemán':'de',
    'Italiano':'it',
}

target_lan = st.selectbox('Idioma destino', options=list(languages.keys()))

if st.button('Traducir'):
    if text_to_translate:
        try:
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lan],
            ).translate(text_to_translate)
            st.success(f'Traducción: {translated_text}')
            st.button('Copiar', icon=':material/file_copy:', type='primary', on_click=copy_text(translated_text))
        except Exception as e:
            st.error(f'Error al traducir: {e}')
    else:
        st.warning('Escribe un texto')
