import streamlit as st
from PIL import Image

# Custom CSS to hide 3 dots on top right
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: some;}
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

st.image('images/sifu1.png')
st.write('---')
st.video('https://youtu.be/SVZxI8yvLWU')

st.write('''
### Director general 
#### Fundador de Fast Defense System
---
''')

st.image('images/sifu2.png', width=700)

st.write('''
Inicia su entrenamiento de Wing Chun en 1985 en el Puerto de Acapulco; Gro. Con el Profr. Rodolfo Álvares. (QEPD +++)

De 1990 – 1996 entrena Jeet Kune Do en la Academia IMB en el Puerto de Acapulco; Gro. Representada por el profesor Rodolfo Álvares Ayvar,donde entrenó diversas disciplinas de Artes Marciales como Boxeo, Muay Thai, Kali Filipino, Jeet Kune Do.
Durante este periodo de tiempo, participo en diversos seminarios de Jeet Kune con el Maestro Richard Bustillo, Co-fundador de la IMB (INTERNATIONAL MARTIAL ARTS & BOXING)

De 1996 – 2000 entreno con Si fu Abram Ghandy Yuaza, Fundador de la Asociación Nacional de Hok Hok Pai y Asociación Nacional de VingTsun Moy Yat.

Del 2000 – 2010 Entrenó con Sifu Emin Boztepe.

Ha practicado diversos sistemas de Artes Marciales aparte del WingChun como Boxeo, Kali, Kuntao Silat, Jiu-jitsu, Sambo y judo, así como kick boxing. Sus entrenamientos los ha llevado a cabo en México y USA. ( LAX, MIAMI, LAS VEGAS )

Ha participado en diversos programas de  televisión en como:
Hoy,Se vale, TeleHit, Canal 11, TV Azteca,y un gran número de reportajes de medios impresos y radio.

Ha impartido varios seminarios de VingTzun y defensa personal en diversas Ciudades del País.

Ha sido Instructor de escoltas  y grupos de seguridad élite.

Creador de los programas de FAST DEFENSE SYSTEM…Defensa Personal para el Mundo Real

CERTIFICACIONES EN MEDICINA CHINA Y TERAPIAS ALTERNATIVAS:

Título de “Quirofísico” con especialidad en Hidroterapia, Quiropráctico y Masajes. ( Sueco, drenaje linfático, deportivo, shiatsu, reductivo)

- Especialidad de asesor en herbolaria.
- Ventosas y Moxibustión
- Certificación en Auriculo-puntura
- Digito Presión
- Reflexología
- Maestría en Reiki Usui Tibetano
- Certificación en Ajuste Biomagnético 
- Certificación en terapia neural
- Certificación en manejo de emociones
''')

st.video('https://youtu.be/shrFVQlL4X0?list=TLGG9avOOg2e9ZsxNzEyMjAyNQ')
