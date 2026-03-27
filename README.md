#  Sentinel Pro - AI Financial Advisor

**Sentinel Pro** es un MicroSaaS diseñado para proporcionar asesoría financiera estratégica a pequeñas empresas mediante Inteligencia Artificial de última generación.

## 🚀 Características
- **Análisis Predictivo:** Basado en ingresos y gastos, genera diagnósticos de salud financiera.
- **Motor de IA:** Integración con **Gemini 2.0 Flash** para consejos personalizados según el sector del negocio.
- **Seguridad:** Autenticación robusta con hashing de contraseñas y gestión de sesiones.
- **Persistencia en la Nube:** Historial de análisis almacenado en **Supabase (PostgreSQL)**.

## 🛠️ Stack Tecnológico
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Base de Datos:** Supabase
- **IA:** Google Gemini AI Studio
- **Lenguaje:** Python 3.10+

## 📦 Instalación y Uso
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Configurar las variables de entorno en un archivo `.env`.
5. Ejecutar Backend: `uvicorn main:app --reload`.
6. Ejecutar Frontend: `streamlit run portal.py`.

**   Made with Love by Gabriel Blanco**
