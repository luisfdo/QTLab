from fastapi import FastAPI

from qtlab.api.studies import router as studies_router


app = FastAPI(
    title="QTLab",
    version="0.1.0",
)

app.include_router(studies_router)


@app.get("/")
def root():
    return {
        "name": "QTLab",
        "version": "0.1.0",
        "status": "running",
    }