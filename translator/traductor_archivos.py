import streamlit as st
from deep_translator import GoogleTranslator #5000 characte max
import pyperclip
from docx import Document
from PyPDF2 import PdfReader
import pandas as pd

st.title('Traductor de archivos')

def copy_text(text):
    pyperclip.copy(text)

languages = {
    'Español':'es',
    'Inglés':'en',
    'Francés':'fr',
    'Alemán':'de',
    'Italiano':'it',
}

target_lan = st.selectbox('Idioma destino', options=list(languages.keys()))

file = st.file_uploader('Sube archivo (text, docx, pdf, csv)', type=['txt','docx','pdf','csv'])

if file:
    text_content = ''
    try:
        if file.name.endswith('.txt'):
            text_content = file.read().decode('utf-8')
        elif file.name.endswith('.docx'):
            doc = Document(file)
            text_content = '\n'.join([p.text for p in doc.paragraphs])
        elif file.name.endswith('.pdf'):
            pdf_reader = PdfReader(file)
            text_content = '\n'.join([page.extract_text() for page in pdf_reader.pages])
        elif file.name.endswith('.csv'):
            df = pd.read_csv(file)
            text_content = df.to_csv(index=False)
        
        st.text_area('Contenido del archivo', text_content, height=300)
        
        if st.button('Traducir'):
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lan],
            ).translate(text_content)
        
            st.success('Traducción completa!')
            st.text_area('Texto traducido', translated_text, height=300)
            st.button('Copiar', icon=':material/file_copy:', type='primary', on_click=copy_text(translated_text))            

    except Exception as e:
        st.error(f'Error al procesar el archivo: {e}')
    