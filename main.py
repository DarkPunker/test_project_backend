# main.py
from fastapi import FastAPI
from model.database import init_db

from .model.database import init_db
from .router import producto_router #categoria_router, tienda_router, comentario_router, cliente_router

app = FastAPI()

# Initialize the database
#init_db()

# Include routers for each endpoint
#app.include_router(producto_router.router)
# app.include_router(categoria_router.router)
# app.include_router(tienda_router.router)
# app.include_router(comentario_router.router)
# app.include_router(cliente_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
