import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "../static")

# 🧩 Verificación temporal: listar contenido del directorio estático
try:
    print("📁 Archivos detectados en STATIC_DIR:", os.listdir(STATIC_DIR))
except Exception as e:
    print("⚠️ Error al listar STATIC_DIR:", e)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# 📁 Ruta absoluta al directorio 'static'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "../static")

# 🚀 Monta archivos estáticos (HTML, CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 🏠 Ruta raíz → devuelve index.html
@app.get("/")
def read_root():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "index.html no encontrado en /static"}

# ✅ Prueba de salud (para verificar desde Render o localhost)
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "GeoNova 2025 está corriendo correctamente."}
