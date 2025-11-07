import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Render ejecuta el código desde /opt/render/project/src/backend
STATIC_DIR = STATIC_DIR = os.path.join(ROOT_DIR, "Static")


print("📁 Intentando servir archivos desde:", STATIC_DIR)
print("📂 Contenido detectado:", os.listdir(STATIC_DIR) if os.path.exists(STATIC_DIR) else "No existe")

# Monta carpeta estática
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(index_path):
        return {"error": f"index.html no encontrado en {STATIC_DIR}"}
    return FileResponse(index_path)
