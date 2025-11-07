import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
<<<<<<< HEAD

# Render ejecuta el código desde /opt/render/project/src/backend
STATIC_DIR = STATIC_DIR = os.path.join(ROOT_DIR, "Static")


print("📁 Intentando servir archivos desde:", STATIC_DIR)
print("📂 Contenido detectado:", os.listdir(STATIC_DIR) if os.path.exists(STATIC_DIR) else "No existe")

# Monta carpeta estática
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

=======
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "../static")

# 🧩 Verificación temporal: listar contenido del directorio estático
try:
    print("📁 Archivos detectados en STATIC_DIR:", os.listdir(STATIC_DIR))
except Exception as e:
    print("⚠️ Error al listar STATIC_DIR:", e)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
>>>>>>> ea119c03f5e56eef88d45c67be8943bff19303f6
@app.get("/")
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(index_path):
<<<<<<< HEAD
        return {"error": f"index.html no encontrado en {STATIC_DIR}"}
    return FileResponse(index_path)
=======
        return {"error": "index.html no encontrado en /static"}
    return FileResponse(index_path)


      
>>>>>>> ea119c03f5e56eef88d45c67be8943bff19303f6
