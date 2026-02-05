import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import re

# hide streamlit logo and footer
hide_default_format = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

# customize color of sidebar and text
st.markdown(hide_default_format, unsafe_allow_html=True)
st.markdown("""
    <style>
        /* 1. Target the main content area background */
        [data-testid="stAppViewBlockContainer"] {
            background-color: #f6f6f6;
        }
        /* Sidebar background */
        [data-testid=stSidebar] {
            background-color: #f6f6f6;
            color: #28282b;
        }
        /* Target all text elements within the sidebar (labels, markdown, sliders, etc.) */
        [data-testid="stSidebar"] * {
            color: #28282b !important;
        }
    </style>
    """, unsafe_allow_html=True)


# page layout config and add image
st.set_page_config(layout="centered", page_title="Contact", page_icon=":material/contact_mail:")

# set title and subtitle
st.markdown("<h1><span style='color: #691c32;'>📩 Contact Form</span></h1>",
    unsafe_allow_html=True)

st.write("Please fill out the form below to get in touch.")


# Simple but effective email regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

# Establish the connection to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Name", placeholder='Jane Doe',)
    email = st.text_input("email", placeholder='jane.doe@example.com',)
    #subject = st.selectbox("Subject", ["Interview", "Information", "Technical Support",])
    message = st.text_area("Message", placeholder='Write your message here.',)
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if name and email and message:
            # CHECK: Is the email valid?
            if not is_valid_email(email):
                st.error("📧 Please enter a valid email address (e.g., name@example.com).")
            else:
                try:
                    # Get fresh data (no cache)
                    existing_data = conn.read(worksheet="database", ttl=0)
                    # 1. Create a dataframe from the new entry        
                    new_data = pd.DataFrame([{
                        "Name": name,
                        "email": email,
                        #"Subject": subject,
                        "Message": message,
                    }])

                    #get uppercase letters
                    new_data['Name'] = new_data['Name'].str.title()
                    new_data['email'] = new_data['email'].str.lower()
                    new_data['Message'] = new_data['Message'].str.capitalize()

                    # 2. Add the new row
                    updated_df = pd.concat([existing_data, new_data], ignore_index=True)
                    
                    # 3. Update the Google Sheet
                    conn.update(worksheet="database", data=updated_df)
                    
                    st.success(f'''Thank you, {name.title()}.   
                        Your message has been sent!
                        ''')
                    st.balloons()
                except Exception as e:
                    st.error(f"Connection error: {e}")

        else:
            st.warning("⚠️ Please fill in all fields.")

st.caption('©2026 *Jesus LM*')
