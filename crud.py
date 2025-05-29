from database import collection
from bson import ObjectId

def workout_helper(workout) -> dict:
    workout["id"] = str(workout["_id"])
    del workout["_id"]
    return workout

async def get_workouts(skip=0, limit=10):
    items = await collection.find().skip(skip).limit(limit).to_list(length=limit)
    return [workout_helper(item) for item in items]

async def create_workout(workout):
    new = await collection.insert_one(workout.dict())
    return workout_helper(await collection.find_one({"_id": new.inserted_id}))

async def delete_workout(workout_id):
    return await collection.delete_one({"_id": ObjectId(workout_id)})

async def update_workout(workout_id, workout):
    await collection.update_one(
        {"_id": ObjectId(workout_id)},
        {"$set": workout.dict(exclude={"id"})}
    )
    return await collection.find_one({"_id": ObjectId(workout_id)})
