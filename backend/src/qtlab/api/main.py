from fastapi import FastAPI

from qtlab.api.studies import router as studies_router
from qtlab.infrastructure.database import Base, engine


app = FastAPI(
    title="QTLab",
    version="0.1.0",
)

app.include_router(studies_router)
# Create the database
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "name": "QTLab",
        "version": "0.1.0",
        "status": "running",
    }