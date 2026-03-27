import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargamos variables de entorno
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configuración correcta para la librería google-generativeai
genai.configure(api_key=api_key)

async def obtener_consejo_ia(negocio: str, utilidad: float, margen: float):
    model = genai.GenerativeModel('gemini-3-flash')
    
    prompt_text = f"""
        Actúa como un Consultor Financiero Senior experto en PYMES colombianas.
        Tu objetivo es analizar los datos del negocio "{negocio}" y dar un consejo táctico inmediato.

        DATOS DEL NEGOCIO:
        - Nombre: {negocio}
        - Utilidad Neta: ${utilidad}
        - Margen de Ganancia: {margen}%

        INSTRUCCIONES DE RESPUESTA:
        1. Usa terminología propia del sector de "{negocio}" (ej. mermas, insumos, costos operativos).
        2. El consejo debe ser directo: ¿Subir precios, bajar costos o invertir en marketing?
        3. Máximo 2 frases. Tono profesional y ejecutivo.
        4. No saludes, ve directo al grano.
    """

    # La librería estándar usa generate_content_async para el modo non-blocking
    response = await model.generate_content_async(prompt_text)
    
    return response.text