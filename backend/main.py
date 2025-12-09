from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Sistema": "KODO", "Estado": "OPERATIVO", "Mensaje": "Bienvenido al Nexus"}