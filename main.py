from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import uvicorn

app = FastAPI(
    title="Workout Tracker API",
    description="Backend for Lab6 Workout Tracker",
    version="1.0.0"
)

# ✅ CORRECT origin format: No path, just scheme + host + port
origins = [
    "http://localhost:5173",  # Local dev frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
