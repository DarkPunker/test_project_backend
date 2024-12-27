
import config
from fastapi import FastAPI
from router import auth_router, producto_router, tienda_router
from router import librerias_router, categoria_router,  tienda_producto_router, orden_compra_router

app = FastAPI()

# Initialize the database


# Include routers for each endpoint
app.include_router(producto_router.router)
app.include_router(tienda_producto_router.router)
app.include_router(auth_router.router)
app.include_router(categoria_router.router)
app.include_router(librerias_router.router)
app.include_router(tienda_router.router)
app.include_router(orden_compra_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
