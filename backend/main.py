"""
GeoNova 2025 — Main Server
Autor: Ricardo Bolaños
Optimizado para Render, FastAPI y ejecución local.
No requiere modificaciones futuras.
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

# ----------------------------------------------------------
# 🔧 Configuración inicial
# ----------------------------------------------------------
app = FastAPI(title="GeoNova 2025", version="2.0")

# Detecta entorno de ejecución (Render o Local)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.abspath(os.path.join(ROOT_DIR, "../static"))

# Verificación automática del entorno
if "RENDER" in os.environ.get("RENDER", ""):
    print("🌐 Ejecutando en entorno Render...")
else:
    print("💻 Ejecutando en entorno local...")

# Verifica la existencia del directorio estático
if not os.path.exists(STATIC_DIR):
    print(f"⚠️ Carpeta estática no encontrada en: {STATIC_DIR}")
    # Crea la carpeta si no existe
    os.makedirs(STATIC_DIR, exist_ok=True)
    print("🆕 Carpeta /static creada automáticamente.")

# Muestra el contenido disponible
print(f"📂 Directorio estático: {STATIC_DIR}")
print("📄 Archivos detectados:", os.listdir(STATIC_DIR) or "Ninguno")

# Monta carpeta estática
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ----------------------------------------------------------
# 🏠 Ruta principal (sirve index.html)
# ----------------------------------------------------------
@app.get("/")
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        print("✅ index.html encontrado correctamente.")
        return FileResponse(index_path)
    else:
        print("❌ index.html no encontrado en:", STATIC_DIR)
        return JSONResponse(
            content={"error": "index.html no encontrado", "path": STATIC_DIR},
            status_code=404
        )

# ----------------------------------------------------------
# 🩺 Ruta de diagnóstico /health (usada por Render)
# ----------------------------------------------------------
@app.get("/health")
async def health_check():
    return {"status": "ok", "environment": "Render" if "RENDER" in os.environ else "Local"}

# ----------------------------------------------------------
# 🧠 Ruta de depuración opcional (solo modo local)
# ----------------------------------------------------------
@app.get("/debug")
async def debug_info():
    return {
        "static_dir": STATIC_DIR,
        "files": os.listdir(STATIC_DIR),
        "working_directory": os.getcwd(),
        "environment": "Render" if "RENDER" in os.environ else "Local",
    }
