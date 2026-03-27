import requests
import streamlit as st
from database import supabase 
import asyncio
from auth_manager import encriptar_contra, verificar_contra
import os
api_key = st.secrets["GEMINI_API_KEY"]
st.set_page_config(page_title="Sentinel Pro Portal", page_icon="🛡️")


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user_email'] = ""
    st.session_state['user_name'] = ""

if st.session_state['logged_in']:
    st.sidebar.title(f"👤Bienvenido, {st.session_state['user_name']}")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.title("📊 Dashboard Sentinel Pro")
    st.info(f"Has iniciado sesión como: {st.session_state['user_email']}")
    

    st.write("---")
    st.subheader("Nuevo Análisis Financiero")
    
    # para los datos que pide tu FastAPI
    negocio = st.text_input("Nombre del Negocio", placeholder="Ej: Mi MicroSaaS")
    col1, col2 = st.columns(2)
    with col1:
        ventas_input = st.number_input("Ventas Totales ($)", min_value=0.0, step=100.0)
    with col2:
        gastos_input = st.number_input("Gastos Totales ($)", min_value=0.0, step=100.0)

    if st.button("Empezar Análisis Pro"):
        if negocio and ventas_input > 0:
            with st.spinner("Empezando analisis..."):
                try:
                    # 2. Llamada real a tu Backend (Uvicorn debe estar prendido)
                    url_api = "sentinel-pro-ai-financial-advisor-znvg2wjtha6fd6a5mfuh7h.streamlit.app/analizar"
                    params = {
                        "ventas": ventas_input,
                        "gastos": gastos_input,
                        "nombre_negocio": negocio,
                        "nombre_usuario": st.session_state['user_name']  # <--- AGREGA ESTA LÍNEA
                    }

                    response = requests.post(url_api, params=params)                   
                    if response.status_code == 200:
                        res = response.json()
                        st.balloons() # ¡Efecto de éxito!
                        
                        # 3. Mostrar los resultados que vienen de FastAPI
                        st.success(f"### {res['saludo_personalizado']}")
                        
                        m1, m2 = st.columns(2)
                        m1.metric("Utilidad Neta", f"${res['utilidad_neta']}")
                        m2.metric("Margen", res['margen_porcentaje'])
                        
                        st.markdown("#### Consejo Estratégico :")
                        st.info(res['consejo_estrategico'])
                        
                        st.caption(f"Estado del motor: {res['analisis_estatico']}")
                    else:
                        st.error("Error en la respuesta del Backend.")
                        
                except Exception as e:
                    st.error(f"No se pudo conectar con el servidor.. Error: {e}")
        else:
            st.warning("Por favor ingresa un nombre y ventas mayores a 0.")


else:
    st.title(" Portal Financiero")
    menu = ["Login", "Registro"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Registro":
        st.subheader("Crear nueva cuenta")
        new_user = st.text_input("Email")
        new_name = st.text_input("Nombre Completo")
        new_password = st.text_input("Contraseña", type='password')

        if st.button("Registrarme"):
            hashed_pw = encriptar_contra(new_password)
            datos = {
                "email": new_user,
                "full_name": new_name,
                "password_hash" : hashed_pw,
                "plan_tipo": "free",
                "analisis_restantes": 3,
                "preferencias_notif": True
            }
            try:
                supabase.table("usuarios").insert(datos).execute()
                st.success("¡Cuenta creada! Ahora puedes ir al Login.")
            except Exception as e:
                st.error(f"Error: {e}")

    elif choice == "Login":
        st.subheader("Bienvenido de nuevo")
        username = st.text_input("Email")
        password = st.text_input("Contraseña", type='password')

        if st.button("Entrar"):
            res = supabase.table("usuarios").select("*").eq("email", username).execute()
            
            if res.data:
                hash_en_db = res.data[0]['password_hash']
                if verificar_contra(password, hash_en_db):

                    st.session_state['logged_in'] = True
                    st.session_state['user_email'] = username
                    st.session_state['user_name'] = res.data[0]['full_name']
                    st.rerun() 
                else:
                    st.error("Contraseña incorrecta")
            else:
                st.error("El usuario no existe")