
from fastapi import FastAPI
from fastapi import Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal

from fastapi.middleware.cors import CORSMiddleware
#from app.controllers.tu_jemplo_controller import get_all_funciónEjemplo     #Aquí importarás las funciones desde tus controllers
#from app.routes.tu_ejemplo_router import router as ejemplo_router           #Aquí importarás tus rutas desde tus archivos router

# Inicializa FastAPI app
app = FastAPI()

# Configuración CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen (en producción, especificar dominios permitidos)
    allow_credentials=True,
    allow_methods=["*"],   # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],   # Permite todos los encabezados 
)

#
#app.include_router(ejemplo_router)  #Incluye tus routers en este espacio
#

@app.get("/")
def read_root():
    return {"message": "Bienvenido a tu nueva API!"}