import os 
from google import genai as genai 
from dotenv import load_dotenv

#cargamos lo del archivo 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# ia configuracion API!!!
client = genai.Client(api_key=api_key)

# async aprendi que es para que haga como multitasking y no bloquee toda la pagina

async def obtener_consejo_ia(negocio: str, utilidad: float, margen: float):
    # el prompt para la ia
    prompt = await client.aio.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = f"""
        Actúa como un Consultor Financiero Senior experto en PYMES colombianas.
        Tu objetivo es analizar los datos del negocio "{negocio}" y dar un consejo táctico inmediato.

        DATOS DEL NEGOCIO:
        - Nombre: {negocio}
        - Utilidad Neta: ${utilidad}
        - Margen de Ganancia: {margen}%

        INSTRUCCIONES DE RESPUESTA:
        1. Usa terminología propia del sector de "{negocio}" (ej. si es restaurante habla de mermas o insumos; si es tecnología habla de costos de servidor o licencias).
        2. El consejo debe ser directo: ¿Debe subir precios, bajar costos operativos o invertir en marketing?
        3. Máximo 2 frases. Tono profesional, motivador y ejecutivo.
        4. No saludes, ve directo al grano.

        CONSEJO ESTRATÉGICO:
        """
    ) 
    # llamar a la ia igual q arriba 

   # return f"Simulación: El negocio {negocio} tiene una utilidad de {utilidad}. ¡Buen trabajo!"
    return prompt.text



