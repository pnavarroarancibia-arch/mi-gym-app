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
        color: #FF4B2B !important; /* Naranja Deportivo */
    }
    .stButton>button {
        background-color: #FF4B2B;
        color: white;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1E1E1E;
        border-radius: 4px 4px 0px 0px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF4B2B;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 2. Encabezado con Imagen de Fondo
st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1470&auto=format&fit=crop", caption="Tu éxito comienza hoy", use_container_width=True)

st.title("🏋️‍♂️ GYM PRO ELITE")

# 3. Sidebar (Perfil)
st.sidebar.header("👤 Perfil de Atleta")
nombre = st.sidebar.text_input("Nombre", "Atleta")
objetivo = st.sidebar.selectbox("Objetivo", ["Perder Peso", "Ganar Músculo"])
peso_act = st.sidebar.number_input("Peso Actual (kg)", 40.0, 150.0, 70.0)

# 4. Pestañas de la App Completa
tab1, tab2, tab3, tab4 = st.tabs(["💪 RUTINAS DIARIAS", "📊 BIOMETRÍA", "🍎 NUTRICIÓN", "💧 HIDRATACIÓN"])

with tab1:
    st.header("📋 Tu Entrenamiento del Día")
    
    # Ejemplo de ejercicio con imagen
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW92Z3J6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxxSAYX9HlS/giphy.gif", caption="Sentadillas")
    
    with col2:
        st.subheader("Sentadilla Goblet")
        st.write("**Series:** 4 | **Reps:** 15 | **Descanso:** 60 seg")
        st.info("💡 Mantén la espalda recta y el peso cerca de tu pecho.")
        st.checkbox("Marcar como completado", key="ej1")

    st.divider()

    col3, col4 = st.columns([1, 2])
    with col3:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW92Z3J6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l0HlPtb37SjPr7iM/giphy.gif", caption="Flexiones")
    
    with col4:
        st.subheader("Flexiones de Brazo")
        st.write("**Series:** 3 | **Reps:** Al fallo | **Descanso:** 90 seg")
        st.info("💡 No permitas que tu cadera caiga. Cuerpo como una tabla.")
        st.checkbox("Marcar como completado", key="ej2")

with tab2:
    st.header("📉 Seguimiento de Medidas")
    st.write("Registra tu evolución para ver las gráficas de progreso.")
    # Aquí iría el código de gráficas anterior...

with tab3:
    st.header("🥗 Diario de Alimentos")
    st.write("Próximamente: Registro de nutrientes y vitaminas.")
    comida = st.text_input("¿Qué comiste hoy?")
    calorias_comida = st.number_input("Calorías estimadas", 0, 2000, 0)
    if st.button("Registrar Alimento"):
        st.success(f"Registrado: {comida} ({calorias_comida} kcal)")

with tab4:
    st.header("💧 Control de Hidratación")
    vasos = st.slider("Vasos de agua hoy (250ml)", 0, 20, 0)
    st.progress(vasos / 10 if vasos <= 10 else 1.0)
    st.write(f"Has bebido {vasos * 0.25} Litros de agua.")
