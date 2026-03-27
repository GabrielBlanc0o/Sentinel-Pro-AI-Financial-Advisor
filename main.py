from fastapi import FastAPI
from ai_engine import obtener_consejo_ia
from fastapi.middleware.cors import CORSMiddleware # para seguiridad local
from database import guardar_analisis
#la instancia 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que cualquier web se conecte (solo para desarrollo)
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)
# endpoint primero 
@app.get("/")
async def root():
    return {"mensaje":"Sentinel API esta en linea","estado":"Operativo"}

#logica de algo basico plus la ruta web 
@app.post("/analizar")
async def analizar_ventas(ventas: float, gastos: float, nombre_negocio : str,nombre_usuario: str):
    if ventas <= 0:
        return {"error": "Las ventas deben ser mayores a cero para calcular el margen."}
    
    
    utilidad = ventas - gastos
    margen = (utilidad / ventas)* 100
    prompt_res = await obtener_consejo_ia(nombre_negocio,utilidad,margen)
    #await guardar_analisis(nombre_negocio, utilidad, round(margen,2), prompt_res)
    try:
        # MANDAMOS LOS 6 ARGUMENTOS QUE PIDE LA TABLA
        await guardar_analisis(
            nombre_negocio, 
            ventas,          
            gastos,         
            utilidad, 
            round(margen, 2), 
            prompt_res
        )
        print(" ¡Guardado exitoso en la nube!")
    except Exception as e:
        print(f" Error guardando en Supabase: {e}")
        
    return {
        "negocio": nombre_negocio,
        "utilidad_neta" : utilidad,
        "margen_porcentaje" : f"{round(float(margen))}%",
        "analisis_estatico": "Margen saludable" if margen > 20 else "Revisar costos",
        "consejo_estrategico": prompt_res,
        "saludo_personalizado" : f"Hola {nombre_usuario}, el analisis para {nombre_negocio} es..."
    }

