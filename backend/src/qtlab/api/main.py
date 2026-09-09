from fastapi import FastAPI


app = FastAPI(
    title="QTLab",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "QTLab",
        "version": "0.1.0",
        "status": "running",
    }