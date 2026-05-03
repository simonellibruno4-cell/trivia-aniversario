import os
import base64
import time
import streamlit as st

def musica_continua(nombre_archivo):
    # Detecta la carpeta donde está guardado este script (trivia_amor.py)
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_base, nombre_archivo)
    
    # Verificación de depuración
    if not os.path.exists(ruta_completa):
        st.error(f"No encuentro el archivo {nombre_archivo} en {ruta_base}")
        return

    with open(ruta_completa, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
    
    audio_html = f"""
        <audio id="bg-audio" loop autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("bg-audio");
            var time = localStorage.getItem("audioTime");
            if (time) {{ audio.currentTime = time; }}
            audio.play();
            setInterval(function() {{
                localStorage.setItem("audioTime", audio.currentTime);
            }}, 1000);
        </script>
    """
    st.components.v1.html(audio_html, height=0)

# Llamala solo con el nombre del archivo, sin rutas manuales
musica_continua("swim.mp3")


# Configuración de página
st.set_page_config(page_title="Trivia de Nuestro Amor ❤️", page_icon="❤️")


# Inicializar estados de la sesión 
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'pregunta' not in st.session_state:
    st.session_state.pregunta = 1

# Estilo para el título principal en Magenta
st.markdown("<h1 style='text-align: center; color: #FF00FF;'>💖 BIENVENIDA A LA TRIVIA DE NUESTRO AMOR</h1>", unsafe_allow_html=True)

# --- LÓGICA DE PREGUNTAS CON COLORES ---

if st.session_state.pregunta == 1:
    st.markdown("<h3 style='color: #FFFF00;'>1. ¿Que canción me recomendaste, que te mande una foto acostado escuchandola?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p1").strip().lower()
    if st.button("Enviar"):
        if "devil's advocate" in res or "devil advocate" in res:
            st.success("¡Correcto! te acordaste de esa foto. ✅")
            st.session_state.puntos += 1
        else:
            st.error("era Devil's Advocate 😔.")
        time.sleep(5)
        st.session_state.pregunta = 2
        st.rerun()

elif st.session_state.pregunta == 2:
    st.markdown("<h3 style='color: #FFFF00;'>2. ¿Qué película fuimos a ver cuando salimos por primera vez? (escribilo en ingles)</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p2").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["the exorcist: believer", "the exorcist believer", "the exorcist"]):
            st.success("¡Exacto! Que pelicula poronga jajaj. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! Era la de the exorcist believer.")
        time.sleep(5)
        st.session_state.pregunta = 3
        st.rerun()

elif st.session_state.pregunta == 3:
    st.markdown("<h3 style='color: #FFFF00;'>3. ¿Que hicimos cuando cumplimos 1 año de novios?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p3").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["fuimos a comer a motz", "comimos en motz", "comimos hamburguesa de motz", "fuimos a motz"]):
            st.success("¡Correcto! podriamos comer en motz 🍔 (guiño,guiño). ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! comimos unas hamburguesas en motz.")
        time.sleep(5)
        st.session_state.pregunta = 4
        st.rerun()

elif st.session_state.pregunta == 4:
    st.markdown("<h3 style='color: #FFFF00;'>4. ¿Qué hicimos un 4 de enero de 2024?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p4").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["ginecologo", "doctor", "medico"]):
            st.success("¡Correcto! nos dio un susto la desgarrada de chucha. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! fuimos al ginecologo porque te desgarre la chucha.")
        time.sleep(5)
        st.session_state.pregunta = 5
        st.rerun()

elif st.session_state.pregunta == 5:
    st.markdown("<h3 style='color: #FFFF00;'>5. ¿te acordas que hamburguesa comimos un 5/6 de mayo de 2025?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p5").strip().lower()
    if st.button("Enviar"):
       if any(x in res for x in ["doritos", "la de doritos", "dorimotz", "la de motz de doritos", "hamburguesa de doritos"]):
            st.success("¡Correcto! Que rica esa hamburguesa, podriamos ir a comer alli de nuevo 🍔. ✅")
            st.session_state.puntos += 1
    else:
            st.error("¡No! comimos la hamburguesa de doritos.")
    time.sleep(5)
    st.session_state.pregunta = 6
    st.rerun()

elif st.session_state.pregunta == 6:
    st.markdown("<h3 style='color: #FFFF00;'>6. ¿Qué hicimos despues del cumpleaños de santy julio de 2024?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p6").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["primer video", "el video", "video", "el primer video"]):
            st.success("¡Correcto! Es hermoso el video. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! Hicimos nuestro primer video.")
        time.sleep(5)
        st.session_state.pregunta = 7
        st.rerun()

elif st.session_state.pregunta == 7:
    st.markdown("<h3 style='color: #FFFF00;'>7. ¿Qué palabra dije cuando estabamos desayunando que fue muy graciosa?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p7").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["quason", "cuason", "croissant"]):
            st.success("¡Correcto! quasoooooon 🥐. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! era quasoooon.")
        time.sleep(5)
        st.session_state.pregunta = 8
        st.rerun()

elif st.session_state.pregunta == 8:
    st.markdown("<h3 style='color: #FFFF00;'>8. ¿Qué pelicula vimos cuando estuvimos en mi casa solos?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p8").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["como entrenar a tu dragon", "dragon", "entrenar a tu dragon"]):
            st.success("¡Correcto! que buena pelicula, me faltaba ver 1 mas 🐉. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! era como entrenar a tu dragon 🏋️🐉.")
        time.sleep(5)
        st.session_state.pregunta = 9
        st.rerun()

elif st.session_state.pregunta == 9:
    st.markdown("<h3 style='color: #FFFF00;'>9. ¿Te acordas a donde fuimos a desayunar un 27 de agosto de 2024?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p9").strip().lower()
    if st.button("Enviar"):
        if "atipico" in res:
            st.success("¡Correcto! Estaba rico ese desayuno. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! fuimos atipico.")
        time.sleep(5)
        st.session_state.pregunta = 10
        st.rerun()

elif st.session_state.pregunta == 10:
    st.markdown("<h3 style='color: #FFFF00;'>10. ¿Qué te regale para un cumple mes de febrero del 2025?</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p10").strip().lower()
    if st.button("Enviar"):
        if any(x in res for x in ["cuadro", "el cuadro", "la pintura"]):
            st.success("¡Correcto! todo un picasso, un salvador dali. ✅")
            st.session_state.puntos += 1
        else:
            st.error("¡No! era el cuadro que tenes colgado😔.")
        time.sleep(5)
        st.session_state.pregunta = 11
        st.rerun()

elif st.session_state.pregunta == 11:
    st.markdown("<h3 style='color: #FF00FF;'>pregunta final. ¿Me das la cola? 🤔</h3>", unsafe_allow_html=True)
    res = st.text_input("Tu respuesta:", key="p11").strip().lower()
    if st.button("Enviar Final"):
        st.markdown("<h4 style='color: #FF69B4;'>¡Correcto! que rico me entregas el chiquito(cualquier respuesta es correcta jiji). 🔥</h4>", unsafe_allow_html=True)
        st.session_state.puntos += 1
        time.sleep(5)
        st.session_state.pregunta = 12
        st.rerun()

# --- RESULTADO FINAL ---
elif st.session_state.pregunta == 12:
    st.balloons()
    st.markdown("<h2 style='color: #FF00FF;'>===========================================</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='color: #FF4B4B; text-align: center;'>¡FELICITACIONES! Lograste {st.session_state.puntos} puntos. ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #FF00FF;'>===========================================</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #FF4B4B;'>Feliz mes amooor 2 años y 6 meses wooow❤️.</h3>", unsafe_allow_html=True)
    st.write("Sos todo para mi amor, gracias por todo lo que haces por mi y por todo mi amor.")
    st.write("Espero ser tu compañero de vida hasta que nos mueramos, y despues de muertos tambien jajaja.")
    st.markdown("<p style='color: #FF4B4B; font-weight: bold;'>Te amo con todo mi corazon, sos lo mejor que me paso en la vida, y espero que podamos seguir creando recuerdos hermosos juntos por muchos años mas❤️♾️.</p>", unsafe_allow_html=True)

    if st.button("Reiniciar"):
        st.session_state.puntos = 0
        st.session_state.pregunta = 1
        st.rerun()