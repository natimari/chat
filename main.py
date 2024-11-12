import streamlit as st
from groq import Groq 

st.set_page_config(page_title="mi chat de ia", page_icon="🎇")
st.title("mi priemra aplicacion")
nombre = st.text_input("¿Cuál es tu nombre?")

if st.button("Saludar") :
    st.write(f"¡Hola, {nombre}! gracias por venir a Talento Tech")

MODELO = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key = clave_secreta)


def configurar_modelo(cliente, modelo, mensaje):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user","content": mensaje}],
        stream = True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append(
        {"role": rol, "content": contenido, "avatar": avatar}
    )

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje ["avatar"]) : 
            st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height= 400, border= True)
    with contenedorDelChat : mostrar_historial()

def configurar_pagina():
    st.title("mi chat de ia")
    st.sidebar.title("configuracion")
    elegirModelo = st.sidebar.selectbox(
        "titulo",
        MODELO,
        index = 2
    )

    return elegirModelo


def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        print(frase)


#invocacion de funciones
modelo = configurar_pagina()
clienteUsuario = crear_usuario_groq()
inicializar_estado()
area_chat()
mensaje = st.chat_input("escribi tu mensaje: ")
#st.write(f"usuario: {mensaje}")

if mensaje: 
    actualizar_historial("user", mensaje, "🎆")
    chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
    generar_respuesta(chat_completo)
    actualizar_historial("assistant", chat_completo, "🎇")
    st.rerun()
    #print(mensaje)

