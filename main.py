# main.py
import config
from fastapi import FastAPI

from router import producto_router, tienda_router,cliente_router, usuario_router
from router import librerias_router, categoria_router, comentario_router, tienda_producto_router

app = FastAPI()

# Initialize the database


# Include routers for each endpoint
app.include_router(producto_router.router)
app.include_router(tienda_producto_router.router)
app.include_router(usuario_router.router)
app.include_router(categoria_router.router)
app.include_router(comentario_router.router)
app.include_router(librerias_router.router)
app.include_router(tienda_router.router)
app.include_router(cliente_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
