from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from qtlab.api.studies import router as studies_router
from qtlab.infrastructure.database import Base, engine


app = FastAPI(
    title="QTLab",
    version="0.1.0",
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(studies_router)
# Create the databases
# Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "name": "QTLab",
        "version": "0.1.0",
        "status": "running",
    }