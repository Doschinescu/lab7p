from fastapi import FastAPI
from routes import router
import uvicorn

app = FastAPI(
    title="Workout Tracker API",
    description="Backend for Lab6 Workout Tracker",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
