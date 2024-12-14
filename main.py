# main.py
import config
from fastapi import FastAPI

from router import producto_router, tienda_router,cliente_router,  campos_de_formularios_router 

app = FastAPI()

# Initialize the database


# Include routers for each endpoint
app.include_router(producto_router.router)
app.include_router(campos_de_formularios_router.router)
app.include_router(tienda_router.router)
app.include_router(cliente_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
