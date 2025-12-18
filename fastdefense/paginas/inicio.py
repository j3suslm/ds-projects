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

# image
st.image('images/home.png')

st.write('''
<h2 style='text-align: justify; color: #fff;'>
¿De qué te sirve aprender técnicas que no puedes utilizar en situaciones reales?
''',
unsafe_allow_html=True)

st.markdown('''
<div style="text-align: justify; color: fff;">
<b>FAST DEFENSE SYSTEM</b> te permite aprender un método de defensa personal altamente EFICIENTE y de rápido aprendizaje.
<br>
<br>
Aprender a defenderte, te permitirá desarrollar confianza y seguridad. Además, aprenderás a obtener el control ante una agresión o cualquier situación de peligro que te encuentres.

Aprenderás como aplicar las técnicas y estrategias más efectivas para contrarrestar cualquier tipo de agresión. Y estarás preparado para actuar eficientemente ante cualquier situación o agresión inminente.

La verdad es que no necesitas ser cinta negra ni pasar muchos años entrenando, para que aprendas como puedes defenderte eficientemente.

Nuestro método de defensa personal, funciona para cualquier persona que necesite aprender a protegerse en situaciones a las que estamos EXPUESTOS todo el tiempo.

Fast Defense System es un método comprobado. Aquí no perdemos tiempo haciendo katas, ejercicios aeróbicos o simulaciones de pelea que no sirven para la vida real.

La diferencia es muy simple; enseñamos técnicas y estrategias basadas en la realidad, a la que inevitablemente te vas a enfrentar.

Debemos de entender que en la calle no existen reglas ni un réferi que te proteja en un conflicto, donde las cosas no te estén saliendo bien. Solo tu instinto asesino de supervivencia hará que salgas victorioso.

<b>LA REALIDAD ES QUE EN LA CALLE NO HAY REGLAS</b>

En una pelea callejera nadie estará para ayudarte. Solo tus habilidades podrán sacarte victorioso para SOBREVIVIR.

<b>¡No esperes más y CONTÁCTANOS YA!</b>

Te garantizamos RESULTADOS INMEDIATOS
</div>
''',
unsafe_allow_html=True)
