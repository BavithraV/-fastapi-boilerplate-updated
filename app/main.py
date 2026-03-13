from fastapi import FastAPI
from app.api.v1.rating_routes import router as rating_router
from app.config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(rating_router)


@app.get("/health")
def health():
    return {"status": "ok"}