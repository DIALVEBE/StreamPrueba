import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página
st.set_page_config(page_title="Demo Streamlit", layout="wide")
#st.set_page_config(page_title="Demo Streamlit", layout="centered")

# Sidebar
st.sidebar.title("Configuración")
nombre = st.sidebar.text_input("Tu nombre", "Usuario")
edad = st.sidebar.slider("Edad", 0, 100, 25)
mostrar_datos = st.sidebar.checkbox("Mostrar datos", True)

# Estado de sesión
if "contador" not in st.session_state:
    st.session_state.contador = 0

# Título principal
st.title("🚀 Demo completa de Streamlit")
st.write(f"Hola **{nombre}**, tienes {edad} años")

# Botón con estado
if st.button("Incrementar contador"):
    st.session_state.contador += 1

st.write(f"Contador: {st.session_state.contador}")

# Layout con columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Formulario")
    with st.form("mi_formulario"):
        num1 = st.number_input("Número 1", value=0)
        num2 = st.number_input("Número 2", value=0)
        operacion = st.selectbox("Operación", ["Suma", "Resta", "Multiplicación"])
        enviar = st.form_submit_button("Calcular")

    if enviar:
        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        else:
            resultado = num1 * num2
        st.success(f"Resultado: {resultado}")

with col2:
    st.subheader("Subir archivo")
    archivo = st.file_uploader("Sube un CSV", type=["csv"])
    if archivo:
        df = pd.read_csv(archivo)
        st.write(df.head())

# Generar datos
st.subheader("Datos aleatorios")
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["A", "B", "C"]
)

if mostrar_datos:
    st.dataframe(data)

# Gráficos
st.subheader("Gráficos")
col3, col4 = st.columns(2)

with col3:
    st.line_chart(data)

with col4:
    st.bar_chart(data)

# Tabs
tab1, tab2, tab3 = st.tabs(["Texto", "Código", "JSON"])

with tab1:
    st.write("Esto es texto en una pestaña")
    st.caption("Esto es texto en un caption")

with tab2:
    st.code("""
def hola():
    print("Hola mundo")
""", language="python")

with tab3:
    st.json({"nombre": nombre, "edad": edad})

# Multimedia
st.subheader("Multimedia")
st.image("https://dummyimage.com/500x400/000/fff", caption="Imagen de ejemplo")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Mensajes
st.success("Esto es un mensaje de éxito")
st.warning("Esto es una advertencia")
st.error("Esto es un error")

# Barra de progreso
st.subheader("Progreso")
progress = st.progress(100)

for i in range(100):
    progress.progress(50)

# Footer
st.write("---")
st.caption("App demo hecha con Streamlit")