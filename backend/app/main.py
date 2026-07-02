from fastapi import FastAPI

app = FastAPI(
    title="ReqForge AI",
    description="AI-Powered Software Requirements & Solution Generator",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ReqForge AI API",
        "status": "running"
    }