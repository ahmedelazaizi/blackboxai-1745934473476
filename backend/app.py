from fastapi import FastAPI
from backend.auth import router as auth_router
from backend.portal_config import router as portal_config_router
from backend.invoices import router as invoices_router

app = FastAPI(title="Egyptian E-Invoice Integration API")

app.include_router(auth_router)
app.include_router(portal_config_router)
app.include_router(invoices_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
