import streamlit as st
from st_social_media_links import SocialMediaIcons
import streamlit.components.v1 as components
from PIL import Image

# Custom CSS to hide 3 dots on top right
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Custom CSS to make the sidebar black
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #000000;
        }
        
        /* Optional: Change sidebar text color to white for better contrast */
        [data-testid="stSidebar"] .stText, 
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] label {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# load icon image
logo = Image.open('images/dragon.png')
st.set_page_config(page_title="Fast Defense Mexico", layout="centered", page_icon=logo)


# website pages
pages = [
        st.Page("paginas/inicio.py", title="Home", icon=":material/add:"),
        st.Page("paginas/cursos.py", title="Cursos", icon=":material/add:"),
        st.Page("paginas/sifu.py", title="Sifu Martin Arzate", icon=":material/add:"),
    ]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()


# footer
st.caption('---')
# map location
components.iframe("https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d60223.87490881656!2d-99.1519037!3d19.3694912!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85d1ff86e874b39d%3A0x65a4132ed916912e!2sFast%20Defense%20System!5e0!3m2!1sen!2smx!4v1765993580838!5m2!1sen!2smx", width=450, height=320)
st.caption('Municipio Libre 174, Col. Portales Norte, Alcaldía Benito Juárez, CP 03300, CdMx, México (52) 55 3028 3342')


# social media icons
social_media_links = [
    'https://www.tiktok.com/@fastdefensesystem?lang=es&is_from_webapp=1&sender_device=mobile&sender_web_id=7431161494010250757',
    "https://www.facebook.com/Sifumartinarzate/videos/fast-defense-system-te-permite-aprender-a-defenderte-ante-cualquier-situaci%C3%B3n-de/233239751937116",
    "https://www.youtube.com/@fastdefensesystem",
    "https://api.whatsapp.com/send?phone=5215530283342&text=Solicito%20informaci%C3%B3n%20de%20los%20cursos%20de%20defensa%20personal%20",
    "mailto:marzate38@yahoo.com.mx",
]

colors = ["Silver", "Blue", "Red", "Green", "Silver"]
social_media_icons = SocialMediaIcons(social_media_links, colors)
social_media_icons.render(sidebar=False)
