import streamlit as st

def custom_card(title,content,color):
    card_style = f"""
        <style>
        .card{{
            background-color: {color};
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 20px;
            margin: 10px 0;
        }}
        .card-title{{
            font-size: 25px;
            font-weight: bold;
            color: black;
        }}
        .card-content{{
            font-size: 15px;
            color:#555;
        }}
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)
    card_html = f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <div class="card-content">{content}</div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)