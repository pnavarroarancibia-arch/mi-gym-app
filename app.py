import streamlit as st
import pandas as pd
import math

# 1. Configuración de Estilo "Gimnasio Real" (Negro y Naranja)
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
    }
    </style>
    """, unsafe_allow_html=True) # <-- AQUÍ ESTABA EL ERROR CORREGIDO

# Imagen de cabecera
st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1470&auto=format&fit=crop", use_container_width=True)

st.title("🏋️‍♂️ GYM PRO ELITE")

# Sidebar
st.sidebar.header("👤 Perfil de Atleta")
nombre = st.sidebar.text_input("Nombre", "Atleta")
objetivo = st.sidebar.selectbox("Objetivo", ["Perder Peso", "Ganar Músculo"])
peso_act = st.sidebar.number_input("Peso Actual (kg)", 40.0, 150.0, 70.0)

# Pestañas
tab1, tab2, tab3, tab4 = st.tabs(["💪 RUTINAS", "📊 BIOMETRÍA", "🍎 NUTRICIÓN", "💧 HIDRATACIÓN"])

with tab1:
    st.header("📋 Entrenamiento del Día")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW92Z3J6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9iYyZjdD1n/3o7TKMGpxxSAYX9HlS/giphy.gif")
    with col2:
        st.subheader("Sentadilla Goblet")
        st.write("**4 Series x 15 Reps**")
        st.info("💡 Baja la cadera manteniendo la espalda recta.")

with tab4:
    st.header("💧 Control de Hidratación")
    vasos = st.slider("Vasos de agua hoy", 0, 15, 0)
    st.write(f"Has bebido {vasos * 250} ml de agua.")
    if vasos >= 8:
        st.balloons()
        st.success("¡Meta diaria cumplida! 💧")

