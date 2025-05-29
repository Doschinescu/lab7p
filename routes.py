from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth import create_token, verify_token
from models import WorkoutIn, TokenRequest
import crud

router = APIRouter()
auth_scheme = HTTPBearer()

def check_permissions(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload

@router.post("/token")
async def get_token(data: TokenRequest):
    token = create_token(data.dict())
    return {"token": token}

@router.get("/workouts")
async def list_workouts(skip: int = 0, limit: int = 10, user=Depends(check_permissions)):
    return await crud.get_workouts(skip, limit)

@router.post("/workouts")
async def add_workout(workout: WorkoutIn, user=Depends(check_permissions)):
    if "WRITE" not in user["permissions"]:
        raise HTTPException(status_code=403, detail="No permission to write")
    return await crud.create_workout(workout)

@router.put("/workouts/{workout_id}")
async def update_workout(workout_id: str, workout: WorkoutIn, user=Depends(check_permissions)):
    return await crud.update_workout(workout_id, workout)

@router.delete("/workouts/{workout_id}")
async def delete_workout(workout_id: str, user=Depends(check_permissions)):
    return await crud.delete_workout(workout_id)
