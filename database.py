import os
from supabase import create_client,  Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_PUBLISHABLE_DEFAULT_KEY")
supabase: Client = create_client(url, key)

async def guardar_analisis(negocio, ventas, gastos, utilidad, margen, consejo):
 
    datos = {
        "negocio": negocio,
        "ventas": float(ventas),   # Aseguramos que sean números para float8
        "gastos": float(gastos),
        "utilidad": float(utilidad),
        "margen": float(margen),
        "consejo": consejo
    }

    return supabase.table("analisis_financieros").insert(datos).execute()