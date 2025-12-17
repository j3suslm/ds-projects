import streamlit as st
import pandas as pd

def imc():
    st.subheader('Indice de Masa Corporal')
    st.latex(r'\text{IMC} = \frac{\text{Peso (kg)}}{\text{Estatura (m)}^2}')
    
    st.markdown('**Tabla del IMC según la OMS**')
    
    datos_imc = {
        'Categoria': [
            'Peso insuficiente', 
            'Peso normal',
            'Sobrepeso',
            'Obesidad grado 1',
            'Obesidad grado 2',
            'Obesidad grado 3 (morbida)',
        ],
        'Rango del IMC': [
            '< 18.5',
            '18.5 - 24.9',
            '25 - 29.9',
            '30 - 34.9',
            '35 - 39.9',
            '40+',
        ]
    }

    tabla_imc = pd.DataFrame(datos_imc)

    st.table(tabla_imc)

    c1, c2 = st.columns(2)

    peso = c1.number_input('Peso', step=0.1)
    altura = c2.number_input('Altura')

    def imc_calc(peso, altura):
        if altura <=0 or peso <=0:
            return None
        else:
            imc_res = peso/altura**2
        return imc_res
    
    if st.button('Calcular', type='primary'):
        imc_res = imc_calc(peso, altura)
    
        if imc_res is None:
            st.error("¡Altura y peso deben ser mayores a cero!")
        elif imc_res < 18.5:
            st.info(f'Tu IMC es: {imc_res:.1f}')
        elif 18.5 < imc_res < 24.9:
            st.success(f'Tu IMC es: {imc_res:.1f}')
        elif 25 < imc_res < 29.9:
            st.warning(f'Tu IMC es: {imc_res:.1f}')
        else:
            st.error(f'Tu IMC es: {imc_res:.1f}')
