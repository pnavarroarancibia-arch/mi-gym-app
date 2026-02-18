import streamlit as st
import pandas as pd
import math

# 1. Configuración Visual Estilo Gym (Negro y Naranja)
st.set_page_config(page_title="Gym Pro Elite", page_icon="💪", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #FF4B2B !important;
    }
    .stButton>button {
        background-color: #FF4B2B;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1E1E1E;
        border-radius: 4px;
        color: white;
        padding: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF4B2B;
    }
    </style>
    """, unsafe_allow_html=True) # <-- CORRECCIÓN AQUÍ

# Imagen de fondo profesional
st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1470&auto=format&fit=crop", use_container_width=True)

st.title("🏋️‍♂️ GYM PRO ELITE")

# Sidebar con Perfil
st.sidebar.header("👤 Perfil de Atleta")
nombre = st.sidebar.text_input("Nombre", "Atleta")
objetivo = st.sidebar.selectbox("Objetivo", ["Perder Peso", "Ganar Músculo"])
peso_act = st.sidebar.number_input("Peso Actual (kg)", 40.0, 150.0, 70.0)
altura = st.sidebar.number_input("Altura (cm)", 100, 250, 170)

# Pestañas de la Aplicación
tab1, tab2, tab3, tab4 = st.tabs(["💪 RUTINAS", "📊 BIOMETRÍA", "🍎 NUTRICIÓN", "💧 HIDRATACIÓN"])

with tab1:
    st.header("📋 Tu Entrenamiento de Hoy")
    
    # Ejercicio 1
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW92Z3J6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxxSAYX9HlS/giphy.gif", caption="Sentadillas")
    with c2:
        st.subheader("Sentadilla Goblet")
        st.write("**Series:** 4 | **Reps:** 15 | **Descanso:** 60 seg")
        st.info("💡 Mantén la espalda recta y baja la cadera.")
        st.checkbox("Completado", key="ex1")

    st.divider()

    # Ejercicio 2
    c3, c4 = st.columns([1, 2])
    with c3:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW92Z3J6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l0HlPtb37SjPr7iM/giphy.gif", caption="Flexiones")
    with c4:
        st.subheader("Flexiones de Brazo")
        st.write("**Series:** 3 | **Reps:** Al fallo | **Descanso:** 90 seg")
        st.info("💡 Aprieta el abdomen y no dejes caer la cadera.")
        st.checkbox("Completado", key="ex2")

with tab2:
    st.header("📉 Seguimiento Biométrico")
    imc = peso_act / ((altura/100)**2)
    st.metric("Tu IMC Actual", round(imc, 1))
    st.write("Registra tus medidas semanales para generar gráficas de progreso.")

with tab3:
    st.header("🍎 Registro de Nutrición")
    comida = st.text_input("¿Qué comiste hoy? (Ej: Pechuga con arroz)")
    calorias = st.number_input("Calorías estimadas", 0, 1000, 0)
    if st.button("Registrar Alimento"):
        st.success(f"Guardado: {comida} - {calorias} kcal")
        st.info("💡 Tip: Prioriza proteínas y vegetales verdes.")

with tab4:
    st.header("💧 Hidratación (Meta: 3 Litros)")
    vasos = st.slider("Vasos de agua (250ml cada uno)", 0, 15, 0)
    litros = vasos * 0.25
    st.progress(min(litros/3, 1.0))
    st.write(f"Has bebido: **{litros} Litros**")
    if litros >= 3:
        st.balloons()
        st.success("¡Meta cumplida! Estás bien hidratado.")
