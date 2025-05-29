from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Workout(BaseModel):
    id: Optional[str]
    type: str
    distance: Optional[float]
    duration: float
    notes: Optional[str]
    liked: Optional[bool] = False
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)

class WorkoutIn(Workout):
    pass

class TokenRequest(BaseModel):
    role: Optional[str] = "ADMIN"
    permissions: Optional[List[str]] = ["READ", "WRITE"]
