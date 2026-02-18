import streamlit as st
import pandas as pd
import math
from datetime import datetime

# 1. Configuración de la App
st.set_page_config(page_title="Mi Gimnasio Pro", page_icon="🏋️‍♂️")

# 2. Título y Bienvenida
st.title("🏋️‍♂️ Mi Gimnasio Pro")
st.markdown("""
### 🌟 ¡Bienvenido a tu nueva vida saludable!
Esta aplicación es tu asistente personal para lograr el cuerpo que deseas. 
**¿Qué puedes hacer hoy?** Usa las pestañas de abajo para navegar.
""")

# 3. Formulario en la barra lateral (Perfil)
st.sidebar.header("👤 Tu Perfil")
nombre = st.sidebar.text_input("Nombre", "Usuario")
edad = st.sidebar.number_input("Edad", 15, 100, 25)
genero = st.sidebar.selectbox("Género", ["Hombre", "Mujer"])
altura = st.sidebar.number_input("Altura (cm)", 100, 250, 170)
objetivo = st.sidebar.selectbox("Objetivo", ["Perder Peso", "Ganar Músculo"])

# 4. Pestañas principales
tab1, tab2, tab3 = st.tabs(["📊 Mi Progreso", "🍎 Mi Dieta", "💪 Mi Rutina"])

with tab1:
    st.header("Seguimiento Físico")
    col1, col2, col3 = st.columns(3)
    peso_act = col1.number_input("Peso (kg)", 30.0, 200.0, 70.0)
    cintura_act = col2.number_input("Cintura (cm)", 40.0, 150.0, 80.0)
    cuello_act = col3.number_input("Cuello (cm)", 20.0, 70.0, 40.0)
    
    # Cálculos automáticos
    imc = peso_act / ((altura/100)**2)
    
    # Fórmula Grasa Corporal (Marina EE.UU.)
    try:
        if genero == "Hombre":
            grasa = 495 / (1.0324 - 0.19077 * math.log10(cintura_act - cuello_act) + 0.15456 * math.log10(altura)) - 450
        else:
            # Aproximación para mujer
            grasa = 495 / (1.29579 - 0.35004 * math.log10(cintura_act + 10 - cuello_act) + 0.22100 * math.log10(altura)) - 450
    except:
        grasa = 0

    st.divider()
    st.subheader("Resultados de Hoy")
    c_imc, c_grasa = st.columns(2)
    c_imc.metric("Tu IMC", round(imc, 1))
    c_grasa.metric("Grasa Corporal", f"{round(grasa, 1)}%")

with tab2:
    st.header("Plan Nutricional Inteligente")
    # Cálculo de Calorías (Harris-Benedict)
    tmb = (10 * peso_act) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
    mantenimiento = tmb * 1.55
    kcal_final = mantenimiento - 500 if objetivo == "Perder Peso" else mantenimiento + 300
    
    st.success(f"🎯 Meta diaria recomendada: **{round(kcal_final)} kcal**")
    
    # Macros
    prot = peso_act * (2.0 if objetivo == "Perder Peso" else 2.2)
    gras = peso_act * 1.0
    carb = (kcal_final - (prot * 4) - (gras * 9)) / 4
    
    m1, m2, m3 = st.columns(3)
    m1.info(f"🥩 Prot: {round(prot)}g")
    m2.info(f"🥑 Grasas: {round(gras)}g")
    m3.info(f"🍝 Carbos: {round(carb)}g")

with tab3:
    st.header("Rutina Recomendada")
    if objetivo == "Perder Peso":
        st.write("🔥 **Enfoque:** Quema de grasa y tono muscular.")
        st.write("1. **Sentadillas:** 4 series de 20 reps.")
        st.write("2. **Flexiones:** 3 series al fallo.")
        st.write("3. **Burpees:** 3 series de 12 reps.")
    else:
        st.write("⚡ **Enfoque:** Hipertrofia y fuerza.")
        st.write("1. **Press Militar:** 4 series de 10 reps.")
        st.write("2. **Peso Muerto:** 4 series de 8 reps.")
        st.write("3. **Dominadas o Remo:** 3 series de 10 reps.")

st.sidebar.divider()
st.sidebar.write("💡 *Recuerda actualizar tu peso cada semana para ajustar tus macros.*")
