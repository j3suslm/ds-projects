import streamlit as st


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

st.image('images/cursos1.png')

st.write('''
## Una decisión puede cambiar tú vida 

#### NO TE ENGAÑES,NO ES CUESTIÓN DE SUERTE

Son las decisiones que tomamos, lo único que nos permite solucionar los problemas que podemos enfrentar a lo largo de nuestra vida; aprender DEFENSA PERSONAL puede ser la mejor decisión e inversión que podamos tomar. Recordemos que es mejor estar preparado para algo que nunca suceda, a no saber que hacer si se presenta.

Hoy en día, es indispensable tener herramientas y conocimientos de auto protección, que nos permita protegernos ante cualquier ataque inesperado, que ponga en riesgo nuestra integridad, nuestro patrimonio o la de nuestros seres queridos.
''')

st.image('images/cursos2.png')

st.write('''
### WING CHUN KUNG FU 

¿Te gustaría tener el control y dominio de cualquier situación de peligro que te encuentres?

Wing chun es un sistema altamente eficiente, basado en movimientos ágiles, contundentes y efectivos. El sistema fue desarrollado para utilizar estrategias y tácticas especiales de la defensa personal, (espacio) que transforman la aparente vulnerabilidad en control y poder absoluto.

Domina los secretos del auténtico Wing chun y te convertirás en el dueño de tú seguridad. No pierdas más tiempo y dinero. Aprende una de las mejores artes marciales para la defensa personal. Nuestros resultados están garantizados. Toma la decisión que transformará radicalmente tu vida.
''')

st.image('images/cursos3.png')

st.write('''
### FAST DEFENSE SYSTEM 

El entrenamiento que se desarrolla NORMALMENTE en una clase de artes marciales dentro de un Dojo, dista mucho de apegarse a la realidad.

De que te sirve aprender técnicas o estrategias que no te van a funcionar ante una agresión real y que te exponen a lesiones graves o letales.

LO COMERCIAL O LAS FANTASÍAS DEL SÉPTIMO ARTE son muy peligrosas, por qué te hacen creer que eres invencible y poderoso. Lamentablemente descubres a la mala, que nunca estuviste capacitado, ni sabes defenderte realmente.

Esto puede traerte graves consecuencias legales. Pues somos responsables en todo momento de nuestros actos y de nuestras decisiones.

FAST DEFENSE SYSTEM fue desarrollado para que aprendas defensa personal realmente de forma eficiente y consciente.

FAST DEFENSE SYSTEM es un sistema práctico y no teórico. Está basado en situaciones reales a las que estamos constantemente EXPUESTOS.

Nuestro sistema es de rápido aprendizaje, contamos con más de 35 años de experiencia en la enseñanza de las artes marciales y defensa personal.

AL FINAL SON LOS RESULTADOS LO ÚNICO QUE REALMENTE CUENTAN.
''')

st.image('images/cursos4.png')

st.write('''
### CURSO PARA MUJERES 

La violencia contra las mujeres está más extendida. Ocurre en el ámbito de las relaciones más cercanas, como la de la pareja. Por ende, el principal agresor es o ha sido el actual o última pareja, algún familiar; y por supuesto, las emergencias que se presentan en la calle.

EL MÁS GRAVE ERROR ES PENSAR QUE NO ESTAMOS EXPUESTOS O SOMOS VULNERABLES A CUALQUIER TIPO DE AGRESIÓN.

Lo mejor que podemos hacer, es adquirir las herramientas necesarias para saber qué hacer ante cualquier agresión y obtener el control de cualquier situación
''')

st.image('images/cursos5.png')

st.write('''
### CURSO PARA ADOLESCENTES 

Si realmente quieres proteger a tus hijos, la mejor decisión que puedes tomar, es brindarles la oportunidad de aprender a defenderse por sí mismos.

La realidad nos enseña, que no siempre estarás ahí para defenderlo de las agresiones o abusos, a los que inevitablemente está expuesto.

APRENDER A DEFENDERSE ES INDISPENSABLE PARA SU DESARROLLO.             

APRENDER A DEFENDERSE ES INDISPENSABLE PARA SU CONFIANZA.                 

APRENDER  A DEFENDERSE ES INDISPENSABLE PARA SU SEGURIDAD.                 

APRENDER A DEFENDERSE ES INDISPENSABLE PARA EVITAR ABUSOS.

FAST DEFENSE SYSTEM está desarrollado para brindarle las herramientas necesarias y para obtener el control de la situación. Y al mismo tiempo. saber qué es lo más conveniente que puede hacer ante una agresión o abuso.

Te garantizamos que somos la mejor opción para el aprendizaje de la defensa personal a un alto nivel para tus hijos.

Nuestro sistema está basado en situaciones reales y es de rápido aprendizaje
''')

st.image('images/cursos6.png')
st.image('images/cursos7.png')

st.write('''
### CURSO ONLINE

Este curso se compone de 8 módulos con más de 55 vídeos que te llevarán paso a paso, para que tu domines los aspectos importantes de la defensa personal.

Cada módulo del curso, lleva una secuencia para que vayas dominando cada aspecto que se muestra a nivel técnico, práctico y teórico.

Aprender a defenderte desde casa, si es posible con nuestro curso de defensa personal online. Nuestro curso en línea, te enseña a desarrollar habilidades prácticas para protegerte y manejar situaciones de riesgo, guiado personalmente por Sifu Martin Arzate.
''')

st.image('images/cursos8.png')

st.write('''
### CURSO PARA EMPRESAS 

Por varios años, hemos impartido esta capacitación con excelentes resultados y de mucho aprendizaje para cada participante.

Si tú eres una empresa que busca brindar un beneficio de valor a tu personal, no dudes en contactarnos para ofrecerte una propuesta, acorde a tus necesidades.

Podemos impartir cursos-talleres con la duración de horas que mejor te convenga. Ponte en contacto con nosotros, donde con mucho gusto te daremos la mejor solución a tu solicitud y el mejor entrenamiento.

Somos expertos en la defensa personal y tumejor opción.
''')

st.image('images/cursos9.png')

st.write('''
### CURSO PARA ESCOLTAS

Aumenta las habilidades que necesitas para proteger y protegerte eficientemente.

Nuestro curso de defensa personal especializado para escoltas, te prepara para enfrentar situaciones de riesgo con confianza y tener el control que se necesita.

Aprende técnicas avanzadas de control y conducción de agresores, manejo de amenazas y tácticas de protección en un entorno seguro y profesional.

Mejora tus capacidades y refuerza la seguridad de tu entorno hoy mismo.
''')

st.image('images/cursos10.png')

st.write('''
### WING CHUN KUNG FU 

¡Conviértete en un Instructor Experto en Defensa Personal y Wing Chun Kung fu

¿Eres instructor o profesional del entrenamiento físico? Este curso de Defensa Personal Especial para Instructores está diseñado específicamente para ti.

Adquiere las técnicas y herramientas avanzadas necesarias para capacitar a otros en defensa personal, ayudándoles a enfrentar situaciones de riesgo con seguridad y confianza.

¿Por qué este curso es diferente?

1. Metodología Exclusiva: Aprende un enfoque integral de defensa personal que combina técnicas físicas, psicológicas y preventivas, diseñado específicamente para entrenadores que desean enseñar de manera segura y efectiva.

2. Enfocado en la Enseñanza: No solo aprenderás habilidades de defensa personal; aprenderás a transmitirlas. Obtén los conocimientos pedagógicos para enseñar a personas de diferentes niveles de habilidad y preparación física.

3. Certificación Profesional: Al finalizar, recibirás una certificación reconocida que avala tu capacidad como instructor especializado, aumentando tu valor profesional y abriendo nuevas oportunidades en el mercado laboral.

4. Clases Prácticas y Simulaciones: Entrena en escenarios realistas con expertos que te enseñarán cómo responder en situaciones de la vida real. Esto te permitirá prepararte para responder y enseñar con calma y precisión.

¿Qué obtendrás al finalizar el curso?

Habilidad para instruir con seguridad y profesionalismo.

Técnicas avanzadas de defensa personal.

Certificación que te destacará en el mercado de fitness y seguridad.

Da el siguiente paso en tu carrera como instructor! 

Inscríbete hoy en el Curso de Defensa Personal para instructores y comienza a marcar la diferencia.
''')
