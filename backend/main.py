from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import subprocess
import os
import uuid

app = FastAPI()

# --- CONFIGURACIÓN CORS ---
# Esto es vital: Permite que tu Svelte (puerto 5173) hable con Python (puerto 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción esto se restringe, para local está bien "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carpeta donde guardaremos los archivos (dentro del contenedor)
# Gracias a Docker, esto se ve en tu carpeta 'kodo_files' de Windows
UPLOAD_DIR = "/app/converted_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"Sistema": "KODO", "Estado": "LISTO PARA PROCESAR"}

@app.post("/convert")
async def convert_file(file: UploadFile = File(...)):
    """
    Recibe un archivo, lo guarda y lo convierte a MP4 usando FFmpeg.
    """
    # 1. Generar un ID único para no mezclar archivos
    unique_id = str(uuid.uuid4())[:8]
    input_filename = f"{unique_id}_{file.filename}"
    output_filename = f"converted_{unique_id}.mp4" # Por defecto convertimos a MP4
    
    input_path = os.path.join(UPLOAD_DIR, input_filename)
    output_path = os.path.join(UPLOAD_DIR, output_filename)

    # 2. Guardar el archivo subido en el disco
    try:
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return {"status": "error", "message": f"Error al guardar: {str(e)}"}

    # 3. EJECUTAR FFMPEG (La magia de Linux)
    # Comando: ffmpeg -i entrada -preset ultrafast salida.mp4
    ffmpeg_cmd = [
        "ffmpeg", "-y",          # -y = Sobreescribir si existe
        "-i", input_path,        # Archivo de entrada
        "-c:v", "libx264",       # Codec de video estándar
        "-preset", "ultrafast",  # Conversión rápida para pruebas
        output_path              # Archivo de salida
    ]

    print(f" > EJECUTANDO: {' '.join(ffmpeg_cmd)}") # Log para ver en la terminal
    
    # Lanzamos el subproceso
    result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)

    # 4. Verificar si funcionó
    if result.returncode != 0:
        print(f"ERROR FFMPEG: {result.stderr}")
        return {"status": "error", "message": "Fallo en la conversión", "log": result.stderr}

    # 5. Devolver la URL para descargar
    # Nota: Usamos localhost:8000 porque estás en local
    download_url = f"http://localhost:8000/download/{output_filename}"
    
    return {
        "status": "success", 
        "original": file.filename,
        "converted": output_filename,
        "download_url": download_url
    }

@app.get("/download/{filename}")
async def download_file(filename: str):
    """Permite descargar el archivo convertido forzando la descarga"""
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    if os.path.exists(file_path):
        # El truco está aquí: añadimos 'filename=' y 'media_type'
        return FileResponse(
            path=file_path, 
            filename=filename,  # Esto le dice al navegador el nombre real
            media_type='application/octet-stream' # Esto fuerza la descarga binaria
        )
    return {"error": "Archivo no encontrado (¿Lo borró el sistema?)"}