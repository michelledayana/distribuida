from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI en Railway"}

# Configuración para Railway
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Usa el puerto de Railway o 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)
