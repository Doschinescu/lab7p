from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import uvicorn

app = FastAPI(
    title="Workout Tracker API",
    description="Backend for Lab6 Workout Tracker",
    version="1.0.0"
)

# ✅ CORS Configuration
origins = [
    "http://localhost:5173/Lab6/",  # Frontend development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Use ["*"] to allow all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your API routes
app.include_router(router)

# ✅ Run the app
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
